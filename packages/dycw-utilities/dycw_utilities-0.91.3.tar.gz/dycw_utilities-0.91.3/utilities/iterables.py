from __future__ import annotations

import datetime as dt
from collections import Counter
from collections.abc import (
    Callable,
    Hashable,
    Iterable,
    Iterator,
    Mapping,
    Sequence,
    Sized,
)
from collections.abc import Set as AbstractSet
from contextlib import suppress
from dataclasses import dataclass
from enum import Enum
from functools import cmp_to_key, partial, reduce
from itertools import accumulate, chain, groupby, islice, pairwise, product
from math import isnan
from types import NoneType
from typing import (
    TYPE_CHECKING,
    Any,
    Generic,
    Literal,
    Self,
    TypeAlias,
    TypeGuard,
    TypeVar,
    assert_never,
    cast,
    overload,
)

from typing_extensions import override

from utilities.errors import ImpossibleCaseError
from utilities.functions import ensure_hashable, ensure_not_none, ensure_str
from utilities.math import (
    _CheckIntegerEqualError,
    _CheckIntegerEqualOrApproxError,
    _CheckIntegerMaxError,
    _CheckIntegerMinError,
    check_integer,
)
from utilities.reprlib import get_repr
from utilities.sentinel import Sentinel, sentinel
from utilities.zoneinfo import UTC

if TYPE_CHECKING:
    from utilities.types import MaybeIterable, StrMapping


_K = TypeVar("_K")
_T = TypeVar("_T")
_U = TypeVar("_U")
_V = TypeVar("_V")
_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_T3 = TypeVar("_T3")
_T4 = TypeVar("_T4")
_T5 = TypeVar("_T5")
_THashable = TypeVar("_THashable", bound=Hashable)
_UHashable = TypeVar("_UHashable", bound=Hashable)


##


def always_iterable(obj: MaybeIterable[_T], /) -> Iterable[_T]:
    """Typed version of `always_iterable`."""
    obj = cast(Any, obj)
    if isinstance(obj, str | bytes):
        return cast(list[_T], [obj])
    try:
        return iter(cast(Iterable[_T], obj))
    except TypeError:
        return cast(list[_T], [obj])


##


def apply_bijection(
    func: Callable[[_T], _U], iterable: Iterable[_T], /
) -> Mapping[_T, _U]:
    """Apply a function bijectively."""
    keys = list(iterable)
    try:
        check_duplicates(keys)
    except CheckDuplicatesError as error:
        raise _ApplyBijectionDuplicateKeysError(
            keys=keys, counts=error.counts
        ) from None
    values = list(map(func, keys))
    try:
        check_duplicates(values)
    except CheckDuplicatesError as error:
        raise _ApplyBijectionDuplicateValuesError(
            keys=keys, values=values, counts=error.counts
        ) from None
    return dict(zip(keys, values, strict=True))


@dataclass(kw_only=True, slots=True)
class ApplyBijectionError(Exception, Generic[_T]):
    keys: list[_T]
    counts: Mapping[_T, int]


@dataclass(kw_only=True, slots=True)
class _ApplyBijectionDuplicateKeysError(ApplyBijectionError[_T]):
    @override
    def __str__(self) -> str:
        return f"Keys {get_repr(self.keys)} must not contain duplicates; got {get_repr(self.counts)}"


@dataclass(kw_only=True, slots=True)
class _ApplyBijectionDuplicateValuesError(ApplyBijectionError[_T], Generic[_T, _U]):
    values: list[_U]

    @override
    def __str__(self) -> str:
        return f"Values {get_repr(self.values)} must not contain duplicates; got {get_repr(self.counts)}"


##


def apply_to_tuple(func: Callable[..., _T], args: tuple[Any, ...], /) -> _T:
    """Apply a function to a tuple of args."""
    return apply_to_varargs(func, *args)


##


def apply_to_varargs(func: Callable[..., _T], *args: Any) -> _T:
    """Apply a function to a variable number of arguments."""
    return func(*args)


##


def chain_nullable(iterable: Iterable[Iterable[_T | None] | None], /) -> Iterable[_T]:
    """Chain a set of values; ignoring nulls."""
    values = ((i for i in it if i is not None) for it in iterable if it is not None)
    return chain.from_iterable(values)


##


def check_bijection(mapping: Mapping[Any, Hashable], /) -> None:
    """Check if a mapping is a bijection."""
    try:
        check_duplicates(mapping.values())
    except CheckDuplicatesError as error:
        raise CheckBijectionError(mapping=mapping, counts=error.counts) from None


@dataclass(kw_only=True, slots=True)
class CheckBijectionError(Exception, Generic[_THashable]):
    mapping: Mapping[Any, _THashable]
    counts: Mapping[_THashable, int]

    @override
    def __str__(self) -> str:
        return f"Mapping {get_repr(self.mapping)} must be a bijection; got duplicates {get_repr(self.counts)}"


##


def check_duplicates(iterable: Iterable[Hashable], /) -> None:
    """Check if an iterable contains any duplicates."""
    counts = {k: v for k, v in Counter(iterable).items() if v > 1}
    if len(counts) >= 1:
        raise CheckDuplicatesError(iterable=iterable, counts=counts)


