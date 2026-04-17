# made by gemini
import asyncio
from pixbot.commands.core import *
from pixbot.Pixbot import Pixbot
from engine.command_handler.CommandDecorators import *

# Uncomment the provider you want to use:
# from engine.Platform.discord_impl import DiscordProvider
from engine.platform.cli_impl import CLIProvider
# from engine.Platform.wpp_impl import WPPProvider

 
async def main():
   
    # 1. Instantiate the chosen provider
    provider = CLIProvider() # Swapped to CLI for testing without auth
    
    # 2. Inject into engine
    engine = Pixbot(provider)
    
    try:
        # 3. Start loop. (Pass your Discord token here if using DiscordProvider)
        await engine.start(None) 
    except KeyboardInterrupt:
        await engine.provider.stop()
    except Exception as e:
        print(f"Fatal error during execution: {e}")
    finally:
        print("Shutdown complete.")

if __name__ == "__main__":
    # made by gemini
    asyncio.run(main())