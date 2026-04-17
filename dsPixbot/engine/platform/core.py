# made by gemini
from abc import ABC, abstractmethod

class IBotContext(ABC):
    # made by gemini
    def __init__(self, platform_name, raw_message, author_id, author_name, content):
        self.platform = platform_name
        self.raw_message = raw_message
        self.author_id = author_id
        self.author_name = author_name
        self.content = content

    @abstractmethod
    async def reply(self, text: str):
        """Sends a message back to the same channel/contact."""
        pass

    @abstractmethod
    def has_permission(self, permission_id: str) -> bool:
        """Abstracted permission check."""
        pass

class IPlatformProvider(ABC):
    # made by gemini
    def __init__(self, bot_instance=None):
        self.bot = bot_instance

    @abstractmethod
    async def start(self, token: str):
        """Starts the platform-specific event loop."""
        pass

    @abstractmethod
    async def stop(self):
        """Gracefully shuts down the connection."""
        pass