@dataclass(kw_only=True, slots=True)
class CheckDuplicatesError(Exception, Generic[_THashable]):
    iterable: Iterable[_THashable]
    counts: Mapping[_THashable, int]

    @override
    def __str__(self) -> str:
        return f"Iterable {get_repr(self.iterable)} must not contain duplicates; got {get_repr(self.counts)}"


##


def check_iterables_equal(left: Iterable[Any], right: Iterable[Any], /) -> None:
    """Check that a pair of iterables are equal."""
    left_list, right_list = map(list, [left, right])
    errors: list[tuple[int, Any, Any]] = []
    state: _CheckIterablesEqualState | None
    it = zip(left_list, right_list, strict=True)
    try:
        for i, (lv, rv) in enumerate(it):
            if lv != rv:
                errors.append((i, lv, rv))
    except ValueError as error:
        msg = ensure_str(one(error.args))
        match msg:
            case "zip() argument 2 is longer than argument 1":
                state = "right_longer"
            case "zip() argument 2 is shorter than argument 1":
                state = "left_longer"
            case _:  # pragma: no cover
                raise
    else:
        state = None
    if (len(errors) >= 1) or (state is not None):
        raise CheckIterablesEqualError(
            left=left_list, right=right_list, errors=errors, state=state
        )


_CheckIterablesEqualState: TypeAlias = Literal["left_longer", "right_longer"]


@dataclass(kw_only=True, slots=True)
class CheckIterablesEqualError(Exception, Generic[_T]):
    left: list[_T]
    right: list[_T]
    errors: list[tuple[int, _T, _T]]
    state: _CheckIterablesEqualState | None

    @override
    def __str__(self) -> str:
        parts = list(self._yield_parts())
        match parts:
            case (desc,):
                pass
            case first, second:
                desc = f"{first} and {second}"
            case _:  # pragma: no cover
                raise ImpossibleCaseError(case=[f"{parts=}"])
        return f"Iterables {get_repr(self.left)} and {get_repr(self.right)} must be equal; {desc}"

    def _yield_parts(self) -> Iterator[str]:
        if len(self.errors) >= 1:
            errors = [(f"{i=}", lv, rv) for i, lv, rv in self.errors]
            yield f"differing items were {get_repr(errors)}"
        match self.state:
            case "left_longer":
                yield "left was longer"
            case "right_longer":
                yield "right was longer"
            case None:
                pass
            case _ as never:
                assert_never(never)


##


def check_length(
    obj: Sized,
    /,
    *,
    equal: int | None = None,
    equal_or_approx: int | tuple[int, float] | None = None,
    min: int | None = None,  # noqa: A002
    max: int | None = None,  # noqa: A002
) -> None:
    """Check the length of an object."""
    n = len(obj)
    try:
        check_integer(n, equal=equal, equal_or_approx=equal_or_approx, min=min, max=max)
    except _CheckIntegerEqualError as error:
        raise _CheckLengthEqualError(obj=obj, equal=error.equal) from None
    except _CheckIntegerEqualOrApproxError as error:
        raise _CheckLengthEqualOrApproxError(
            obj=obj, equal_or_approx=error.equal_or_approx
        ) from None
    except _CheckIntegerMinError as error:
        raise _CheckLengthMinError(obj=obj, min_=error.min_) from None
    except _CheckIntegerMaxError as error:
        raise _CheckLengthMaxError(obj=obj, max_=error.max_) from None


@dataclass(kw_only=True, slots=True)
class CheckLengthError(Exception):
    obj: Sized


@dataclass(kw_only=True, slots=True)
class _CheckLengthEqualError(CheckLengthError):
    equal: int

    @override
    def __str__(self) -> str:
        return f"Object {get_repr(self.obj)} must have length {self.equal}; got {len(self.obj)}"


@dataclass(kw_only=True, slots=True)
class _CheckLengthEqualOrApproxError(CheckLengthError):
    equal_or_approx: int | tuple[int, float]

    @override
    def __str__(self) -> str:
        match self.equal_or_approx:
            case target, error:
                desc = f"approximate length {target} (error {error:%})"
            case target:
                desc = f"length {target}"
        return f"Object {get_repr(self.obj)} must have {desc}; got {len(self.obj)}"


@dataclass(kw_only=True, slots=True)
class _CheckLengthMinError(CheckLengthError):
    min_: int

    @override
    def __str__(self) -> str:
        return f"Object {get_repr(self.obj)} must have minimum length {self.min_}; got {len(self.obj)}"


@dataclass(kw_only=True, slots=True)
class _CheckLengthMaxError(CheckLengthError):
    max_: int

    @override
    def __str__(self) -> str:
        return f"Object {get_repr(self.obj)} must have maximum length {self.max_}; got {len(self.obj)}"


##


def check_lengths_equal(left: Sized, right: Sized, /) -> None:
    """Check that a pair of sizes objects have equal length."""
    if len(left) != len(right):
        raise CheckLengthsEqualError(left=left, right=right)


