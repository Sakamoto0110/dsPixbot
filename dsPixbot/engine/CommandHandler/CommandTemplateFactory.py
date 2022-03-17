from engine.CommandHandler.CommandTemplate import CommandTemplate
class CommandFactory:
    s_buffer       : dict[str,any]         = { }
    s_bufferex     : dict[str,list[any]]   = { }
    s_commandCount : int                   = 0

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
                if not args[0] in CommandFactory.s_bufferex.keys():
                    CommandFactory.s_bufferex[args[0]] = []                   
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
            from pixbot.Pixbot import Pixbot
            fHandler = engine.FunctionHandler.Function(_callable,CommandFactory.s_commandCount)            
            template = CommandTemplate(CommandFactory.s_commandCount)
            
            for key in CommandFactory.s_buffer: 
                if key in template.__dict__:
                    template.__dict__[key] = CommandFactory.s_buffer[key]                
            for key in CommandFactory.s_bufferex: 
                if key in template.__dict__:
                    template.__dict__[key] = CommandFactory.s_bufferex[key]
       
          
            Pixbot.AppendCommand(fHandler)
            Pixbot.AppendTemplate(template)
           
            prefix = __buildPrefix(CommandFactory.s_commandCount)
            print("[{0}{1}] Command registred: {2}.".format(prefix,CommandFactory.s_commandCount, fHandler.descriptor.name))
            CommandFactory.s_commandCount += 1
        except KeyError as err:
            print("Failed to register command. Details:\n{0} {1}".format(KeyError,err))            
        finally:
            CommandFactory.s_buffer.clear()
            CommandFactory.s_bufferex.clear()
        return