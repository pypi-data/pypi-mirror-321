from __future__ import annotations

from dataclasses import MISSING, dataclass, field, fields, replace
from pathlib import Path
from typing import TYPE_CHECKING, Any, Generic, Literal, TypeVar, overload

from typing_extensions import override

from utilities.errors import ImpossibleCaseError
from utilities.functions import (
    get_class_name,
    is_dataclass_class,
    is_dataclass_instance,
)
from utilities.iterables import _OneStrEmptyError, _OneStrNonUniqueError, one_str
from utilities.operator import is_equal
from utilities.reprlib import get_repr
from utilities.sentinel import Sentinel, sentinel
from utilities.types import Dataclass, StrMapping
from utilities.typing import get_type_hints

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable, Iterator, Mapping


_T = TypeVar("_T")
_U = TypeVar("_U")
_TDataclass = TypeVar("_TDataclass", bound=Dataclass)


##


def asdict_without_defaults(
    obj: Dataclass,
    /,
    *,
    globalns: StrMapping | None = None,
    localns: StrMapping | None = None,
    rel_tol: float | None = None,
    abs_tol: float | None = None,
    extra: Mapping[type[_T], Callable[[_T, _T], bool]] | None = None,
    final: Callable[[type[Dataclass], StrMapping], StrMapping] | None = None,
    recursive: bool = False,
) -> StrMapping:
    """Cast a dataclass as a dictionary, without its defaults."""
    out: dict[str, Any] = {}
    for fld in yield_fields(obj, globalns=globalns, localns=localns):
        if not fld.equals_default(rel_tol=rel_tol, abs_tol=abs_tol, extra=extra):
            if recursive and is_dataclass_instance(fld.value):
                value_as_dict = asdict_without_defaults(
                    fld.value,
                    globalns=globalns,
                    localns=localns,
                    rel_tol=rel_tol,
                    abs_tol=abs_tol,
                    extra=extra,
                    final=final,
                    recursive=recursive,
                )
            else:
                value_as_dict = fld.value
            out[fld.name] = value_as_dict
    return out if final is None else final(type(obj), out)


##


def mapping_to_dataclass(
    cls: type[_TDataclass],
    mapping: StrMapping,
    /,
    *,
    globalns: StrMapping | None = None,
    localns: StrMapping | None = None,
    case_sensitive: bool = True,
    post: Callable[[_YieldFieldsClass[Any], Any], Any] | None = None,
) -> _TDataclass:
    """Construct a dataclass from a mapping."""
    fields = yield_fields(cls, globalns=globalns, localns=localns)
    mapping_use = {
        f.name: _mapping_to_dataclass_one(
            f, mapping, case_sensitive=case_sensitive, post=post
        )
        for f in fields
    }
    return cls(**mapping_use)


def _mapping_to_dataclass_one(
    field: _YieldFieldsClass[Any],
    mapping: StrMapping,
    /,
    *,
    case_sensitive: bool = True,
    post: Callable[[_YieldFieldsClass[Any], Any], Any] | None = None,
) -> Any:
    try:
        key = one_str(mapping, field.name, case_sensitive=case_sensitive)
    except _OneStrEmptyError:
        raise _MappingToDataclassEmptyError(
            mapping=mapping, field=field.name, case_sensitive=case_sensitive
        ) from None
    except _OneStrNonUniqueError as error:
        raise _MappingToDataclassCaseInsensitiveNonUniqueError(
            mapping=mapping, field=field.name, first=error.first, second=error.second
        ) from None
    value = mapping[key]
    if post is not None:
        value = post(field, value)
    return value


@dataclass(kw_only=True, slots=True)
class MappingToDataclassError(Exception):
    mapping: StrMapping
    field: str


@dataclass(kw_only=True, slots=True)
class _MappingToDataclassEmptyError(MappingToDataclassError):
    case_sensitive: bool = True

    @override
    def __str__(self) -> str:
        desc = f"Mapping {get_repr(self.mapping)} does not contain {self.field!r}"
        if not self.case_sensitive:
            desc += " (modulo case)"
        return desc


@dataclass(kw_only=True, slots=True)
class _MappingToDataclassCaseInsensitiveNonUniqueError(MappingToDataclassError):
    first: str
    second: str

    @override
    def __str__(self) -> str:
        return f"Mapping {get_repr(self.mapping)} must contain {self.field!r} exactly once (modulo case); got {self.first!r}, {self.second!r} and perhaps more"


##


@overload
def replace_non_sentinel(
    obj: Any, /, *, in_place: Literal[True], **kwargs: Any
) -> None: ...
@overload
def replace_non_sentinel(
    obj: _TDataclass, /, *, in_place: Literal[False] = False, **kwargs: Any
) -> _TDataclass: ...
@overload
def replace_non_sentinel(
    obj: _TDataclass, /, *, in_place: bool = False, **kwargs: Any
) -> _TDataclass | None: ...
def replace_non_sentinel(
    obj: _TDataclass, /, *, in_place: bool = False, **kwargs: Any
) -> _TDataclass | None:
    """Replace attributes on a dataclass, filtering out sentinel values."""
    if in_place:
        for k, v in kwargs.items():
            if not isinstance(v, Sentinel):
                setattr(obj, k, v)
        return None
    return replace(
        obj, **{k: v for k, v in kwargs.items() if not isinstance(v, Sentinel)}
    )


##