@dataclass(kw_only=True, slots=True)
class CheckLengthsEqualError(Exception):
    left: Sized
    right: Sized

    @override
    def __str__(self) -> str:
        return f"Sized objects {get_repr(self.left)} and {get_repr(self.right)} must have the same length; got {len(self.left)} and {len(self.right)}"


##


def check_mappings_equal(left: Mapping[Any, Any], right: Mapping[Any, Any], /) -> None:
    """Check that a pair of mappings are equal."""
    left_keys, right_keys = set(left), set(right)
    try:
        check_sets_equal(left_keys, right_keys)
    except CheckSetsEqualError as error:
        left_extra, right_extra = map(set, [error.left_extra, error.right_extra])
    else:
        left_extra = right_extra = set()
    errors: list[tuple[Any, Any, Any]] = []
    for key in left_keys & right_keys:
        lv, rv = left[key], right[key]
        if lv != rv:
            errors.append((key, lv, rv))
    if (len(left_extra) >= 1) or (len(right_extra) >= 1) or (len(errors) >= 1):
        raise CheckMappingsEqualError(
            left=left,
            right=right,
            left_extra=left_extra,
            right_extra=right_extra,
            errors=errors,
        )


@dataclass(kw_only=True, slots=True)
class CheckMappingsEqualError(Exception, Generic[_K, _V]):
    left: Mapping[_K, _V]
    right: Mapping[_K, _V]
    left_extra: AbstractSet[_K]
    right_extra: AbstractSet[_K]
    errors: list[tuple[_K, _V, _V]]

    @override
    def __str__(self) -> str:
        parts = list(self._yield_parts())
        match parts:
            case (desc,):
                pass
            case first, second:
                desc = f"{first} and {second}"
            case first, second, third:
                desc = f"{first}, {second} and {third}"
            case _:  # pragma: no cover
                raise ImpossibleCaseError(case=[f"{parts=}"])
        return f"Mappings {get_repr(self.left)} and {get_repr(self.right)} must be equal; {desc}"

    def _yield_parts(self) -> Iterator[str]:
        if len(self.left_extra) >= 1:
            yield f"left had extra keys {get_repr(self.left_extra)}"
        if len(self.right_extra) >= 1:
            yield f"right had extra keys {get_repr(self.right_extra)}"
        if len(self.errors) >= 1:
            errors = [(f"{k=}", lv, rv) for k, lv, rv in self.errors]
            yield f"differing values were {get_repr(errors)}"


##


def check_sets_equal(left: Iterable[Any], right: Iterable[Any], /) -> None:
    """Check that a pair of sets are equal."""
    left_as_set = set(left)
    right_as_set = set(right)
    left_extra = left_as_set - right_as_set
    right_extra = right_as_set - left_as_set
    if (len(left_extra) >= 1) or (len(right_extra) >= 1):
        raise CheckSetsEqualError(
            left=left_as_set,
            right=right_as_set,
            left_extra=left_extra,
            right_extra=right_extra,
        )


@dataclass(kw_only=True, slots=True)
class CheckSetsEqualError(Exception, Generic[_T]):
    left: AbstractSet[_T]
    right: AbstractSet[_T]
    left_extra: AbstractSet[_T]
    right_extra: AbstractSet[_T]

    @override
    def __str__(self) -> str:
        parts = list(self._yield_parts())
        match parts:
            case (desc,):
                pass
            case first, second:
                desc = f"{first} and {second}"
            case _:  # pragma: no cover
                raise ImpossibleCaseError(case=[f"{parts=}"])
        return f"Sets {get_repr(self.left)} and {get_repr(self.right)} must be equal; {desc}"

    def _yield_parts(self) -> Iterator[str]:
        if len(self.left_extra) >= 1:
            yield f"left had extra items {get_repr(self.left_extra)}"
        if len(self.right_extra) >= 1:
            yield f"right had extra items {get_repr(self.right_extra)}"


##


def check_submapping(left: Mapping[Any, Any], right: Mapping[Any, Any], /) -> None:
    """Check that a mapping is a subset of another mapping."""
    left_keys, right_keys = set(left), set(right)
    try:
        check_subset(left_keys, right_keys)
    except CheckSubSetError as error:
        extra = set(error.extra)
    else:
        extra = set()
    errors: list[tuple[Any, Any, Any]] = []
    for key in left_keys & right_keys:
        lv, rv = left[key], right[key]
        if lv != rv:
            errors.append((key, lv, rv))
    if (len(extra) >= 1) or (len(errors) >= 1):
        raise CheckSubMappingError(left=left, right=right, extra=extra, errors=errors)


@dataclass(kw_only=True, slots=True)
class CheckSubMappingError(Exception, Generic[_K, _V]):
    left: Mapping[_K, _V]
    right: Mapping[_K, _V]
    extra: AbstractSet[_K]
    errors: list[tuple[_K, _V, _V]]

    @override
    def __str__(self) -> str:
        parts = list(self._yield_parts())
        match parts:
            case (desc,):
                pass
            case first, second:
                desc = f"{first} and {second}"
            case _:  # pragma: no cover
                raise ImpossibleCaseError(case=[f"{parts=}"])
        return f"Mapping {get_repr(self.left)} must be a submapping of {get_repr(self.right)}; {desc}"

    def _yield_parts(self) -> Iterator[str]:
        if len(self.extra) >= 1:
            yield f"left had extra keys {get_repr(self.extra)}"
        if len(self.errors) >= 1:
            errors = [(f"{k=}", lv, rv) for k, lv, rv in self.errors]
            yield f"differing values were {get_repr(errors)}"


