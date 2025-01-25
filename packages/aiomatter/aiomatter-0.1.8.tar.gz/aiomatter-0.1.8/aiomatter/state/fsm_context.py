from typing import Any, Dict

from aiomatter.state.base import State


class FSMContext:
    """
    Context for managing state and data for a specific user or entity.
    """

    def __init__(self) -> None:
        self._state: State | None = None
        self._data: Dict[str, Any] = {}

    def set_state(self, state: State | None) -> None:
        self._state = state

    def get_state(self) -> State | None:
        return self._state

    def set_data(self, key: str, value: Any) -> None:
        self._data[key] = value

    def get_data(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

    def get_all_data(self) -> Dict[str, Any]:
        return self._data

    def reset_state(self) -> None:
        self._state = None

    def reset_data(self) -> None:
        self._data.clear()
