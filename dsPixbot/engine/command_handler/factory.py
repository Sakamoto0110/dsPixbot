# made by gemini
class CommandFactory:
    
    @staticmethod
    def Property(prop_name, prop_value):
        def wrapper(_callable):
            # Initialize the metadata dict if it doesn't exist
            if not hasattr(_callable, "_cmd_meta"):
                _callable._cmd_meta = {}
            
            # Store the property
            _callable._cmd_meta[prop_name] = prop_value
            return _callable
        return wrapper
    
    @staticmethod
    def Appender(prop_name, prop_value):
        def wrapper(_callable):
            if not hasattr(_callable, "_cmd_meta"):
                _callable._cmd_meta = {}
            
            # Initialize the list if this is the first item being appended
            if prop_name not in _callable._cmd_meta:
                _callable._cmd_meta[prop_name] = []
                
            _callable._cmd_meta[prop_name].append(prop_value)
            return _callable
        return wrapper

    @staticmethod
    def Register(_callable):
        from pixbot.Pixbot import Pixbot
        import engine.function_handler
        from engine.command_handler.models import CommandTemplate

        cmd_id = len(Pixbot.COMMAND_MAP)
        
        # 1. Create the engine objects
        fHandler = engine.function_handler.Function(_callable, cmd_id)            
        template = CommandTemplate(cmd_id)
        
        # 2. THE MAGIC LOOP: Dynamically inject ALL metadata into the template
        # No hardcoded names! Whatever decorators were used, they get applied here.
        if hasattr(_callable, "_cmd_meta"):
            for attr_name, attr_value in _callable._cmd_meta.items():
                setattr(template, attr_name, attr_value)
        
        # 3. Register with the core engine
        Pixbot.AppendCommand(fHandler)
        Pixbot.AppendTemplate(template)
        if not Pixbot._SILENT:
            prefix = str(cmd_id).zfill(3)
            print(f"[{prefix}] Command registered: {fHandler.descriptor.name}.")
        
        return _callable