##


def check_subset(left: Iterable[Any], right: Iterable[Any], /) -> None:
    """Check that a set is a subset of another set."""
    left_as_set = set(left)
    right_as_set = set(right)
    extra = left_as_set - right_as_set
    if len(extra) >= 1:
        raise CheckSubSetError(left=left_as_set, right=right_as_set, extra=extra)


@dataclass(kw_only=True, slots=True)
class CheckSubSetError(Exception, Generic[_T]):
    left: AbstractSet[_T]
    right: AbstractSet[_T]
    extra: AbstractSet[_T]

    @override
    def __str__(self) -> str:
        return f"Set {get_repr(self.left)} must be a subset of {get_repr(self.right)}; left had extra items {get_repr(self.extra)}"


##


def check_supermapping(left: Mapping[Any, Any], right: Mapping[Any, Any], /) -> None:
    """Check that a mapping is a superset of another mapping."""
    left_keys, right_keys = set(left), set(right)
    try:
        check_superset(left_keys, right_keys)
    except CheckSuperSetError as error:
        extra = set(error.extra)
    else:
        extra = set()
    errors: list[tuple[Any, Any, Any]] = []
    for key in left_keys & right_keys:
        lv, rv = left[key], right[key]
        if lv != rv:
            errors.append((key, lv, rv))
    if (len(extra) >= 1) or (len(errors) >= 1):
        raise CheckSuperMappingError(left=left, right=right, extra=extra, errors=errors)


@dataclass(kw_only=True, slots=True)
class CheckSuperMappingError(Exception, Generic[_K, _V]):
    left: Mapping[_K, _V]
    right: Mapping[_K, _V]
    extra: AbstractSet[_K]
    errors: list[tuple[_K, _V, _V]]

    @override
    def __str__(self) -> str:
        parts = list(self._yield_parts())
        match parts:
            case (desc,):
                pass
            case first, second:
                desc = f"{first} and {second}"
            case _:  # pragma: no cover
                raise ImpossibleCaseError(case=[f"{parts=}"])
        return f"Mapping {get_repr(self.left)} must be a supermapping of {get_repr(self.right)}; {desc}"

    def _yield_parts(self) -> Iterator[str]:
        if len(self.extra) >= 1:
            yield f"right had extra keys {get_repr(self.extra)}"
        if len(self.errors) >= 1:
            errors = [(f"{k=}", lv, rv) for k, lv, rv in self.errors]
            yield f"differing values were {get_repr(errors)}"


##


def check_superset(left: Iterable[Any], right: Iterable[Any], /) -> None:
    """Check that a set is a superset of another set."""
    left_as_set = set(left)
    right_as_set = set(right)
    extra = right_as_set - left_as_set
    if len(extra) >= 1:
        raise CheckSuperSetError(left=left_as_set, right=right_as_set, extra=extra)


@dataclass(kw_only=True, slots=True)
class CheckSuperSetError(Exception, Generic[_T]):
    left: AbstractSet[_T]
    right: AbstractSet[_T]
    extra: AbstractSet[_T]

    @override
    def __str__(self) -> str:
        return f"Set {get_repr(self.left)} must be a superset of {get_repr(self.right)}; right had extra items {get_repr(self.extra)}."


##


def check_unique_modulo_case(iterable: Iterable[str], /) -> None:
    """Check that an iterable of strings is unique modulo case."""
    try:
        _ = apply_bijection(str.lower, iterable)
    except _ApplyBijectionDuplicateKeysError as error:
        raise _CheckUniqueModuloCaseDuplicateStringsError(
            keys=error.keys, counts=error.counts
        ) from None
    except _ApplyBijectionDuplicateValuesError as error:
        raise _CheckUniqueModuloCaseDuplicateLowerCaseStringsError(
            keys=error.keys, values=error.values, counts=error.counts
        ) from None


@dataclass(kw_only=True, slots=True)
class CheckUniqueModuloCaseError(Exception):
    keys: Iterable[str]
    counts: Mapping[str, int]


@dataclass(kw_only=True, slots=True)
class _CheckUniqueModuloCaseDuplicateStringsError(CheckUniqueModuloCaseError):
    @override
    def __str__(self) -> str:
        return f"Strings {get_repr(self.keys)} must not contain duplicates; got {get_repr(self.counts)}"


@dataclass(kw_only=True, slots=True)
class _CheckUniqueModuloCaseDuplicateLowerCaseStringsError(CheckUniqueModuloCaseError):
    values: Iterable[str]

    @override
    def __str__(self) -> str:
        return f"Strings {get_repr(self.values)} must not contain duplicates (modulo case); got {get_repr(self.counts)}"


##


def chunked(iterable: Iterable[_T], n: int, /) -> Iterator[Sequence[_T]]:
    """Break an iterable into lists of length n."""
    return iter(partial(take, n, iter(iterable)), [])


##


