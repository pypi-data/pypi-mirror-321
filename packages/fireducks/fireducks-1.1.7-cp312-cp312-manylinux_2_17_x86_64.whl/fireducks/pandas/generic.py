# Copyright (c) 2023 NEC Corporation. All Rights Reserved.

import os
import numpy as np
import pandas
import pandas.api.extensions as pandas_extensions
from pandas.core.dtypes.common import is_dict_like
from pandas.compat.numpy import function as nv
from pandas.util._validators import validate_bool_kwarg
from pandas.util._decorators import deprecate_nonkeyword_arguments
import pandas._libs.lib as pandas_lib
from pandas.core.dtypes.common import is_float

from fireducks import ir, irutils
from fireducks.pandas.indexing import _LocIndexer, _IlocIndexer
from fireducks.pandas.binop import is_inplace_binop
from fireducks.pandas.wrappers import Index, MultiIndex, DatetimeIndex
import fireducks.core
import fireducks.pandas
import fireducks.pandas.utils as utils
from fireducks.pandas.metadata import IRMetadataWrapper
import firefw as fire

import functools
import logging
import operator
import types
import warnings

# import warnings

logger = logging.getLogger(__name__)


class FireDucksPandasCompatMetaclass(type):
    def __getattr__(cls, name):
        logger.debug(
            "FireDucksPandasCompatMetaclass.__getattr__: name=%s", name
        )

        def unwrap(reason):
            return utils._pandas_class(cls)

        return utils.fallback_attr(unwrap, name)

    # __setattr__ is not defined here because we have no attribute which should
    # be set to pandas class. As far as we know, class attributes which are set
    # by a user is "_metadata" and "__finalize__", but those are set to
    # fireducks class.


class FireDucksObject:
    def __init__(self, value: fire.Value):
        self._value = value
        value.bind(self)

    def _rebind(self, value):
        """Rebind self to value."""
        value.bind(self._value.unbind())
        self._value = value

        if fireducks.core.get_fireducks_options().benchmark_mode:
            self._evaluate()

    # fireducks method

    def _evaluate(self, options=None, _logger=None):
        logger.debug("FireDucksObject._evaluate")
        fireducks.core.evaluate([self._value], options, _logger)
        return self


class FireDucksMetadata:
    """Metadata."""

    def __init__(self, *, hint=None):
        self.pandas_object_cache = None
        self.hint = hint
        self._internal_referrers = []

    def add_internal_referrer(self, referrer):
        """Be careful that adding referrer to internal referrer also increases
        refcount of the referrer!"""
        logger.debug("add_extra_internal_referrer")
        self._internal_referrers.append(referrer)

    def get_internal_referrers(self):
        return self._internal_referrers

    def get_cache(self):
        return self.pandas_object_cache

    def invalidate_cache(self):
        logger.debug("invalidate_cache")
        self.pandas_object_cache = None

    def is_cached(self):
        return self.get_cache() is not None

    def set_cache(self, obj: pandas.DataFrame):
        logger.debug("set_cache: %x", id(obj))
        self.pandas_object_cache = obj

    def invalidate_hint(self):
        self.hint = None


def _install_fallback_mutating_method(cls, name):
    def wrapper(self, *args, **kwargs):
        reason = f"{name} (mutating method) is not yet implemented"
        return self._fallback_mutating_method(
            name, args, kwargs, reason=reason
        )

    type.__setattr__(cls, name, wrapper)


def _install_binops(cls, pandas_cls):
    binops = [
        # methods
        "add",
        "floordiv",
        "mod",
        "mul",
        "pow",
        "sub",
        "truediv",
        "radd",
        "rfloordiv",
        "rmod",
        "rmul",
        "rpow",
        "rsub",
        "rtruediv",
        # operators
        "__add__",
        "__floordiv__",
        "__mod__",
        "__mul__",
        "__pow__",
        "__sub__",
        "__truediv__",
        "__iadd__",
        "__ifloordiv__",
        "__imod__",
        "__imul__",
        "__ipow__",
        "__isub__",
        "__itruediv__",
        "__radd__",
        "__rfloordiv__",
        "__rmod__",
        "__rmul__",
        "__rpow__",
        "__rsub__",
        "__rtruediv__",
        # Comparison
        # TODO: Pandas has difference among comparison functions and operators
        # such as `eq` and `==` (`__eq__`). But we do not know much of this
        # difference, our IR supports only operators at the moment.
        # 'eq', 'ge', 'gt', 'le', 'lt', 'ne',
        "__eq__",
        "__ge__",
        "__gt__",
        "__le__",
        "__lt__",
        "__ne__",
        # logical
        "__and__",
        "__or__",
        "__xor__",
        "__iand__",
        "__ior__",
        "__ixor__",
        "__rand__",
        "__ror__",
        "__rxor__",
    ]  # yapf: disable

    for op in binops:
        realop = op.replace("_", "")

        @functools.wraps(getattr(pandas_cls, op))
        def wrapper(self, other, *args, op_=realop, originop=op, **kwargs):
            # As pandas we do not allow __op__ takes additional arguments
            if originop.startswith("__") and args:
                raise TypeError(
                    "takes 2 positional arguments but 3 were given"
                )

            # FireDucks IR does not have inplace binops. It will be implemented
            # as out-of-place binop and rebind
            inplace = is_inplace_binop(op_)
            if inplace:
                op_ = op_[1:]

            return self._build_binop(
                other, op_, originop, args, kwargs, inplace=inplace
            )

        # Use `type._setattr__` to bypass metaclass's `__setattr__`
        type.__setattr__(cls, op, wrapper)

    type.__setattr__(cls, "div", getattr(cls, "truediv"))
    type.__setattr__(cls, "rdiv", getattr(cls, "rtruediv"))
    type.__setattr__(cls, "__div__", getattr(cls, "truediv"))
    type.__setattr__(cls, "__idiv__", getattr(cls, "__itruediv__"))


def _install_unary_op_fallbacks(cls, parent):
    # Explicit fallbacks are required since __getattr__ does not hook special
    # methods
    methods = [
        # unary ops
        "__bool__",
        "__invert__",
        "__iter__",
        "__pos__",
    ]
    utils.install_fallbacks(cls, methods, parent)


def _get_inplace(pos, default, args, kwargs):
    """
    Return true if `inplace` argument in `args` or `kwargs` is true. If inplace
    is only in kswargs, `pos` should be -1.
    """
    if pos >= 0 and len(args) > pos:
        return args[pos]
    return kwargs.get("inplace", default)