def repr_without_defaults(
    obj: Dataclass,
    /,
    *,
    ignore: Iterable[str] | None = None,
    globalns: StrMapping | None = None,
    localns: StrMapping | None = None,
    rel_tol: float | None = None,
    abs_tol: float | None = None,
    extra: Mapping[type[_T], Callable[[_T, _T], bool]] | None = None,
    recursive: bool = False,
) -> str:
    """Repr a dataclass, without its defaults."""
    ignore_use: set[str] = set() if ignore is None else set(ignore)
    out: dict[str, str] = {}
    for fld in yield_fields(obj, globalns=globalns, localns=localns):
        if (
            (fld.name not in ignore_use)
            and fld.repr
            and not fld.equals_default(rel_tol=rel_tol, abs_tol=abs_tol, extra=extra)
        ):
            if recursive and is_dataclass_instance(fld.value):
                repr_as_dict = repr_without_defaults(
                    fld.value,
                    ignore=ignore,
                    globalns=globalns,
                    localns=localns,
                    rel_tol=rel_tol,
                    abs_tol=abs_tol,
                    extra=extra,
                    recursive=recursive,
                )
            else:
                repr_as_dict = repr(fld.value)
            out[fld.name] = repr_as_dict
    cls = get_class_name(obj)
    joined = ", ".join(f"{k}={v}" for k, v in out.items())
    return f"{cls}({joined})"


##


@overload
def yield_fields(
    obj: Dataclass,
    /,
    *,
    globalns: StrMapping | None = ...,
    localns: StrMapping | None = ...,
) -> Iterator[_YieldFieldsInstance[Any]]: ...
@overload
def yield_fields(
    obj: type[Dataclass],
    /,
    *,
    globalns: StrMapping | None = ...,
    localns: StrMapping | None = ...,
) -> Iterator[_YieldFieldsClass[Any]]: ...
def yield_fields(
    obj: Dataclass | type[Dataclass],
    /,
    *,
    globalns: StrMapping | None = None,
    localns: StrMapping | None = None,
) -> Iterator[_YieldFieldsInstance[Any]] | Iterator[_YieldFieldsClass[Any]]:
    """Yield the fields of a dataclass."""
    if is_dataclass_instance(obj):
        for field in yield_fields(type(obj), globalns=globalns, localns=localns):
            yield _YieldFieldsInstance(
                name=field.name,
                value=getattr(obj, field.name),
                type_=field.type_,
                default=field.default,
                default_factory=field.default_factory,
                init=field.init,
                repr=field.repr,
                hash_=field.hash_,
                compare=field.compare,
                metadata=field.metadata,
                kw_only=field.kw_only,
            )
    elif is_dataclass_class(obj):
        hints = get_type_hints(
            obj,
            globalns=globalns,
            localns={"Path": Path} | ({} if localns is None else dict(localns)),
        )
        for field in fields(obj):
            if isinstance(field.type, type):
                type_ = field.type
            else:
                type_ = hints.get(field.name, field.type)
            yield (
                _YieldFieldsClass(
                    name=field.name,
                    type_=type_,
                    default=sentinel if field.default is MISSING else field.default,
                    default_factory=sentinel
                    if field.default_factory is MISSING
                    else field.default_factory,
                    init=field.init,
                    repr=field.repr,
                    hash_=field.hash,
                    compare=field.compare,
                    metadata=dict(field.metadata),
                    kw_only=sentinel if field.kw_only is MISSING else field.kw_only,
                )
            )
    else:
        raise YieldFieldsError(obj=obj)


@dataclass(kw_only=True, slots=True)
class _YieldFieldsInstance(Generic[_T]):
    name: str
    value: _T
    type_: Any
    default: _T | Sentinel = sentinel
    default_factory: Callable[[], _T] | Sentinel = sentinel
    repr: bool = True
    hash_: bool | None = None
    init: bool = True
    compare: bool = True
    metadata: StrMapping = field(default_factory=dict)
    kw_only: bool | Sentinel = sentinel

    def equals_default(
        self,
        *,
        rel_tol: float | None = None,
        abs_tol: float | None = None,
        extra: Mapping[type[_U], Callable[[_U, _U], bool]] | None = None,
    ) -> bool:
        """Check if the field value equals its default."""
        if isinstance(self.default, Sentinel) and isinstance(
            self.default_factory, Sentinel
        ):
            return False
        if (not isinstance(self.default, Sentinel)) and isinstance(
            self.default_factory, Sentinel
        ):
            expected = self.default
        elif isinstance(self.default, Sentinel) and (
            not isinstance(self.default_factory, Sentinel)
        ):
            expected = self.default_factory()
        else:  # pragma: no cover
            raise ImpossibleCaseError(
                case=[f"{self.default=}", f"{self.default_factory=}"]
            )
        return is_equal(
            self.value, expected, rel_tol=rel_tol, abs_tol=abs_tol, extra=extra
        )


@dataclass(kw_only=True, slots=True)
class _YieldFieldsClass(Generic[_T]):
    name: str
    type_: Any
    default: _T | Sentinel = sentinel
    default_factory: Callable[[], _T] | Sentinel = sentinel
    repr: bool = True
    hash_: bool | None = None
    init: bool = True
    compare: bool = True
    metadata: StrMapping = field(default_factory=dict)
    kw_only: bool | Sentinel = sentinel


@dataclass(kw_only=True, slots=True)
class YieldFieldsError(Exception):
    obj: Any

    @override
    def __str__(self) -> str:
        return f"Object must be a dataclass instance or class; got {self.obj}"


##

__all__ = [
    "MappingToDataclassError",
    "YieldFieldsError",
    "asdict_without_defaults",
    "mapping_to_dataclass",
    "replace_non_sentinel",
    "repr_without_defaults",
    "yield_fields",
]
