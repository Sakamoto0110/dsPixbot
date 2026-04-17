# made by gemini
import discord
from engine.platform.core import IBotContext, IPlatformProvider

class DiscordContext(IBotContext):
    # made by gemini
    def __init__(self, msg: discord.Message):
        super().__init__(
            platform_name="Discord",
            raw_message=msg,
            author_id=msg.author.id,
            author_name=msg.author.name,
            content=msg.content
        )

    async def reply(self, text: str):
        # made by gemini
        await self.raw_message.channel.send(text)

    def has_permission(self, permission_id: str) -> bool:
        # made by gemini
        return any(role.name == permission_id for role in self.raw_message.author.roles)

class DiscordProvider(IPlatformProvider):
    # made by gemini
    def __init__(self):
        super().__init__(bot_instance=None)
        self.client = None

    async def start(self, token: str):
        intents = discord.Intents.default()
        intents.members = True
        self.client = discord.Client(intents=intents)
        
        @self.client.event
        async def on_message(msg):
            if msg.author == self.client.user: 
                return
            await self.bot.process_message(DiscordContext(msg))

        await self.client.start(token)

    async def stop(self):
        # made by gemini
        if self.client: 
            print("Closing Discord connection...")
            await self.client.close()