def _from_pandas_to_value(obj):
    if isinstance(obj, pandas.DataFrame):
        from fireducks.pandas.frame import _from_pandas_frame

        return _from_pandas_frame(obj)
    elif isinstance(obj, pandas.Series):
        from fireducks.pandas.series import _from_pandas_series

        return _from_pandas_series(obj)
    raise RuntimeError(
        "fireducks._from_pandas_to_value: unknown object is given: "
        f"{type(obj)}"
    )


def _setup_FireDucksPandsCompat(cls):
    fallback_methods = [
        # Explicit fallbacks are required since __getattr__ does not hook
        # special methods
        # These methods have to be defined in a super class of DataFrame
        # because those might be called explicitly like `super(DataFrame,
        # df).rename_axis` as some test cases in pandas.tests do.
        "rename_axis",
        "drop",
        "interpolate",
        "_where",
        "mask",
        "__delitem__",
        "__matmul__",
        "__rmatmul__",
        "__array_ufunc__",
    ]
    utils.install_fallbacks(cls, fallback_methods)

    return cls


def _wrap_pandas(cls, pandas_cls):
    inherited_methods = set()
    for attr_name, attr_value in vars(cls).items():
        if not attr_name.startswith("_") and isinstance(
            attr_value, types.FunctionType
        ):
            pandas_func = getattr(pandas_cls, attr_name, None)
            inherited_methods.add(attr_name)
            if pandas_func:
                functools.update_wrapper(attr_value, pandas_func)

    # Add the super class methods to the class for docsting
    super_cls = cls.__bases__[0]
    for attr_name, attr_value in vars(super_cls).items():
        if (
            not attr_name.startswith("_")
            and attr_name not in inherited_methods
            and isinstance(attr_value, types.FunctionType)
        ):
            pandas_func = getattr(pandas_cls, attr_name, None)
            if pandas_func:

                @functools.wraps(pandas_func)
                def wrapper(self, *args, _func=attr_value, **kwargs):
                    return _func(self, *args, **kwargs)

                type.__setattr__(cls, attr_name, wrapper)


