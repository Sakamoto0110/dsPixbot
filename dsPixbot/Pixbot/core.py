


CMD_MAP = {}
def ChkIfCommandExists(cmd_name):
  return cmd_name in CMD_MAP.keys()




def RegisterCommandHandler(_callableObj):
    
    import CommandHandler.Function
    func = CommandHandler.Function.Function(_callableObj)
    func_name = func.GetName()
    CMD_MAP[func_name] = func
    return CMD_MAP[func_name]



import discord



from CommandHandler.Function import Function



class CommandTemplate:
    
    def __init__(self) -> None:
        self.roles = []
        
        pass

class CommandFactory:
    s_buffer       : dict[str,any]         = {}
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
    def Register(_callable=None):
        def __buildPrefix(c: int) -> str:
            if c < 10: return "00"
            if c >= 10 and c <= 99: return "0"
            if c > 99: return ""

        try:
            fHandler = Function(_callable,CommandFactory.s_commandCount)            
            CommandFactory.s_templates.append(CommandTemplate())
            for key in CommandFactory.s_buffer: 
                # template variable
                if str(key).startswith('!t'):                    
                    CommandFactory.s_templates[CommandFactory.s_commandCount].roles.append(CommandFactory.s_buffer[key])                    
                # normal variable
                elif key in fHandler.descriptor.__dict__.keys():
                    fHandler.descriptor.__dict__[key] = CommandFactory.s_buffer[key]
                # invalid variable
                else:                    
                    print("property \"{0}\" does not exists in \"{1}\" object.".format(key,type(fHandler.descriptor).__name__))
            CMD_MAP[fHandler.descriptor.name] = fHandler
            prefix = __buildPrefix(CommandFactory.s_commandCount)
            print("[{0}{1}] Command registred: {2}.".format(prefix,CommandFactory.s_commandCount, fHandler.descriptor.name))
            CommandFactory.s_commandCount += 1
        except KeyError as err:
            print("Failed to register command. Details:\n{0} {1}".format(KeyError,err))            
        finally:
            CommandFactory.s_buffer.clear()
        return        
   
   
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# DECORATORS            
        
def pixbot_command(_callable) : return CommandFactory.Register(_callable)
def description(value)        : return CommandFactory.Property("description",value)
def minArgs(value)            : return CommandFactory.Property("minArgs",value)
    
def addRole(value)            :  return CommandFactory.Property("!t",value)



intents = discord.Intents.default()
intents.members = True
__dClient = discord.Client(intents = intents)

def GetDiscordClient(): return __dClient

# DO NOT REMOVE THE FOLLOWING LINE!!!!
import Pixbot.events
def StartDiscordServer(token):        
    __dClient.run(token)






