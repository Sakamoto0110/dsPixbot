# made by gemini
from engine.platform.core import IBotContext, IPlatformProvider

class WPPContext(IBotContext):
    # made by gemini
    def __init__(self, wpp_msg):
        super().__init__(
            platform_name="WhatsApp",
            raw_message=wpp_msg,
            author_id=wpp_msg.info.sender.String(), 
            author_name=wpp_msg.info.push_name or "WPP User",
            content=wpp_msg.message.conversation or wpp_msg.message.extendedTextMessage.text
        )

    async def reply(self, text: str):
        # made by gemini
        await self.provider_client.send_message(self.author_id, text)

    def has_permission(self, permission_id: str) -> bool:
        # made by gemini
        admin_numbers = ["5511999999999@s.whatsapp.net"] 
        if permission_id == "Admin":
            return self.author_id in admin_numbers
        return True

class WPPProvider(IPlatformProvider):
    # made by gemini
    def __init__(self):
        super().__init__(bot_instance=None)
        self.client = None

    async def start(self, session_name: str):
        # made by gemini
        # Replace 'some_wpp_library' with your actual wrapper (e.g., neonize)
        from some_wpp_library import NewClient 
        
        self.client = NewClient(session_name)
        
        @self.client.event
        async def on_message(wpp_msg):
            if wpp_msg.info.from_me:
                return
            
            ctx = WPPContext(wpp_msg)
            ctx.provider_client = self.client 
            await self.bot.process_message(ctx)

        print(f"Connecting to WhatsApp session: {session_name}...")
        await self.client.connect()

    async def stop(self):
        # made by gemini
        if self.client:
            print("Disconnecting WhatsApp...")
            await self.client.disconnect()