from typing import Any, Callable, TypeVar, cast, get_type_hints
from typing_extensions import override
from pydit.core.register import injectable
from pydit.core.resolver import DependencyResolver
from pydit.exceptions.missing_property_type import MissingPropertyTypeException
from pydit.types.dependency_property import DependencyPropertyType


R = TypeVar("R")

GetInstanceFnType = Callable[[type[R]], R]


class PyDit:
    def __init__(self):
        self._dep_resolver = DependencyResolver()

    def add_dependency(self, value: Any, token: str | None = None):
        injectable(value, token=token)

    def inject(self, *, token: str | None = None):
        def decorator(func: Callable[..., R]) -> DependencyPropertyType[R]:
            return self.DependencyProperty(
                func=func,
                token=token,
                dep_resolver=self._dep_resolver,
                get_value_fn=self._get_value,
            )

        return decorator

    class DependencyProperty(DependencyPropertyType[R]):
        _inject_type: R
        _token: str | None = None
        _dep_resolver: DependencyResolver
        _get_value_fn: GetInstanceFnType[R]
        _value: Any = None

        def __init__(
            self,
            *,
            func: Callable[..., R],
            token: str | None = None,
            dep_resolver: DependencyResolver,
            get_value_fn: GetInstanceFnType[R]
        ):
            hints = get_type_hints(func)

            self._inject_type = cast(R, hints.get("return"))
            self._token = token
            self._dep_resolver = dep_resolver
            self._get_value_fn = get_value_fn

            if self._inject_type is None:
                raise MissingPropertyTypeException

        @override
        def __get__(self, _instance: Any, _obj: Any = None) -> R:
            if self._value is not None:
                return self._value

            dependency = self._dep_resolver.resolve_dependencies(
                self._inject_type, self._token
            )

            is_callable = callable(dependency.value)

            if not is_callable:
                self._value = dependency.value

                return dependency.value

            instance = self._get_value_fn(dependency.value)

            self._value = instance

            return instance

    def _get_value(self, dependency: type[R]) -> R:
        """
        This function will resolve __init__ signature in the future
        """
        return dependency()
