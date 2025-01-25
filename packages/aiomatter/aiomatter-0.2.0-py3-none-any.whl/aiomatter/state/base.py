from typing import Iterator, Type


class State:
    """
    Represents a single state in a finite-state machine.
    """

    def __init__(
        self, state: str | None = None, group_name: str | None = None
    ) -> None:
        self._state = state
        self._group_name = group_name
        self._group: Type["StatesGroup"] | None = None

    @property
    def group(self) -> Type["StatesGroup"]:
        if not self._group:
            raise RuntimeError(f"State '{self._state}' is not part of any group.")
        return self._group

    @property
    def state(self) -> str:
        group = self._group_name or (
            self._group.__full_group_name__ if self._group else "@"
        )
        return f"{group}:{self._state}"

    def set_parent(self, group: Type["StatesGroup"]) -> None:
        if not issubclass(group, StatesGroup):
            raise ValueError("Parent group must be a subclass of StatesGroup")
        self._group = group

    def __set_name__(self, owner: Type["StatesGroup"], name: str) -> None:
        if self._state is None:
            self._state = name
        self.set_parent(owner)

    def __str__(self) -> str:
        return f"<State '{self.state}'>"

    def __repr__(self) -> str:
        return self.__str__()


class StatesGroupMeta(type):
    """
    Metaclass for StatesGroup to manage states and hierarchy.
    """

    def __new__(mcs, name, bases, namespace, **kwargs):
        cls = super().__new__(mcs, name, bases, namespace)

        cls.__states__ = {
            key: value
            for key, value in namespace.items()
            if isinstance(value, State)
        }
        for state_name, state in cls.__states__.items():
            state._group_name = name

        return cls

    @property
    def __full_group_name__(cls) -> str:
        return cls.__name__

    def __iter__(cls) -> Iterator[State]:
        return iter(cls.__states__.values())


class StatesGroup(metaclass=StatesGroupMeta):
    """
    Represents a group of related states in a finite-state machine.
    """
