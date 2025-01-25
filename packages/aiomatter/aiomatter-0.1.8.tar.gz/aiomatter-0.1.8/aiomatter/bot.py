import asyncio
from logging import Logger
from typing import Any, Callable, Coroutine, Dict, List, Union

from .driver import MattermostDriver
from .events import EventType
from .plugin import Plugin
from .settings import Settings
from .aiologger import setup_logger
from .state.fsm_context import FSMContext

EventHandler = Callable[
    [Dict[str, Any], FSMContext], Coroutine[Any, Any, None]
]


class Bot:
    def __init__(
        self,
        plugins: List[Plugin],
        settings: Settings,
        logger: Logger | None = None,
    ):
        """Инициализация бота с подключенными плагинами и настройками."""
        self.plugins = plugins
        self.settings = settings
        self.logger = logger or setup_logger()
        self.driver = MattermostDriver(
            settings.full_api_url, settings.BOT_TOKEN, logger=self.logger
        )
        self.handlers: Dict[EventType, List[EventHandler]] = (
            self._register_plugins()
        )
        self.fsm_contexts: Dict[str, FSMContext] = (
            {}
        )  # FSMContext для каждого пользователя

    def _register_plugins(self) -> Dict[EventType, List[EventHandler]]:
        """Регистрирует плагины и передает им драйвер."""
        handlers: Dict[EventType, List[EventHandler]] = {}
        for plugin in self.plugins:
            plugin.setup_plugin(self.driver, self.logger)
            for event_type, funcs in plugin.get_handlers().items():
                handlers.setdefault(event_type, []).extend(funcs)
        return handlers

    async def _initialize(self) -> None:
        await self.driver.initialize()

    def _get_fsm_context(self, user_id: str) -> FSMContext:
        """Получает или создает FSMContext для пользователя."""
        if user_id not in self.fsm_contexts:
            self.fsm_contexts[user_id] = FSMContext()
        return self.fsm_contexts[user_id]

    async def handle_event(self, event: Union[Dict[str, Any], str]):
        """Обрабатывает событие и вызывает соответствующие хэндлеры."""
        try:
            # Преобразуем событие в словарь, если оно передано как строка
            if isinstance(event, str):
                import json

                try:
                    event = json.loads(event)
                except json.JSONDecodeError:
                    self.logger.error(
                        "Ошибка: событие не удалось декодировать из строки."
                    )
                    return

            # Проверяем, что event — это словарь
            if not isinstance(event, dict):
                self.logger.error("Ошибка: событие имеет некорректный формат.")
                return

            event_type = event.get('event')
            matching_handlers = self.handlers.get(event_type, [])

            if EventType.ANY in self.handlers:
                matching_handlers.extend(self.handlers[EventType.ANY])

            # Обрабатываем поле "post" внутри события
            post_data = event.get("data", {}).get("post")
            if isinstance(post_data, str):
                import json

                try:
                    post_data = json.loads(post_data)
                except json.JSONDecodeError:
                    self.logger.error(
                        "Ошибка: не удалось декодировать поле 'post'."
                    )
                    post_data = {}

            # Проверяем, что post_data является словарем
            if not isinstance(post_data, dict):
                post_data = {}

            user_id = post_data.get("user_id", "default")
            fsm_context = self._get_fsm_context(user_id)

            for handler in matching_handlers:
                await handler(event, fsm_context)
        except Exception as e:
            self.logger.exception(f"Ошибка при обработке события:\n{e}")

    async def _async_run(self):
        """Асинхронный метод запуска бота."""
        await self._initialize()

        ws_url = f"{self.settings.full_api_url}/websocket"
        self.logger.info(f"Бот подключается к WebSocket: {ws_url}")

        while True:
            try:
                await self.driver.connect_websocket(ws_url, self.handle_event)
            except Exception as e:
                self.logger.error(
                    f"Ошибка WebSocket: {e}. Переподключение через 5 секунд..."
                )
                await asyncio.sleep(5)

    def run(self):
        """Синхронный метод запуска бота."""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(self._async_run())
        finally:
            loop.close()

    async def _async_stop(self):
        """Асинхронная остановка бота."""
        await self.driver.close()

    def stop(self):
        """Синхронный метод для остановки бота."""
        asyncio.run(self._async_stop())