@_setup_FireDucksPandsCompat
class FireDucksPandasCompat(
    FireDucksObject, metaclass=FireDucksPandasCompatMetaclass
):
    """
    Super class of fireducks.pandas.DataFrame and Series to share
    implementation.

    This class does not intend to be compatible with
    pandas.core.generic.NDFrame.
    """

    # DataFrame is not hashable as pandas. Because we define __eq__,
    # we have to set None explicitly. See GT #1229
    __hash__ = None

    def __init__(self, value, *, pandas_object=None, hint=None):
        logger.debug("FireDucksPandasCompat.__init__: hint=%s", hint)
        super().__init__(value)
        metadata = FireDucksMetadata(hint=hint)
        metadata.set_cache(pandas_object)
        object.__setattr__(self, "_fireducks_meta", metadata)

    @property
    def _fireducks_hint(self):
        """
        Return hint if available, otherwise None

        Return
        ======
        :class:`fireducks.pandas.hinting.hint.TableHint` or None
        """
        return self._fireducks_meta.hint

    def __finalize__(self, other, method=None):
        return self

    def _rebind(self, value, *, invalidate_cache=False):
        super()._rebind(value)
        if invalidate_cache:
            self._fireducks_meta.invalidate_cache()
            self._fireducks_meta.invalidate_hint()

    def _unwrap(self, reason=None):
        return self.to_pandas(reason=f"unwrap ({reason})")

    def _get_fallback(self, inplace):
        if inplace:
            return self._fallback_mutating_method
        return self._fallback_call_packed

    def _get_metadata(self):
        assert fireducks.core.get_ir_prop().has_metadata
        value = ir.get_metadata(self._value)
        metadata = fireducks.core.evaluate([value])[0]
        return IRMetadataWrapper(metadata)

    # Deprecated. Use _fallback_call_packed
    def _fallback_call(self, __fireducks_method, *args, **kwargs):
        reason = kwargs.pop("__fireducks_reason", None)
        return utils.fallback_call_packed(
            self._unwrap, __fireducks_method, args, kwargs, reason=reason
        )

    def _fallback_call_packed(
        self, method, args=None, kwargs=None, *, reason=None, stacklevel=7
    ):
        return utils.fallback_call_packed(
            self._unwrap,
            method,
            args,
            kwargs,
            reason=reason,
            stacklevel=stacklevel,
        )

    def _fallback_may_inplace(
        self,
        method,
        args,
        kwargs,
        *,
        pos=-1,
        default=False,
        reason=None,
        stacklevel=9,
    ):
        logger.debug(
            "_fallback_may_inplace: method=%s inplace=%s",
            method,
            _get_inplace(pos, default, args, kwargs),
        )
        fallback = self._get_fallback(_get_inplace(pos, default, args, kwargs))
        return fallback(
            method, args, kwargs, reason=reason, stacklevel=stacklevel
        )

    def _rebind_to_cache(self):
        """Rebind self to cached object"""
        assert self._fireducks_meta.is_cached()  # fallback sets cache
        obj = self._fireducks_meta.get_cache()
        value = _from_pandas_to_value(obj)
        self._rebind(value)
        self._fireducks_meta.invalidate_hint()

    # A mutating method changes itself. We have to rebuild self._value because
    # it holds the value before this mutating method.
    def _fallback_mutating_method(
        self, method, args=None, kwargs=None, *, reason=None, stacklevel=7
    ):
        logger.debug("_fallback_mutating_method: %s", method)
        args = [] if args is None else args
        kwargs = {} if kwargs is None else kwargs

        # dfkl backend does not need this evaluation because tables in the dfkl
        # backend are immutable and depending ops can be executed safely after
        # executing this mutating method. But because tables in a pandas
        # backend are not immutable, we will evaluate depending ops here.
        fireducks.core.evaluate_ops_depending_on_defs_of([self._value])

        # At the moment, we allow `from_pandas` to do zero-copy as dfkl
        # backend. It means that a table managed by a backend might share
        # actual data buffer with pandas and such pandas object might be cached
        # at frontend. To prevent a pandas's mutating method from updating such
        # a shared buffer, the cache will be invalidated here. Without a cache,
        # unwrap during fallback creates copy of the buffer.  See GT #2693
        self._fireducks_meta.invalidate_cache()

        ret = self._fallback_call_packed(
            method, args, kwargs, reason=reason, stacklevel=stacklevel
        )
        self._rebind_to_cache()
        return ret

    # In-place binop returns self.
    def _fallback_inplace_binop(self, __fireducks_method, *args, **kwargs):
        self._fallback_mutating_method(__fireducks_method, args, kwargs)
        return self

    def __getattr__(self, name):
        """Fallback of missing attribute"""
        reason = f"{type(self).__name__}.__getattr__ for {name} is called"
        return utils.fallback_attr(self._unwrap, name, reason)

    def __getstate__(self):
        logger.debug("DataFrame.__getstate__")
        return self.to_pandas().__getstate__()

    def _invalidate_cache(self):
        self._fireducks_meta.invalidate_cache()
        return self

    def _set_index_names(self, names):  # inplace: self.index.names = names
        logger.debug("%s._set_index_names", self.__class__.__name__)
        names = irutils.make_tuple_of_scalars(names)
        value = ir.set_index_names(self._value, names)
        self._rebind(value, invalidate_cache=True)

    def _slice(self, slobj, axis=0):
        assert isinstance(slobj, slice), type(slobj)
        reason = None
        if axis != 0:
            reason = f"unsupported axis: {axis} for slicing"

        step = slobj.step or 1
        if step != 1:
            reason = f"unsupported step: {step} for slicing"

        if reason:
            return self._fallback_call(
                "_slice", slobj, __fireducks_reason=reason
            )
        start = slobj.start or 0
        stop = irutils.make_scalar(slobj.stop)
        return self.__class__._create(ir.slice(self._value, start, stop, step))

    def _sort_index(
        self,
        args,
        kwargs,
        *,
        decoded_args,
        is_series,
    ):
        known_kinds = ("quicksort", "mergesort", "heapsort", "stable")
        known_unstable_sort = ("quicksort", "heapsort")
        known_na_position = ("first", "last")

        if decoded_args.kind is None:
            decoded_args.kind = "quicksort"  # default kind

        if decoded_args.axis != 0 and decoded_args.axis != "index":
            reason = "axis is not 0"
        elif not isinstance(decoded_args.ignore_index, bool):
            reason = "ignore_index is not bool"
        elif not isinstance(decoded_args.inplace, bool):
            reason = "inplace is not bool"
        elif decoded_args.kind not in known_kinds:
            reason = f"kind is not in [{', '.join(known_kinds)}]"
        elif decoded_args.na_position not in known_na_position:
            reason = f"na_position is not in [{', '.join(known_na_position)}]"
        else:
            reason = decoded_args.is_not_default(
                exclude=[
                    "axis",
                    "ascending",
                    "ignore_index",
                    "inplace",
                    "kind",
                    "na_position",
                ]
            )

        if reason:
            if callable(decoded_args.level):

                def wrapper(*args, **kwargs):
                    return utils._unwrap(decoded_args.level(*args, **kwargs))

                kwargs["level"] = wrapper

            return self._fallback_may_inplace(
                "sort_index", args, kwargs, pos=3, reason=reason
            )

        if irutils.irable_scalar(decoded_args.ascending):
            ascending = bool(decoded_args.ascending)
        else:
            ascending = [bool(e) for e in decoded_args.ascending]
        orders = irutils.make_vector_or_scalar_of_scalar(ascending)
        na_pos = decoded_args.na_position != "first"
        stable = decoded_args.kind not in known_unstable_sort

        value = ir.sort_index(
            self._value,
            orders,
            ignore_index=decoded_args.ignore_index,
            is_series=is_series,
            na_pos=na_pos,
            stable=stable,
        )
        return self._create_or_inplace(value, decoded_args.inplace)

    def _sort_values(
        self,
        args,
        kwargs,
        *,
        decoded_args,
        by,
        ascending,
        is_series,
    ):
        known_kinds = ("quicksort", "mergesort", "heapsort", "stable")
        known_unstable_sort = ("quicksort", "heapsort")
        known_na_position = ("first", "last")

        if decoded_args.kind is None:
            decoded_args.kind = "quicksort"  # default kind

        if decoded_args.axis != 0 and decoded_args.axis != "index":
            reason = "axis is not 0"
        elif not isinstance(decoded_args.ignore_index, bool):
            reason = "ignore_index is not bool"
        elif not isinstance(decoded_args.inplace, bool):
            reason = "inplace is not bool"
        elif decoded_args.kind not in known_kinds:
            reason = f"kind is not in [{', '.join(known_kinds)}]"
        elif decoded_args.na_position not in known_na_position:
            reason = f"na_position is not in [{', '.join(known_na_position)}]"
        else:
            reason = decoded_args.is_not_default(
                exclude=[
                    "axis",
                    "ascending",
                    "by",
                    "ignore_index",
                    "inplace",
                    "kind",
                    "na_position",
                ]
            )

        if reason:
            if callable(decoded_args.key):

                def wrapper(*args, **kwargs):
                    return utils._unwrap(decoded_args.key(*args, **kwargs))

                kwargs["key"] = wrapper

            return self._fallback_may_inplace(
                "sort_values", args, kwargs, pos=3, reason=reason
            )

        keys = irutils.make_tuple_of_column_names(by)
        orders = ir.make_tuple_i1([bool(a) for a in ascending])
        na_pos = decoded_args.na_position != "first"
        stable = decoded_args.kind not in known_unstable_sort

        value = ir.sort_values(
            self._value,
            keys,
            orders,
            ignore_index=decoded_args.ignore_index,
            is_series=is_series,
            na_pos=na_pos,
            stable=stable,
        )
        return self._create_or_inplace(value, decoded_args.inplace)

    def __get_trunc_repr_method_result__(self, method="__repr__"):
        if self._fireducks_meta.is_cached():
            return (
                utils._wrap(
                    getattr(self._fireducks_meta.get_cache(), method)()
                ),
                False,
            )

        n = len(self)
        minr, maxr = (
            pandas.get_option("display.min_rows"),
            pandas.get_option("display.max_rows"),
        )
        need_truncation = maxr is not None and n > maxr
        if need_truncation:
            minr = maxr if minr is None or minr > maxr else minr
            n = minr // 2 + 1  # +1 for truncated view
            tmp = fireducks.pandas.concat([self.head(n), self.tail(n)])
            pandas.set_option("display.max_rows", minr)
            ret = tmp._fallback_call(
                method, __fireducks_reason="with truncated data"
            )
            pandas.set_option("display.max_rows", maxr)
        else:
            ret = self._fallback_call(
                method, __fireducks_reason=f"with full data of size: {n}"
            )
        return ret, need_truncation

    def __str__(self):
        return repr(self)

    def _where_base(self, args, kwargs, decoded_args, accept_classes):
        decoded_args.inplace = validate_bool_kwarg(
            decoded_args.inplace, "inplace"
        )

        axis = decoded_args.axis
        cond = decoded_args.cond
        other = decoded_args.other

        if utils._pd_version_under2:
            reason = decoded_args.is_not_default(
                ["level", "errors", "try_cast"]
            )
        else:
            # pandas2.2 removed 'errors' and 'try_cast' arguments.
            reason = decoded_args.is_not_default(["level"])

        if decoded_args.inplace:
            reason = "inplace is True"
        elif axis is None:
            if isinstance(other, _Scalar):
                reason = "If other is Series, must specify axis=0 or 1"
            else:
                axis = ir.make_null_scalar_null()
        elif axis == 0:
            axis = irutils.make_scalar(axis)
        else:
            reason = "axis is not 0 or None"

        if isinstance(cond, accept_classes):
            condIsSeries = cond.__class__.__name__ == "Series"
            cond = cond._value
        else:
            reason = reason or f"type of cond is {type(cond).__name__}"

        if other is pandas_extensions.no_default or other is np.nan:
            other = ir.make_null_scalar_null()
            othertype = "scalar"
        elif irutils.irable_scalar(other):
            other = irutils.make_scalar(other)
            othertype = "scalar"
        elif isinstance(other, _Scalar):
            other = other._value
            othertype = "scalar"
        elif isinstance(other, accept_classes):
            other = other._value
            othertype = "table"
        else:
            reason = reason or f"type of other is {type(other).__name__}"

        if reason is not None:
            return self._fallback_may_inplace(
                "where", args, kwargs, pos=2, reason=reason
            )

        if othertype == "scalar":
            value = ir.where_scalar(
                self._value, cond, other, axis, condIsSeries
            )
        else:
            value = ir.where_table(
                self._value, cond, other, axis, condIsSeries
            )

        return self._create_or_inplace(value, decoded_args.inplace)

    #
    # Pandas API
    #

    def apply(self, func, *args, **kwargs):
        if callable(func):

            def wrapper(*args, **kwargs):
                # Because func will be called by pandas, args and kwargs might
                # be pandas's object. func might use fireducks's data or func
                # itself is fireducks's function, args and kwargs should be
                # converted to ducks's one.
                args = utils._wrap(args)
                kwargs = utils._wrap(kwargs)
                return utils._unwrap(func(*args, **kwargs))

            args = (wrapper,) + args
            return self._fallback_call_packed(
                "apply", args, kwargs, stacklevel=8
            )
        else:
            args = (func,) + args
            return self._fallback_call_packed(
                "apply", args, kwargs, stacklevel=8
            )

    def astype(self, dtype, copy=True, errors="raise"):
        from fireducks.pandas import Series

        dtype = dtype.to_dict() if isinstance(dtype, Series) else dtype

        def is_supported_dtype_or_dict(dtype):
            if is_dict_like(dtype):
                return irutils.is_column_names(
                    dtype.keys()
                ) and utils.is_supported_dtypes(dtype.values())
            return utils.is_supported_dtype(dtype)

        reason = None
        if isinstance(dtype, Series):
            reason = "dtype is Series"
        elif not is_supported_dtype_or_dict(dtype):
            reason = f"unsupported dtype: {dtype}"
        elif not copy:
            reason = "copy is false"
        elif errors != "raise":
            reason = "errors is not raise"

        if reason:
            return self._fallback_call(
                "astype", dtype, copy, errors, __fireducks_reason=reason
            )

        if is_dict_like(dtype):
            keys = irutils.make_tuple_of_column_names(dtype.keys())
            dtypes = ir.make_tuple_str(
                [utils.to_supported_dtype(t) for t in dtype.values()]
            )
        else:
            keys = irutils.make_tuple_of_column_names([])
            dtypes = ir.make_tuple_str([utils.to_supported_dtype(dtype)])
        return self.__class__._create(ir.cast(self._value, keys, dtypes))

    def copy(self, deep: bool = True):
        # Pandas 1.3.3 _libs/reduction.pyx calls copy with deep='all'
        # https://github.com/pandas-dev/pandas/issues/31441
        if not isinstance(deep, bool):
            result = self._fallback_call("copy", deep)
        else:
            if not deep:
                warnings.warn(
                    "df2 = df1.copy(deep=False) might not work, when changes "
                    "made in the data values of 'df2' is expected to be "
                    "reflected in 'df1'. REF: https://fireducks-dev.github.io"
                    "/docs/user-guide/04-compatibility/#copydeep--false",
                    UserWarning,
                )
            result = self.__class__._create(
                ir.copy(self._value, deep), hint=self._fireducks_hint
            )
        return result.__finalize__(self)

    def describe(self, *args, **kwargs):
        from fireducks.pandas import Series

        cls = self.__class__

        pandas_cls = utils._pandas_class(self.__class__)
        arg = utils.decode_args(args, kwargs, pandas_cls.describe)
        reason = None
        if arg.percentiles is not None:
            reason = "percentiles is not None"
        if arg.include is not None:
            reason = "include is not None"
        if arg.exclude is not None:
            reason = "exclude is not None"
        if utils._pd_version_under2:
            if arg.datetime_is_numeric:
                reason = "datetime_is_numeric is True"

        if not reason:
            if fireducks.core.get_ir_prop().has_metadata:
                target_types = [
                    np.int8,
                    np.int16,
                    np.int32,
                    np.int64,
                    np.uint8,
                    np.uint16,
                    np.uint32,
                    np.uint64,
                    np.float32,
                    np.float64,
                ]
                col_dtypes = (
                    [self.dtype] if cls == Series else list(self.dtypes)
                )
                is_numeric = len(col_dtypes) > 0 and np.any(
                    [i in target_types for i in col_dtypes]
                )
                # fallback in case no numeric column exists
                if not is_numeric:
                    reason = "describe with non-numeric column"

        if reason is not None:
            return self._fallback_call_packed(
                "describe", args, kwargs, reason=reason
            )
        return cls._create(ir.describe(self._value))

    def diff(self, *args, **kwargs):
        pandas_cls = utils._pandas_class(self.__class__)
        arg = utils.decode_args(args, kwargs, pandas_cls.diff)

        periods = arg.periods
        if not pandas_lib.is_integer(periods):
            if not (is_float(periods) and periods.is_integer()):
                raise ValueError("periods must be an integer")
            periods = int(periods)
        elif isinstance(periods, np.integer):
            periods = int(periods)

        assert isinstance(periods, int)

        reason = None
        # Series.diff does not have axis
        if hasattr(arg, "axis") and (arg.axis == 1 or arg.axis == "columns"):
            reason = "axis is not 0"

        if reason:
            return self._fallback_call(
                "diff", *args, **kwargs, __fireducks_reason=reason
            )

        return self.__class__._create(ir.diff(self._value, periods))

    @deprecate_nonkeyword_arguments(
        version=None, allowed_args=["self", "labels"]
    )
    def drop(self, *args, **kwargs):
        pandas_cls = utils._pandas_class(self.__class__)
        arg = utils.decode_args(args, kwargs, pandas_cls.drop)
        arg.inplace = validate_bool_kwarg(arg.inplace, "inplace")
        arg.axis = self._get_axis_number(
            arg.axis
        )  # error if 1/columns for Series

        if arg.labels is not None:
            if arg.index is not None or arg.columns is not None:
                raise ValueError(
                    "Cannot specify both 'labels' and 'index'/'columns'"
                )
            if arg.axis == 1:
                arg.columns = arg.labels
            else:
                arg.index = arg.labels
        elif arg.index is None and arg.columns is None:
            raise ValueError(
                "Need to specify at least one of "
                "'labels', 'index' or 'columns'"
            )
        reason = arg.is_not_default(["level", "errors"])

        output = None
        if reason is None:
            if arg.columns is not None:
                if self.ndim != 1:
                    if isinstance(arg.columns, str):
                        arg.columns = [arg.columns]
                    if utils._is_str_list_or_index(arg.columns):
                        arg.columns = irutils.make_tuple_of_column_names(
                            arg.columns
                        )
                        value = ir.drop_columns(self._value, arg.columns)
                        output = self._create_or_inplace(value, arg.inplace)
                    else:
                        reason = "columns is not a list or Index of str"
                else:
                    output = self  # no change for Series

        if reason is None:
            if arg.index is not None:
                if irutils.irable_scalar(arg.index):
                    arg.index = Index([arg.index])
                if isinstance(arg.index, list):
                    if np.all([irutils.irable_scalar(i) for i in arg.index]):
                        arg.index = Index(arg.index)
                    elif np.all([isinstance(i, tuple) for i in arg.index]):
                        arg.index = MultiIndex.from_tuples(arg.index)
                if isinstance(arg.index, (Index, MultiIndex)):
                    indices = fireducks.pandas.DataFrame(index=arg.index)
                    # output is not None: for drop_rows followed by drop_columns
                    tbl = self if output is None else output
                    output = tbl._create_or_inplace(
                        ir.drop_rows(tbl._value, indices._value), arg.inplace
                    )
                else:
                    reason = "index is not a scalar, list or Index "

        if reason is None:
            return output

        return self._fallback_may_inplace(
            "drop", args, kwargs, pos=5, reason=reason
        )

    def fillna(self, *args, **kwargs):
        pandas_cls = utils._pandas_class(self.__class__)
        arg = utils.decode_args(args, kwargs, pandas_cls.fillna)
        # raises error for invalid axis
        axis = self._get_axis_number(arg.axis or 0)
        fillv = arg.value

        if fillv is None and arg.method is None:
            raise ValueError("Must specify a fill 'value' or 'method'.")

        reason = arg.is_not_default(["method", "limit", "downcast"])
        if not reason and axis != 0:
            reason = (
                f"{self.__class__.__name__}.fillna on "
                f"unsupported axis: {arg.axis}"
            )

        if not reason:
            if fillv is not None and irutils.irable_scalar(fillv):
                # TODO: add implicit casting support to avoid error
                # when filling nulls of string column with non-string scalar
                keys = irutils.make_tuple_of_column_names([])
                dtypes = ir.make_tuple_str([])
                fillv = irutils.make_scalar(fillv)
                return self._create_or_inplace(
                    ir.fillna_scalar(self._value, fillv, keys, dtypes),
                    arg.inplace,
                )

            elif isinstance(self, fireducks.pandas.DataFrame) and is_dict_like(
                fillv
            ):
                cols, vals, reason = utils.get_key_value_tuples(fillv)
                if not reason:
                    return self._create_or_inplace(
                        ir.column_wise_apply(
                            self._value, "fillna", cols, vals
                        ),
                        arg.inplace,
                    )
            else:
                reason = (
                    f"{self.__class__.__name__}.fillna with unsupported "
                    f"'value' of type: {type(fillv).__name__}"
                )

        return self._fallback_may_inplace(
            "fillna", args, kwargs, pos=3, reason=reason
        )

    def head(self, n=5):
        stop = irutils.make_scalar(n)
        return self.__class__._create(ir.slice(self._value, 0, stop, 1))

    @property
    def iloc(self):
        return _IlocIndexer(self)

    @property
    def index(self):
        """The index (row labels) of the DataFrame/Series"""
        logger.debug("%s.index", self.__class__.__name__)
        if self._fireducks_meta.is_cached():
            index = utils._wrap(self._fireducks_meta.get_cache().index)
            index._set_fireducks_frame(self, "index")
            return index

        # trick: just extract only index part to reduce
        # fallback overhead of data columns
        target = (
            self.to_frame()
            if isinstance(self, fireducks.pandas.Series)
            else self
        )
        index_columns = target[[]]

        # TODO: wrap IndexColumns with _value
        index = utils.fallback_attr(
            index_columns._unwrap,
            # self._unwrap,
            "index",
            reason=f"{self.__class__.__name__}.index",
        )
        index._set_fireducks_frame(self, "index")
        return index

    @index.setter
    def index(self, value):
        logger.debug("%s.index: type=%s", self.__class__.__name__, type(value))
        if value is None:
            raise TypeError(
                "Index(...) must be called with a collection of some kind"
                ", None was passed"
            )
        if utils._pd_version_under2:
            return self._set_axis(
                value, axis=0, inplace=True, _inplace_index_setter=True
            )
        else:
            return self._set_axis(value, axis=0, _inplace_index_setter=True)

    def _fallback_set_axis(
        self, args, kwargs, arg, class_name, _inplace_index_setter
    ):
        # If `_inplace_index_setter` is true, this method is called from
        # the property setter of fireducks.Frame.index.

        if utils._pd_version_under2:
            if arg.inplace is True and arg.copy is True:
                raise ValueError(
                    "Cannot specify both inplace=True and copy=True"
                )
            if arg.inplace is pandas_extensions.no_default:
                arg.inplace = False

        reason = None
        if arg.is_not_default(["copy"]) and not arg.copy:
            reason = f"unsupported copy: {arg.copy}"

        if not reason:
            if arg.axis in ("columns", 1) and class_name == "DataFrame":
                if not irutils._is_irable_scalar_arraylike(arg.labels):
                    reason = (
                        f"unsupported value of type: '{type(arg.labels)}'"
                        "for axis=1"
                    )
            elif arg.axis in ("index", 0):
                from fireducks.pandas import Series

                if isinstance(arg.labels, list):
                    if type(arg.labels) is not list:  # FrozenList etc.
                        arg.labels = list(arg.labels)
                    if len(arg.labels) and pandas_lib.is_all_arraylike(
                        arg.labels
                    ):
                        arg.labels = MultiIndex.from_arrays(arg.labels)

                if not isinstance(
                    arg.labels, (Series, Index, MultiIndex, range)
                ) and not irutils._is_irable_scalar_arraylike(arg.labels):
                    reason = (
                        "labels is neither an index-like nor a list of "
                        "irable-scalars or index-like"
                    )

                if isinstance(arg.labels, np.ndarray) and arg.labels.ndim > 1:
                    raise ValueError("Index data must be 1-dimensional")
            else:
                raise ValueError(
                    f"No axis named {arg.axis} for object type {class_name}"
                )

        if not reason and isinstance(arg.labels, DatetimeIndex):
            # FIXME: frequency information is lost when converting
            # Index -> Series, hence falling back when frequency
            # information is available...
            if arg.labels.freq is not None:
                reason = f"labels is a DatetimeIndex of frequency: {arg.labels.freq}"

        if reason is not None:
            if _inplace_index_setter:
                result = self._fallback_mutating_method(
                    "__setattr__", args=["index", arg.labels], reason=reason
                )
            else:
                result = self._fallback_may_inplace(
                    "set_axis", args, kwargs, pos=2, reason=reason
                )
            return (reason, result)
        else:
            return (reason, None)

    @property
    def loc(self):
        return _LocIndexer(self)

    def pipe(self, func, *args, **kwargs):
        import pandas.core.common as com

        return com.pipe(self, func, *args, **kwargs)

    def replace(self, *args, **kwargs):
        pandas_cls = utils._pandas_class(self.__class__)
        arg = utils.decode_args(args, kwargs, pandas_cls.replace)

        reason = None
        if arg.to_replace is None or not irutils.irable_scalar(arg.to_replace):
            reason = "unsupported to_replace argument"
        elif (
            arg.value is pandas_extensions.no_default
            or not irutils.irable_scalar(arg.value)
        ):
            reason = "unsupported value argument"
        else:
            reason = arg.is_not_default(["inplace", "limit", "method"])

        if not isinstance(arg.regex, bool):
            reason = (
                f"unsupported 'regex' of type '{type(arg.regex).__name__}'"
            )

        if reason:
            return self._fallback_may_inplace(
                "replace", args, kwargs, reason=reason
            )

        arg.to_replace = irutils.make_scalar(arg.to_replace)
        arg.value = irutils.make_scalar(arg.value)
        return self.__class__._create(
            ir.replace_scalar(
                self._value, arg.to_replace, arg.value, arg.regex
            )
        )

    def sample(self, *args, **kwargs):
        from pandas.core import common, sample

        pandas_cls = utils._pandas_class(self.__class__)
        arg = utils.decode_args(args, kwargs, pandas_cls.sample)

        n, frac, replace, weights, random_state, axis, ignore_index = (
            arg.n,
            arg.frac,
            arg.replace,
            arg.weights,
            arg.random_state,
            arg.axis,
            arg.ignore_index,
        )

        reason = None
        if weights is not None:
            reason = "weight is not None"

        if reason:
            return self._fallback_call_packed(
                "sample", args, kwargs, reason=reason
            )

        if axis is None:
            axis = 0
        # raises error if axis is 1 or columns when self is Series
        axis = self._get_axis_number(axis)
        obj_len = self.shape[axis]

        # Process random_state argument
        rs = common.random_state(random_state)

        size = sample.process_sampling_size(n, frac, replace)
        if size is None:
            assert frac is not None
            size = round(frac * obj_len)
        sampled_indices = sample.sample(obj_len, size, replace, weights, rs)
        return self._take(
            sampled_indices,
            axis=axis,
            ignore_index=ignore_index,
            check_boundary=False,
            check_negative=False,
        )

    def shift(self, *args, **kwargs):
        pandas_cls = utils._pandas_class(self.__class__)
        arg = utils.decode_args(args, kwargs, pandas_cls.shift)

        reason = arg.is_not_default(["freq", "fill_value"])

        if not reason:
            if arg.axis in (0, "index"):
                if not isinstance(arg.periods, int):
                    reason = f"periods, '{arg.periods}' is not int"
                else:
                    return self.__class__._create(
                        ir.shift(self._value, arg.periods)
                    )
            else:
                reason = f"unsupported axis: '{arg.axis}'"

        return self._fallback_call(
            "shift", *args, **kwargs, __fireducks_reason=reason
        )

    def squeeze(self, *args, **kwargs):
        pandas_cls = utils._pandas_class(self.__class__)
        arg = utils.decode_args(args, kwargs, pandas_cls.squeeze)
        if arg.axis is None:
            # by default all N-1 axes are squeezed
            if self.ndim == 1:  # Series
                nrows = self.shape[0]
                return self.iloc[0] if nrows == 1 else self
            else:
                nrows, ncols = self.shape
                if nrows == 1:
                    return self.iloc[0, 0] if ncols == 1 else self.iloc[0]
                else:
                    return self.iloc[:, 0] if ncols == 1 else self
        else:
            # raises error if axis is 1 or columns when self is Series
            axis = self._get_axis_number(arg.axis)
            if self.ndim == 1:  # Series (axis parameter is unused)
                nrows = self.shape[0]
                return self.iloc[0] if nrows == 1 else self
            else:
                nrows, ncols = self.shape
                if nrows == 1:
                    if axis == 0:
                        return self.iloc[0, :]
                    else:
                        return self.iloc[:, 0] if ncols == 1 else self
                else:
                    if ncols == 1:
                        return self.iloc[:, 0] if axis == 1 else self
                    else:
                        return self

    def tail(self, n=5):
        if n == 0:
            stop = irutils.make_scalar(0)
        else:
            stop = irutils.make_scalar(None)
        return self.__class__._create(ir.slice(self._value, -n, stop, 1))

    def _take(
        self,
        indices,
        axis=0,
        ignore_index=False,
        check_boundary=True,
        check_negative=True,
    ):
        from fireducks.pandas import Series, Index

        input_indices = None
        if isinstance(indices, range):
            indices = slice(indices.start, indices.stop, indices.step)
        if axis == 0:
            if isinstance(indices, slice):
                return self._slice(indices)

            if isinstance(indices, Series):
                input_indices = indices.astype(int)
            elif utils._is_numeric_index_like(indices):
                input_indices = Series(indices).astype(int)
        else:
            # TODO: improve column slicing (ideally number
            # of columns are not very high though...)
            if isinstance(indices, slice):
                nrow, ncol = self.shape  # should not be called for Series
                if (
                    indices.start is None
                    and indices.stop is None
                    and indices.step == -1
                ):
                    indices = np.arange(ncol - 1, -1, -1)
                else:
                    st = indices.start or 0
                    stop = indices.stop or ncol
                    step = indices.step or 1
                    st = ncol + st if st < 0 else st
                    if stop > ncol:
                        stop = ncol
                    elif stop < 0:
                        stop += ncol
                    indices = np.arange(st, stop, step)
            if isinstance(indices, (Series, Index, np.ndarray)):
                input_indices = irutils.make_vector_or_scalar_of_scalar(
                    indices.astype(int).tolist()
                )
            elif irutils._is_list_or_tuple_of(indices, int):
                input_indices = irutils.make_vector_or_scalar_of_scalar(
                    [int(i) for i in indices]
                )

        if input_indices is None:
            reason = (
                f"axis: {axis} take with unsupported indices of "
                f"type: {type(indices).__name__}"
            )
            return self._fallback_call(
                "take", indices, axis, __fireducks_reason=reason
            )
        # input for take_rows is Series, input for take_cols is vector<int>
        input_indices = input_indices._value if axis == 0 else input_indices
        ignore_index = validate_bool_kwarg(ignore_index, "ignore_index")
        check_boundary = validate_bool_kwarg(check_boundary, "check_boundary")
        check_negative = validate_bool_kwarg(check_negative, "check_negative")
        return self.__class__._create(
            ir.take(
                self._value,
                input_indices,
                axis,
                check_boundary,
                check_negative,
                ignore_index,
            )
        )

    def take(self, *args, **kwargs):
        pandas_cls = utils._pandas_class(self.__class__)
        arg = utils.decode_args(args, kwargs, pandas_cls.take)

        if utils._pd_version_under2 and arg.is_copy is not None:
            warnings.warn(
                "is_copy is deprecated and will be removed in a future version. "
                "'take' always returns a copy, so there is no need to specify this.",
                FutureWarning,
            )

        nv.validate_take((), arg.kwargs)

        indices = arg.indices
        axis = self._get_axis_number(arg.axis)
        return self._take(indices, axis=axis)

    # fireducks method
    def to_pandas(self, options=None, reason=None):
        logger.debug("%s.to_pandas: reason: %s", type(self).__name__, reason)
        if self._fireducks_meta.is_cached():
            logger.debug(
                "to_pandas: reuse _fireducks_meta.pandas_object_cache %x",
                id(self._fireducks_meta.get_cache()),
            )
        else:
            logger.debug("to_pandas: need to _evaluate")
            utils.FallbackManager.check(
                f"{self.__class__.__name__}._to_pandas was called"
            )
            self._fireducks_meta.set_cache(self._to_pandas(options=options))

        return self._fireducks_meta.get_cache()

    def to_csv(self, *args, **kwargs):
        pandas_cls = utils._pandas_class(self.__class__)
        decoded = utils.decode_args(args, kwargs, pandas_cls.to_csv)

        sep = decoded.sep
        columns = decoded.columns
        na_rep = decoded.na_rep
        quoting = 0 if decoded.quoting is None else decoded.quoting
        path_or_buf = decoded.path_or_buf

        # NOTE: pandas seems to allow non bool type variable
        index = bool(decoded.index)

        # Workaround: `header` can not be checked by `decoded.is_not_default`
        # because header might be Index or so which can not be compared with
        # default value by `==` operator used in `is_not_default`
        header = False if decoded.header is None else decoded.header
        supp_header = (
            isinstance(header, bool)
            or irutils.is_column_name(header)
            or (
                isinstance(header, list)
                and all([irutils.is_column_name(x) for x in header])
            )
        )

        supp_columns = (
            columns is None
            or irutils.is_column_name(columns)
            or (
                isinstance(columns, list)
                and all([irutils.is_column_name(x) for x in columns])
            )
        )

        if sep is None:
            raise TypeError('"delimiter" must be string, not NoneType')

        reason = None
        if not (
            isinstance(path_or_buf, (str, os.PathLike)) or path_or_buf is None
        ):
            reason = "path_or_buf is not str or None"
        elif decoded.encoding not in (None, "utf-8", "utf8", "UTF-8", "UTF8"):
            reason = f"unsupported encoding: '{decoded.encoding}'"
        elif not supp_header:
            reason = f"unsupported header of type: '{type(header)}'"
        elif not supp_columns:
            reason = f"unsupported columns of type '{type(columns)}'"
        elif not isinstance(sep, str) or len(sep) != 1:
            reason = f"unsupported separator: '{sep}'"
        elif not isinstance(na_rep, str):
            reason = f"unsupported na_rep: '{na_rep}'"
        elif quoting not in [0, 2, 3, 4]:
            # 1: QUOTE_ALL (including NULL) is not supported by arrow
            reason = f"unsupported quoting: '{quoting}'"
        else:
            reason = decoded.is_not_default(
                exclude=[
                    "encoding",
                    "path_or_buf",
                    "index",
                    "header",
                    "columns",
                    "sep",
                    "na_rep",
                    "quoting",
                ]
            )

        if reason is not None:
            return self._fallback_call_packed(
                "to_csv", args, kwargs, reason=reason
            )

        target = self
        if columns is not None:
            target = target[columns]
        is_series = isinstance(target, fireducks.pandas.Series)
        renamed = False

        if not isinstance(header, list):
            header = bool(header)
        if not isinstance(header, bool):
            if is_series:
                if isinstance(header, list):  # no-op otherwise
                    if len(header) > 1:
                        raise ValueError(
                            f"Writing 1 cols but got {len(header)} aliases"
                        )
                    target = target.copy()
                    target.name = header[0]
                    header = True
                    renamed = True
            else:  # must be DataFrame
                target = target.copy()
                # when len(target.columns) != len(header), error
                # will be raised by columns setter
                target.columns = header
                header = True
                renamed = True

        if header and is_series and not renamed:
            # to rename unnamed column as 0
            target = target.to_frame()

        ir_kwargs = {
            "table": target._value,
            "sep": sep,
            "na_rep": na_rep,
            "header": header,
            "index": index,
            "quoting_style": quoting,
        }
        if path_or_buf is None:
            # no filename, returns string output
            ir_func = ir.to_csv
        else:
            ir_func = ir.write_csv
            ir_kwargs["filename"] = (
                path_or_buf.__fspath__()
                if isinstance(path_or_buf, os.PathLike)
                else path_or_buf
            )

        result = ir_func(**ir_kwargs)
        try:
            ret = fireducks.core.evaluate([result])
        except Exception as e:  # RuntimeError etc. at backend
            reason = f"{type(e).__name__}: {e}. Falling back to pandas."
            return self._fallback_call_packed(
                "to_csv", args, kwargs, reason=reason
            )

        return ret[0]  # either string or None

    # aggregation
    def _build_aggregation_op(self, op, *args, **kwargs):
        # redirect to aggregate only when no args and no kwargs because
        # args/kwargs are not completely same as aggregate. For example,
        # aggregate dose not allow axis=None, but some of methods allow.
        if args or kwargs:
            return self._fallback_call(op, *args, **kwargs)

        # Subclasses, DataFrame and Series, implement aggregate
        return self.aggregate(op)

    def _logical_func(self, func, *args, **kwargs):
        reason = None
        pandas_cls = utils._pandas_class(self.__class__)
        arg = utils.decode_args(args, kwargs, getattr(pandas_cls, func))
        nv.validate_logical_func((), arg.kwargs, fname=func)

        if arg.axis is None:
            reason = "axis=None is not supported"
        else:
            reason = arg.is_not_default(exclude=["axis", "kwargs"])

        if reason is not None:
            return self._fallback_call(
                func, *args, **kwargs, __fireducks_reason=reason
            )

        return self.aggregate(func, arg.axis)

    def all(self, *args, **kwargs):
        return self._logical_func("all", *args, **kwargs)

    def any(self, *args, **kwargs):
        return self._logical_func("any", *args, **kwargs)

    def sum(self, *args, **kwargs):
        pandas_cls = utils._pandas_class(self.__class__)
        arg = utils.decode_args(args, kwargs, pandas_cls.sum)

        reason = arg.is_not_default(exclude=["axis"])
        if reason is not None:
            return self._fallback_call(
                "sum", *args, **kwargs, __fireducks_reason=reason
            )

        # TODO: In pandas 2.0, None means sum all elements to scalar.
        if arg.axis is None:
            arg.axis = 0

        return self.aggregate("sum", arg.axis)

    def min(self, *args, **kwargs):
        return self._build_aggregation_op("min", *args, **kwargs)

    def max(self, *args, **kwargs):
        return self._build_aggregation_op("max", *args, **kwargs)

    def mean(self, *args, **kwargs):
        return self._build_aggregation_op("mean", *args, **kwargs)

    def median(self, *args, **kwargs):
        return self._build_aggregation_op("median", *args, **kwargs)

    def count(self, *args, **kwargs):
        return self._build_aggregation_op("count", *args, **kwargs)

    def nunique(self, *args, **kwargs):
        return self._build_aggregation_op("nunique", *args, **kwargs)

    def var(self, *args, **kwargs):
        return self._build_aggregation_op("var", *args, **kwargs)

    def std(self, *args, **kwargs):
        return self._build_aggregation_op("std", *args, **kwargs)

    def skew(self, *args, **kwargs):
        return self._build_aggregation_op("skew", *args, **kwargs)

    def kurt(self, *args, **kwargs):
        return self._build_aggregation_op("kurt", *args, **kwargs)


