from typing import Any, Awaitable, Callable, Dict

from aiomatter.state.fsm_context import FSMContext


class StateMiddleware:
    """
    Middleware for injecting FSMContext into handlers.
    """

    def __init__(self) -> None:
        self._contexts: Dict[str, FSMContext] = {}

    async def __call__(
        self,
        handler: Callable[..., Awaitable[Any]],
        event: Any,
        data: Dict[str, Any],
    ) -> Any:
        user_id = str(event.get("user_id", "default"))
        context = self._contexts.setdefault(user_id, FSMContext())

        data["fsm_context"] = context
        return await handler(event, data)