class Collection(frozenset[_THashable]):
    """A collection of hashable, sortable items."""

    def __new__(cls, *item_or_items: MaybeIterable[_THashable]) -> Self:
        items = list(chain(*map(always_iterable, item_or_items)))
        cls.check_items(items)
        return super().__new__(cls, items)

    def __init__(self, *item_or_items: MaybeIterable[_THashable]) -> None:
        super().__init__()
        _ = item_or_items

    @override
    def __and__(self, other: MaybeIterable[_THashable], /) -> Self:
        if isinstance(other, type(self)):
            return type(self)(super().__and__(other))
        return self.__and__(type(self)(other))

    @override
    def __or__(self, other: MaybeIterable[_THashable], /) -> Self:
        if isinstance(other, type(self)):
            return type(self)(super().__or__(other))
        return self.__or__(type(self)(other))

    @override
    def __sub__(self, other: MaybeIterable[_THashable], /) -> Self:
        if isinstance(other, type(self)):
            return type(self)(super().__sub__(other))
        return self.__sub__(type(self)(other))

    @classmethod
    def check_items(cls, items: Iterable[_THashable], /) -> None:
        _ = items

    def filter(self, func: Callable[[_THashable], bool], /) -> Self:
        return type(self)(filter(func, self))

    def map(
        self, func: Callable[[_THashable], _UHashable], /
    ) -> Collection[_UHashable]:
        values = cast(Any, map(func, self))
        return cast(Any, type(self)(values))

    def partition(self, func: Callable[[_THashable], bool], /) -> tuple[Self, Self]:
        from more_itertools import partition

        is_false, is_true = partition(func, self)
        return type(self)(is_false), type(self)(is_true)


##


def ensure_hashables(
    *args: Any, **kwargs: Any
) -> tuple[list[Hashable], dict[str, Hashable]]:
    """Ensure a set of positional & keyword arguments are all hashable."""
    hash_args = list(map(ensure_hashable, args))
    hash_kwargs = {k: ensure_hashable(v) for k, v in kwargs.items()}
    return hash_args, hash_kwargs


##


def ensure_iterable(obj: Any, /) -> Iterable[Any]:
    """Ensure an object is iterable."""
    if is_iterable(obj):
        return obj
    raise EnsureIterableError(obj=obj)


@dataclass(kw_only=True, slots=True)
class EnsureIterableError(Exception):
    obj: Any

    @override
    def __str__(self) -> str:
        return f"Object {get_repr(self.obj)} must be iterable"


##


def ensure_iterable_not_str(obj: Any, /) -> Iterable[Any]:
    """Ensure an object is iterable, but not a string."""
    if is_iterable_not_str(obj):
        return obj
    raise EnsureIterableNotStrError(obj=obj)


@dataclass(kw_only=True, slots=True)
class EnsureIterableNotStrError(Exception):
    obj: Any

    @override
    def __str__(self) -> str:
        return f"Object {get_repr(self.obj)} must be iterable, but not a string"


##


def expanding_window(iterable: Iterable[_T], /) -> islice[list[_T]]:
    """Yield an expanding window over an iterable."""

    def func(acc: Iterable[_T], el: _T, /) -> list[_T]:
        return list(chain(acc, [el]))

    return islice(accumulate(iterable, func=func, initial=[]), 1, None)


##


@overload
def filter_include_and_exclude(
    iterable: Iterable[_T],
    /,
    *,
    include: MaybeIterable[_U] | None = None,
    exclude: MaybeIterable[_U] | None = None,
    key: Callable[[_T], _U],
) -> Iterable[_T]: ...
@overload
def filter_include_and_exclude(
    iterable: Iterable[_T],
    /,
    *,
    include: MaybeIterable[_T] | None = None,
    exclude: MaybeIterable[_T] | None = None,
    key: Callable[[_T], Any] | None = None,
) -> Iterable[_T]: ...
def filter_include_and_exclude(
    iterable: Iterable[_T],
    /,
    *,
    include: MaybeIterable[_U] | None = None,
    exclude: MaybeIterable[_U] | None = None,
    key: Callable[[_T], _U] | None = None,
) -> Iterable[_T]:
    """Filter an iterable based on an inclusion/exclusion pair."""
    include, exclude = resolve_include_and_exclude(include=include, exclude=exclude)
    if include is not None:
        if key is None:
            iterable = (x for x in iterable if x in include)
        else:
            iterable = (x for x in iterable if key(x) in include)
    if exclude is not None:
        if key is None:
            iterable = (x for x in iterable if x not in exclude)
        else:
            iterable = (x for x in iterable if key(x) not in exclude)
    return iterable


##


@overload
def groupby_lists(
    iterable: Iterable[_T], /, *, key: None = None
) -> Iterator[tuple[_T, list[_T]]]: ...
@overload
def groupby_lists(
    iterable: Iterable[_T], /, *, key: Callable[[_T], _U]
) -> Iterator[tuple[_U, list[_T]]]: ...
def groupby_lists(
    iterable: Iterable[_T], /, *, key: Callable[[_T], _U] | None = None
) -> Iterator[tuple[_T, list[_T]]] | Iterator[tuple[_U, list[_T]]]:
    """Yield consecutive keys and groups (as lists)."""
    if key is None:
        for k, group in groupby(iterable):
            yield k, list(group)
    else:
        for k, group in groupby(iterable, key=key):
            yield k, list(group)


