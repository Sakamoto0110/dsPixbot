


CMD_MAP = {}
def ChkIfCommandExists(cmd_name):
  return cmd_name in CMD_MAP.keys()


# TODO
# Move to own file
#
class CommandTemplate:
    
    def __init__(self) -> None:
        self.roles = []
        self.description = "no_description"
        pass

class CommandFactory:
    s_buffer       : dict[str,any]         = {}
    s_bufferex     : dict[str,list[any]]   = {}
    s_commandCount : int                   = 0
    s_templates    : list[CommandTemplate] = [] 

    @staticmethod
    def Property(prop_name=None, prop_value = None):
        import functools                                   
        def wrapper(_func):        
            @functools.wraps(_func)
            def inner(*args,**kwargs):                
                CommandFactory.s_buffer[args[0]] = args[1]                
                return _func
            return inner(prop_name,prop_value)                          
        return wrapper
    
    @staticmethod
    def Appender(prop_name=None, prop_value = None):
        import functools                                   
        def wrapper(_func):        
            @functools.wraps(_func)
            def inner(*args,**kwargs):                
                CommandFactory.s_bufferex[args[0]].append(args[1])                
                return _func
            return inner(prop_name,prop_value)                          
        return wrapper


    @staticmethod
    def Register(_callable=None):
        import engine.FunctionHandler
        def __buildPrefix(c: int) -> str:
            if c < 10: return "00"
            if c >= 10 and c <= 99: return "0"
            if c > 99: return ""

        try:
            fHandler = engine.FunctionHandler.Function(_callable,CommandFactory.s_commandCount)            
            CommandFactory.s_templates.append(CommandTemplate())           
            for key in CommandFactory.s_buffer: 
                if key in CommandFactory.s_templates[CommandFactory.s_commandCount].__dict__:
                    CommandFactory.s_templates[CommandFactory.s_commandCount].__dict__[key] = CommandFactory.s_buffer[key]                
            for key in CommandFactory.s_bufferex: 
                if key in CommandFactory.s_templates[CommandFactory.s_commandCount].__dict__:
                    CommandFactory.s_templates[CommandFactory.s_commandCount].__dict__[key] = CommandFactory.s_bufferex[key]

            CMD_MAP[fHandler.descriptor.name] = fHandler
            prefix = __buildPrefix(CommandFactory.s_commandCount)
            print("[{0}{1}] Command registred: {2}.".format(prefix,CommandFactory.s_commandCount, fHandler.descriptor.name))
            CommandFactory.s_commandCount += 1
        except KeyError as err:
            print("Failed to register command. Details:\n{0} {1}".format(KeyError,err))            
        finally:
            CommandFactory.s_buffer.clear()
            CommandFactory.s_bufferex.clear()
        return        
   
   
## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
## DECORATORS            
        
def pixbot_command(_callable) : return CommandFactory.Register(_callable)
def description(value)        : return CommandFactory.Property("description",value)
def minArgs(value)            : return CommandFactory.Property("minArgs",value)
def role(value)               : return CommandFactory.Appender("role",value)



import discord
from discord import client
intents = discord.Intents.default()
intents.members = True
__dClient = discord.Client(intents = intents)

def GetDiscordClient(): return __dClient

# DO NOT REMOVE THE FOLLOWING LINE!!!!
import pixbot.events
def StartDiscordServer(token):        
    __dClient.run(token)

