import asyncio
from pixbot.bot import Pixbot
from engine.platform.cli_impl import CLIProvider
from  engine.command_handler.decorators import *
# Import whatever you use to register commands (e.g., your decorators/factory)


async def main():
    while True:
        # 1. Purge the static state for a true clean slate
        Pixbot.COMMAND_MAP.clear()
        Pixbot.TEMPLATE_MAP.clear()
        from engine.command_handler.factory import CommandFactory
        CommandFactory.clear_module_cache()

        # 2. Re-import / Register your commands here so they populate the fresh dicts
        # (If you have a function that loads your command files, call it here)
        
        CommandFactory.load_all() 

        # 3. Boot the engine
        provider = CLIProvider()
        bot = Pixbot(provider)
        
        # 4. Await the loop. It will block here until a signal is returned
        # signals will be used in future
        exit_signal = await bot.start() 
        
         

if __name__ == "__main__":
    asyncio.run(main())