##


def hashable_to_iterable(obj: _THashable | None, /) -> tuple[_THashable, ...] | None:
    """Lift a hashable singleton to an iterable of hashables."""
    return None if obj is None else (obj,)


##


def is_iterable(obj: Any, /) -> TypeGuard[Iterable[Any]]:
    """Check if an object is iterable."""
    try:
        iter(obj)
    except TypeError:
        return False
    return True


##


def is_iterable_not_enum(obj: Any, /) -> TypeGuard[Iterable[Any]]:
    """Check if an object is iterable, but not an Enum."""
    return is_iterable(obj) and not (isinstance(obj, type) and issubclass(obj, Enum))


##


def is_iterable_not_str(obj: Any, /) -> TypeGuard[Iterable[Any]]:
    """Check if an object is iterable, but not a string."""
    return is_iterable(obj) and not isinstance(obj, str)


##


def merge_str_mappings(
    *mappings: StrMapping, case_sensitive: bool = True
) -> StrMapping:
    """Merge a set of string mappings."""
    return reduce(
        partial(_merge_str_mappings_one, case_sensitive=case_sensitive), mappings, {}
    )


def _merge_str_mappings_one(
    acc: StrMapping, el: StrMapping, /, *, case_sensitive: bool = True
) -> StrMapping:
    out = dict(acc)
    if case_sensitive:
        return out | dict(el)
    try:
        check_unique_modulo_case(el)
    except _CheckUniqueModuloCaseDuplicateLowerCaseStringsError as error:
        raise MergeStrMappingsError(mapping=el, counts=error.counts) from None
    for key_add, value in el.items():
        try:
            key_del = one_str(out, key_add, case_sensitive=False)
        except _OneStrEmptyError:
            pass
        else:
            del out[key_del]
        out[key_add] = value
    return out


@dataclass(kw_only=True, slots=True)
class MergeStrMappingsError(Exception):
    mapping: StrMapping
    counts: Mapping[str, int]

    @override
    def __str__(self) -> str:
        return f"Mapping {get_repr(self.mapping)} keys must not contain duplicates (modulo case); got {get_repr(self.counts)}"


##


def one(iterable: Iterable[_T], /) -> _T:
    """Return the unique value in an iterable."""
    it = iter(iterable)
    try:
        first = next(it)
    except StopIteration:
        raise OneEmptyError(iterable=iterable) from None
    try:
        second = next(it)
    except StopIteration:
        return first
    raise OneNonUniqueError(iterable=iterable, first=first, second=second)


@dataclass(kw_only=True, slots=True)
class OneError(Exception, Generic[_T]):
    iterable: Iterable[_T]


@dataclass(kw_only=True, slots=True)
class OneEmptyError(OneError[_T]):
    @override
    def __str__(self) -> str:
        return f"Iterable {get_repr(self.iterable)} must not be empty"


@dataclass(kw_only=True, slots=True)
class OneNonUniqueError(OneError[_T]):
    first: _T
    second: _T

    @override
    def __str__(self) -> str:
        return f"Iterable {get_repr(self.iterable)} must contain exactly one item; got {self.first}, {self.second} and perhaps more"


##


def one_modal_value(iterable: Iterable[_T], /, *, min_frac: float = 0.5) -> _T:
    """Return the unique modal value in an iterable."""
    counts = Counter(iterable)
    fracs = {k: v / counts.total() for k, v in counts.items()}
    enoughs = {k for k, v in fracs.items() if v >= min_frac}
    try:
        return one(enoughs)
    except OneEmptyError as error:
        raise _OneModalValueEmptyError(iterable=error.iterable, fracs=fracs) from None
    except OneNonUniqueError as error:
        raise _OneModalValueNonUniqueError(
            iterable=error.iterable, fracs=fracs, first=error.first, second=error.second
        ) from None


@dataclass(kw_only=True, slots=True)
class OneModalValueError(Exception, Generic[_T]):
    iterable: Iterable[_T]
    fracs: dict[_T, float]


@dataclass(kw_only=True, slots=True)
class _OneModalValueEmptyError(OneModalValueError[_T]):
    @override
    def __str__(self) -> str:
        return f"Iterable {get_repr(self.iterable)} with fractions {get_repr(self.fracs)} must have a modal value"


@dataclass(kw_only=True, slots=True)
class _OneModalValueNonUniqueError(OneModalValueError[_T]):
    first: _T
    second: _T

    @override
    def __str__(self) -> str:
        return f"Iterable {get_repr(self.iterable)} with fractions {get_repr(self.fracs)} must contain exactly one modal value; got {self.first}, {self.second} and perhaps more"


##


