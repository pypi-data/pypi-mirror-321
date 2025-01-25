import json
from logging import Logger

import aiohttp
import websockets

from aiomatter.input.input_file import InputFile, InputFileGroup
from aiomatter.schemas.post_events import Post
from aiomatter.schemas.user import MattermostUser


class AsyncDriver:
    def __init__(self, base_url, token, logger: Logger):
        self.base_url = base_url
        self.token = token
        self.logger = logger
        self.session = None

    async def initialize(self):
        """Асинхронная инициализация сессии."""
        self.session = aiohttp.ClientSession(
            headers={"Authorization": f"Bearer {self.token}"}
        )

    async def send_request(
        self, endpoint, method='GET', data=None, files=None
    ):
        """Отправляет запрос к REST API."""
        url = f"{self.base_url}{endpoint}"
        headers = {"Authorization": f"Bearer {self.token}"}
        async with self.session.request(
            method, url, json=data, data=files, headers=headers
        ) as response:
            response.raise_for_status()
            return await response.json()

    async def connect_websocket(self, ws_url: str, on_message):
        """Устанавливает WebSocket-соединение и слушает события."""
        headers = {'Authorization': f'Bearer {self.token}'}
        try:
            async with websockets.connect(
                ws_url, additional_headers=headers
            ) as ws:
                self.logger.info("Успешно подключено к WebSocket.")
                async for message in ws:
                    try:
                        self.logger.debug(f"Получено сообщение: {message}")
                        await on_message(json.loads(message))
                    except Exception as e:
                        self.logger.error(
                            f"Ошибка при обработке сообщения: {e}"
                        )
        except websockets.exceptions.ConnectionClosed as e:
            self.logger.error(f"Соединение закрыто: {e}")
            raise e
        except Exception as e:
            self.logger.error(f"Ошибка WebSocket: {e}")
            raise e

    async def close(self):
        """Закрывает сессию для освобождения ресурсов."""
        await self.session.close()


class MattermostDriver(AsyncDriver):
    """Драйвер взаимодействия с Mattermost API на основе WebSocket."""

    async def send_message(self, channel_id, message, root_id=None):
        """Отправляет сообщение в указанный канал."""
        data = {"channel_id": channel_id, "message": message}

        if root_id is not None:
            data["root_id"] = root_id

        response = await self.send_request("/posts", method='POST', data=data)

        return Post(**response)

    async def edit_message(self, post_id, new_message):
        """Редактирует существующее сообщение по его ID."""
        data = {"message": new_message}
        response = await self.send_request(
            f"/posts/{post_id}/patch", method='PUT', data=data
        )

        return Post(**response)

    async def delete_message(self, post_id):
        """Удаляет сообщение по его ID."""
        await self.send_request(f"/posts/{post_id}", method='DELETE')

    async def _create_dm_channel(self, user_id):
        """Создает канал для личного сообщения с пользователем."""
        bot_info = await self.get_bot_info()
        data = [bot_info.id, user_id]
        response = await self.send_request(
            "/channels/direct", method='POST', data=data
        )
        return response["id"]

    async def direct_message(self, user_id, message):
        """Отправляет личное сообщение пользователю."""
        channel_id = await self._create_dm_channel(user_id)
        return await self.send_message(channel_id, message)

    async def get_user_by_name(self, username: str) -> MattermostUser:
        """Получает информацию о пользователе по его имени."""
        username = username.replace('@', '')
        response = await self.send_request(
            f"/users/username/{username}", method='GET'
        )
        return MattermostUser(**response)

    async def get_user_by_id(self, user_id) -> MattermostUser:
        """Получает информацию о пользователе по его ID."""
        response = await self.send_request(f"/users/{user_id}", method='GET')
        return MattermostUser(**response)

    async def get_bot_info(self) -> MattermostUser:
        """Возвращает информацию о боте."""
        response = await self.send_request(
            '/users/me',
            method='GET',
        )
        return MattermostUser(**response)

    async def send_attachment(
        self, channel_id: str, input_file: InputFile, caption: str = ""
    ):
        """
        Send an attachment to a Mattermost channel.

        :param channel_id: The ID of the channel to send the message to.
        :param input_file: An InputFile object representing the file to send.
        :param message: Optional message to accompany the file.
        """
        if input_file.is_uploaded():
            data = {
                "channel_id": channel_id,
                "message": caption,
                "file_ids": [input_file.file_id],
            }
            return await self.send_request("/posts", method="POST", data=data)
        files = (
            {"files": open(input_file.file, "rb")}
            if input_file.is_file_path()
            else {"files": input_file.file}
        )
        form_data = aiohttp.FormData()
        form_data.add_field("channel_id", channel_id)
        form_data.add_field("files", files["files"])

        async with self.session.post(
            f"{self.base_url}/files",
            data=form_data,
            headers={"Authorization": f"Bearer {self.token}"},
        ) as upload_response:
            if upload_response.status not in [200, 201]:
                raise ValueError(
                    f"File upload failed: {upload_response.status}"
                )
            upload_result = await upload_response.json()
        file_id = upload_result.get("file_infos", [{}])[0].get("id")
        if not file_id:
            raise ValueError("Failed to retrieve file ID after upload.")
        data = {
            "channel_id": channel_id,
            "message": caption,
            "file_ids": [file_id],
        }
        return await self.send_request("/posts", method="POST", data=data)

    async def send_attachments_group(
        self,
        channel_id: str,
        input_file_group: InputFileGroup,
        caption: str = "",
    ):
        """
        Send a group of attachments to a Mattermost channel.

        :param channel_id: The ID of the channel to send the message to.
        :param input_file_group: An InputFileGroup object containing the files to send.
        :param message: Optional message to accompany the files.
        """
        file_ids = input_file_group.get_uploaded_file_ids()

        for input_file in input_file_group.get_unuploaded_files():
            if input_file.is_file_path():
                with open(input_file.file, "rb") as file_data:
                    form_data = aiohttp.FormData()
                    form_data.add_field("channel_id", channel_id)
                    form_data.add_field("files", file_data)

                    async with self.session.post(
                        f"{self.base_url}/files",
                        data=form_data,
                        headers={"Authorization": f"Bearer {self.token}"},
                    ) as upload_response:
                        if upload_response.status not in [200, 201]:
                            raise ValueError(
                                f"File upload failed: {upload_response.status}"
                            )
                        upload_result = await upload_response.json()

                file_id = upload_result.get("file_infos", [{}])[0].get("id")
                if not file_id:
                    raise ValueError(
                        "Failed to retrieve file ID after upload."
                    )
                file_ids.append(file_id)
            elif isinstance(input_file.file, bytes):
                form_data = aiohttp.FormData()
                form_data.add_field("channel_id", channel_id)
                form_data.add_field("files", input_file.file)

                async with self.session.post(
                    f"{self.base_url}/files",
                    data=form_data,
                    headers={"Authorization": f"Bearer {self.token}"},
                ) as upload_response:
                    if upload_response.status not in [200, 201]:
                        raise ValueError(
                            f"File upload failed: {upload_response.status}"
                        )
                    upload_result = await upload_response.json()

                file_id = upload_result.get("file_infos", [{}])[0].get("id")
                if not file_id:
                    raise ValueError(
                        "Failed to retrieve file ID after upload."
                    )
                file_ids.append(file_id)
            else:
                raise ValueError("Unsupported file type for upload.")

        data = {
            "channel_id": channel_id,
            "message": caption,
            "file_ids": file_ids,
        }
        return await self.send_request("/posts", method="POST", data=data)
