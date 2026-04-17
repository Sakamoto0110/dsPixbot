# made by gemini
from engine.command_handler import *

class Pixbot:
    # Now using dicts for O(1) access
    COMMAND_MAP : dict[str, any] = {} 
    TEMPLATE_MAP: dict[int, any] = {} 
    VERSION     : str = "0.2"
    BOT_NAME    : str = "Pixbot"
    _SILENT     : bool = False
    _WARNS      : bool = True
    _KEY        : str = '!'
    def __init__(self, provider) -> None:
        self.provider = provider
        self.provider.bot = self

    async def start(self, token: str):
        if not self._SILENT:
            print(f"--- {self.BOT_NAME} v{self.VERSION} Starting ---")
        await self.provider.start(token)

    @staticmethod 
    def GetCommand(cmd_name):
        return Pixbot.COMMAND_MAP.get(cmd_name)
    @staticmethod 
    def GetTable(tb_type):
        if(tb_type == "cmd"):
            return Pixbot.COMMAND_MAP.values()
        if(tb_type == "tmpl"):
            return Pixbot.TEMPLATE_MAP.values()
        return None
    
    @staticmethod
    def GetTemplate(tmpl_id):
        return Pixbot.TEMPLATE_MAP.get(tmpl_id)

    @staticmethod
    def AppendCommand(cmd):
        # made by gemini
        cmd_name = cmd.descriptor.name
        
        if cmd_name in Pixbot.COMMAND_MAP:
            if Pixbot._WARNS:
                print(f"[WARNING] A command named '{cmd_name}' is already registered! Ignoring the duplicate.")
            return False
            
        Pixbot.COMMAND_MAP[cmd_name] = cmd
        return True
    
    @staticmethod
    def AppendTemplate(tmpl):
        # made by gemini
        if tmpl.id in Pixbot.TEMPLATE_MAP:
            if Pixbot._WARNS:
                print(f"[WARNING] A template with ID '{tmpl.id}' already exists!")
            return False
            
        Pixbot.TEMPLATE_MAP[tmpl.id] = tmpl
        return True

    async def process_message(self, ctx):
        # made by gemini
        KEY = Pixbot._KEY
        if not ctx.content.startswith(KEY):
            return

        cmd_str = ctx.content.lstrip(KEY)
        command = UnpackCommand(cmd_str)
        
        if (f := self.GetCommand(command.header)):
            t = self.GetTemplate(f.GetID())
            
            # Use the abstract permission check
            if t.roles: 
                if any(ctx.has_permission(role) for role in t.roles):
                    _f = f(*command.args)
                else:
                    await ctx.reply("Acesso negado.")
                    return
            else:                                    
                _f = f(*command.args)            
            
            if _f:
                await _f(ctx)