def one_str(
    iterable: Iterable[str], text: str, /, *, case_sensitive: bool = True
) -> str:
    """Find the unique string in an iterable."""
    as_list = list(iterable)
    if case_sensitive:
        it = (t for t in as_list if t == text)
    else:
        it = (t for t in as_list if t.lower() == text.lower())
    try:
        return one(it)
    except OneEmptyError:
        raise _OneStrEmptyError(
            iterable=as_list, text=text, case_sensitive=case_sensitive
        ) from None
    except OneNonUniqueError as error:
        raise _OneStrNonUniqueError(
            iterable=as_list,
            text=text,
            case_sensitive=case_sensitive,
            first=error.first,
            second=error.second,
        ) from None


@dataclass(kw_only=True, slots=True)
class OneStrError(Exception):
    iterable: Iterable[str]
    text: str
    case_sensitive: bool = True


@dataclass(kw_only=True, slots=True)
class _OneStrEmptyError(OneStrError):
    @override
    def __str__(self) -> str:
        desc = f"Iterable {get_repr(self.iterable)} does not contain {self.text!r}"
        if not self.case_sensitive:
            desc += " (modulo case)"
        return desc


@dataclass(kw_only=True, slots=True)
class _OneStrNonUniqueError(OneStrError):
    first: str
    second: str

    @override
    def __str__(self) -> str:
        desc = f"Iterable {get_repr(self.iterable)} must contain {self.text!r} exactly once"
        match self.case_sensitive:
            case True:
                return f"{desc}; got at least 2 instances"
            case False:
                return f"{desc} (modulo case); got {self.first!r}, {self.second!r} and perhaps more"
            case _ as never:
                assert_never(never)


def pairwise_tail(iterable: Iterable[_T], /) -> Iterator[tuple[_T, _T | Sentinel]]:
    """Return pairwise elements, with the last paired with the sentinel."""
    return pairwise(chain(iterable, [sentinel]))


def product_dicts(mapping: Mapping[_K, Iterable[_V]], /) -> Iterator[Mapping[_K, _V]]:
    """Return the cartesian product of the values in a mapping, as mappings."""
    keys = list(mapping)
    for values in product(*mapping.values()):
        yield cast(Mapping[_K, _V], dict(zip(keys, values, strict=True)))


def resolve_include_and_exclude(
    *,
    include: MaybeIterable[_T] | None = None,
    exclude: MaybeIterable[_T] | None = None,
) -> tuple[set[_T] | None, set[_T] | None]:
    """Resolve an inclusion/exclusion pair."""
    include_use = include if include is None else set(always_iterable(include))
    exclude_use = exclude if exclude is None else set(always_iterable(exclude))
    if (
        (include_use is not None)
        and (exclude_use is not None)
        and (len(include_use & exclude_use) >= 1)
    ):
        raise ResolveIncludeAndExcludeError(include=include_use, exclude=exclude_use)
    return include_use, exclude_use


@dataclass(kw_only=True, slots=True)
class ResolveIncludeAndExcludeError(Exception, Generic[_T]):
    include: Iterable[_T]
    exclude: Iterable[_T]

    @override
    def __str__(self) -> str:
        include = list(self.include)
        exclude = list(self.exclude)
        overlap = set(include) & set(exclude)
        return f"Iterables {get_repr(include)} and {get_repr(exclude)} must not overlap; got {get_repr(overlap)}"


def sort_iterable(iterable: Iterable[_T], /) -> list[_T]:
    """Sort an iterable across types."""
    return sorted(iterable, key=cmp_to_key(_sort_iterable_cmp))


def _sort_iterable_cmp(x: Any, y: Any, /) -> Literal[-1, 0, 1]:
    """Compare two quantities."""
    if type(x) is not type(y):
        x_qualname = type(x).__qualname__
        y_qualname = type(y).__qualname__
        if x_qualname < y_qualname:
            return -1
        if x_qualname > y_qualname:
            return 1
        raise ImpossibleCaseError(  # pragma: no cover
            case=[f"{x_qualname=}", f"{y_qualname=}"]
        )

    # singletons
    if x is None:
        y = cast(NoneType, y)
        return 0
    if isinstance(x, dt.datetime):
        y = cast(dt.datetime, y)
        return _sort_iterable_cmp_datetimes(x, y)
    if isinstance(x, float):
        y = cast(float, y)
        return _sort_iterable_cmp_floats(x, y)
    if isinstance(x, str):  # else Sequence
        y = cast(str, y)
        return cast(Literal[-1, 0, 1], (x > y) - (x < y))

    # collections
    if isinstance(x, Sized):
        y = cast(Sized, y)
        if (result := _sort_iterable_cmp(len(x), len(y))) != 0:
            return result
    if isinstance(x, Mapping):
        y = cast(Mapping[Any, Any], y)
        return _sort_iterable_cmp(x.items(), y.items())
    if isinstance(x, AbstractSet):
        y = cast(AbstractSet[Any], y)
        return _sort_iterable_cmp(sort_iterable(x), sort_iterable(y))
    if isinstance(x, Sequence):
        y = cast(Sequence[Any], y)
        it: Iterable[Literal[-1, 0, 1]] = (
            _sort_iterable_cmp(x_i, y_i) for x_i, y_i in zip(x, y, strict=True)
        )
        with suppress(StopIteration):
            return next(r for r in it if r != 0)

    try:
        return cast(Literal[-1, 0, 1], (x > y) - (x < y))
    except TypeError:
        raise SortIterableError(x=x, y=y) from None


