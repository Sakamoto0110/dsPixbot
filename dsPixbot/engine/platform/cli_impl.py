# made by gemini
import asyncio
from engine.platform.core import IBotContext, IPlatformProvider

class CLIContext(IBotContext):
    # made by gemini
    def __init__(self, content: str):
        super().__init__(
            platform_name="CLI",
            raw_message=content,
            author_id=0,
            author_name="ConsoleUser",
            content=content
        )

    async def reply(self, text: str):
        # made by gemini
        print(f"\n[Pixbot]: {text}")

    def has_permission(self, permission_id: str) -> bool:
        # made by gemini
        return True

class CLIProvider(IPlatformProvider):
    # made by gemini
    def __init__(self):
        super().__init__(bot_instance=None)
        self.running = False

    async def start(self, token: str = None):
        # made by gemini
        self.running = True
        print("--- Pixbot CLI Mode Started (No Auth Required) ---")
        print("Type 'exit' to stop.")
        
        loop = asyncio.get_event_loop()
        
        while self.running:
            user_input = await loop.run_in_executor(None, lambda: input("You> "))
            
            if user_input.lower() in ['exit', 'quit']:
                await self.stop()
                break
            
            if not user_input.strip():
                continue

            ctx = CLIContext(user_input)
            await self.bot.process_message(ctx)

    async def stop(self):
        # made by gemini
        self.running = False
        print("Shutting down CLI provider...")