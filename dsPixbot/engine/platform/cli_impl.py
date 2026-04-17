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
        self.running = True
        # Clear the terminal before showing the "Starting" banner
        # print("\033[H\033[2J", end="", flush=True)
        print("--- Pixbot CLI Mode Started (No Auth Required) ---")
        print("Type 'exit' to stop.")
        
        loop = asyncio.get_event_loop()
        
        while self.running:
            user_input = await loop.run_in_executor(None, lambda: input("You> "))
            
            if user_input.lower() in ['exit', 'quit']:
                await self.stop()
                return "SHUTDOWN" # Treat manual exit as a shutdown
            
            if not user_input.strip():
                continue

            ctx = CLIContext(user_input)
            
            # Catch the signal from the bot
            signal = await self.bot.process_message(ctx)
            
            if signal in ["SHUTDOWN", "RESTART"]:
                await self.stop()
                return signal # Pass it to the Supervisor

    async def stop(self):
        # made by gemini
        self.running = False
        print("Shutting down CLI provider...")