@dataclass(kw_only=True, slots=True)
class SortIterableError(Exception):
    x: Any
    y: Any

    @override
    def __str__(self) -> str:
        return f"Unable to sort {get_repr(self.x)} and {get_repr(self.y)}"


def _sort_iterable_cmp_datetimes(
    x: dt.datetime, y: dt.datetime, /
) -> Literal[-1, 0, 1]:
    """Compare two datetimes."""
    if (x.tzinfo is None) and (y.tzinfo is None):
        return cast(Literal[-1, 0, 1], (x > y) - (x < y))
    if (x.tzinfo is None) and (y.tzinfo is not None):
        return -1
    if (x.tzinfo is not None) and (y.tzinfo is None):
        return 1
    if (x.tzinfo is not None) and (y.tzinfo is not None):
        x_utc = x.astimezone(tz=UTC)
        y_utc = y.astimezone(tz=UTC)
        result = cast(Literal[-1, 0, 1], (x_utc > y_utc) - (x_utc < y_utc))
        if result != 0:
            return result
        x_time_zone = ensure_not_none(x.tzinfo.tzname(x))
        y_time_zone = ensure_not_none(y.tzinfo.tzname(y))
        return cast(
            Literal[-1, 0, 1], (x_time_zone > y_time_zone) - (x_time_zone < y_time_zone)
        )
    raise ImpossibleCaseError(case=[f"{x=}", f"{y=}"])  # pragma: no cover


def _sort_iterable_cmp_floats(x: float, y: float, /) -> Literal[-1, 0, 1]:
    """Compare two floats."""
    if isnan(x) and isnan(y):
        return 0
    if isnan(x) and (not isnan(y)):
        return 1
    if (not isnan(x)) and isnan(y):
        return -1
    if (not isnan(x)) and (not isnan(y)):
        return cast(Literal[-1, 0, 1], (x > y) - (x < y))
    raise ImpossibleCaseError(case=[f"{x=}", f"{y=}"])  # pragma: no cover


def take(n: int, iterable: Iterable[_T], /) -> Sequence[_T]:
    """Return first n items of the iterable as a list."""
    return list(islice(iterable, n))


@overload
def transpose(iterable: Iterable[tuple[_T1]], /) -> tuple[tuple[_T1, ...]]: ...
@overload
def transpose(
    iterable: Iterable[tuple[_T1, _T2]], /
) -> tuple[tuple[_T1, ...], tuple[_T2, ...]]: ...
@overload
def transpose(
    iterable: Iterable[tuple[_T1, _T2, _T3]], /
) -> tuple[tuple[_T1, ...], tuple[_T2, ...], tuple[_T3, ...]]: ...
@overload
def transpose(
    iterable: Iterable[tuple[_T1, _T2, _T3, _T4]], /
) -> tuple[tuple[_T1, ...], tuple[_T2, ...], tuple[_T3, ...], tuple[_T4, ...]]: ...
@overload
def transpose(
    iterable: Iterable[tuple[_T1, _T2, _T3, _T4, _T5]], /
) -> tuple[
    tuple[_T1, ...], tuple[_T2, ...], tuple[_T3, ...], tuple[_T4, ...], tuple[_T5, ...]
]: ...
def transpose(iterable: Iterable[tuple[Any, ...]]) -> tuple[tuple[Any, ...], ...]:
    """Typed verison of `transpose`."""
    return tuple(zip(*iterable, strict=True))


__all__ = [
    "ApplyBijectionError",
    "CheckBijectionError",
    "CheckDuplicatesError",
    "CheckIterablesEqualError",
    "CheckLengthsEqualError",
    "CheckMappingsEqualError",
    "CheckSetsEqualError",
    "CheckSubMappingError",
    "CheckSubSetError",
    "CheckSuperMappingError",
    "CheckSuperSetError",
    "CheckUniqueModuloCaseError",
    "EnsureIterableError",
    "EnsureIterableNotStrError",
    "MergeStrMappingsError",
    "OneEmptyError",
    "OneError",
    "OneModalValueError",
    "OneNonUniqueError",
    "OneStrError",
    "ResolveIncludeAndExcludeError",
    "SortIterableError",
    "always_iterable",
    "apply_bijection",
    "apply_to_tuple",
    "apply_to_varargs",
    "chain_nullable",
    "check_bijection",
    "check_duplicates",
    "check_iterables_equal",
    "check_lengths_equal",
    "check_mappings_equal",
    "check_sets_equal",
    "check_submapping",
    "check_subset",
    "check_supermapping",
    "check_superset",
    "check_unique_modulo_case",
    "chunked",
    "ensure_hashables",
    "ensure_iterable",
    "ensure_iterable_not_str",
    "expanding_window",
    "filter_include_and_exclude",
    "groupby_lists",
    "hashable_to_iterable",
    "is_iterable",
    "is_iterable_not_enum",
    "is_iterable_not_str",
    "merge_str_mappings",
    "one",
    "one_modal_value",
    "one_str",
    "pairwise_tail",
    "product_dicts",
    "resolve_include_and_exclude",
    "sort_iterable",
    "take",
    "transpose",
]
