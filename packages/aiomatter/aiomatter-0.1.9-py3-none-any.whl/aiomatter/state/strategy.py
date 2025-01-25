from enum import Enum, auto


class FSMStrategy(Enum):
    """
    Defines storage strategies for finite-state machines.
    """

    USER_IN_CHAT = auto()
    """State is stored for each user in a specific chat."""
    CHAT = auto()
    """State is stored globally for a chat."""
    GLOBAL_USER = auto()
    """State is stored globally for a user."""


def apply_strategy(
    strategy: FSMStrategy, chat_id: int, user_id: int
) -> tuple[int, int]:
    """
    Apply the given strategy to determine state storage keys.

    :param strategy: The strategy to apply.
    :param chat_id: The ID of the chat.
    :param user_id: The ID of the user.
    :return: Tuple of chat_id and user_id based on strategy.
    """
    if strategy == FSMStrategy.CHAT:
        return chat_id, chat_id
    if strategy == FSMStrategy.GLOBAL_USER:
        return user_id, user_id
    return chat_id, user_id