def setup_Scalar(cls):
    ops = [
        "all",
        "__str__",
        "__bool__",
        "__repr__",
        # unary ops
        "__abs__",
        "__neg__",
    ]  # yapf: disable

    utils.install_fallbacks(cls, ops, override=True)

    bin_ops = [
        "__add__",
        "__floordiv__",
        "__mod__",
        "__mul__",
        "__pow__",
        "__sub__",
        "__truediv__",
        "__radd__",
        "__rfloordiv__",
        "__rmod__",
        "__rmul__",
        "__rpow__",
        "__rsub__",
        "__rtruediv__",
        "__eq__",
        "__ge__",
        "__gt__",
        "__le__",
        "__lt__",
        "__ne__",
        "__and__",
        "__or__",
        "__xor__",
    ]  # yapf: disable

    def get_wrapper(method_name, operator_func, reason):
        @functools.wraps(method_name)
        def wrapper(self, rhs):
            if isinstance(
                rhs, (fireducks.pandas.DataFrame, fireducks.pandas.Series)
            ):
                # Do not evaluate and generate IR if rhs is DataFrame or
                # Series.  e.g. _Scalar.__add__(DataFrame) calls
                # DataFrame.__radd__(_Scalar)
                return NotImplemented
            return operator_func(self._unwrap(reason), rhs)

        return wrapper

    def get_reverse_wrapper(method_name, operator_func, reason):
        @functools.wraps(method_name)
        def wrapper(self, rhs):
            return operator_func(rhs, self._unwrap(reason))

        return wrapper

    for op in bin_ops:
        reason = f"Scalar.{op} is called"

        if op.startswith("__r"):
            # Convert the attribute name from __rand__ to __and__ since operator module does not have __rand__.
            operator_func = getattr(operator, "__" + op[3:])
            wrapper = get_reverse_wrapper(op, operator_func, reason)
        else:
            operator_func = getattr(operator, op)
            wrapper = get_wrapper(op, operator_func, reason)

        utils.install_wrapper(cls, op, wrapper, None, True)

    return cls


@setup_Scalar
class _Scalar(FireDucksObject):
    def _unwrap(self, reason=None):
        from fireducks.fireducks_ext import Scalar

        logger.debug("_Scalar._unwrap: reason=%s", reason)
        val = fireducks.core.evaluate([self._value])[0]
        if isinstance(val, Scalar):
            val = val.to_pandas()
        return np.array(val)[()]  # make numpy scalar

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        if method == "__call__":
            reason = "Scalar.__array_func__ is called"
            # unwrap because self is included in inputs.
            return ufunc(*utils._unwrap(inputs, reason=reason), **kwargs)
        else:
            # TODO: What to do when method is not "__call__"?
            return NotImplemented
