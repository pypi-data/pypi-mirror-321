import json
from functools import wraps
from typing import Callable, Dict, Any, Coroutine, Type
from inspect import signature
from aiomatter.events import EventType
from aiomatter.state.base import State, StatesGroup
from aiomatter.state.fsm_context import FSMContext
from aiomatter.schemas.post_events import (
    PostEvent,
    EditEvent,
    DeleteEvent,
)

from aiomatter.aiologger import logger


EVENT_MAPPING = {
    EventType.POSTED: PostEvent,
    EventType.POST_EDITED: EditEvent,
    EventType.POST_DELETED: DeleteEvent,
    EventType.ANY: lambda event: event,
}


def listen(
    event_type: EventType,
    required_state: State | None = None,
    required_group: Type[StatesGroup] | None = None,
    ignore_bots: bool = True,
):
    """
    Декоратор для регистрации обработчиков событий
    с поддержкой фильтрации по состоянию и группе состояний.

    :param event_type: Тип события, на которое реагирует обработчик.
    :param required_state: Требуемое состояние пользователя для вызова.
    :param required_group: Требуемая группа состояний для вызова обработчика.
    :param ignore_bots: Игнорировать сообщения от ботов.
    """

    def decorator(func: Callable[..., Coroutine[Any, Any, None]]):
        @wraps(func)
        async def wrapper(
            plugin,
            event: Dict[str, Any],
            fsm_context: FSMContext | None = None,
        ):
            if event.get("event") != event_type:
                return

            post_data = event.get("data", {}).get("post")
            if isinstance(post_data, str):
                try:
                    post_data = json.loads(post_data)
                    event["data"]["post"] = post_data
                except json.JSONDecodeError:
                    logger.error("Failed to decode 'post' field.")
                    return

            sender = post_data.get("sender_name", None)
            props = post_data.get("props", {})
            from_bot = props.get("from_bot", "false")

            if (from_bot == "true" or sender == "System") and ignore_bots:
                return

            current_state = fsm_context.get_state() if fsm_context else None
            if required_group:
                if not current_state:
                    return
                if current_state.group != required_group:
                    return
            if required_state and current_state != required_state:
                return

            event_class = EVENT_MAPPING.get(event_type)
            if event_class and callable(event_class):
                try:
                    event = event_class(**event)
                except Exception as e:
                    logger.error(f"Failed to map event to class {event_class}: {e}")
                    return
            func_params = list(signature(func).parameters.keys())
            if "fsm_context" in func_params:
                await func(plugin, event, fsm_context)
            else:
                await func(plugin, event)
        wrapper.event_type = event_type
        return wrapper

    return decorator
