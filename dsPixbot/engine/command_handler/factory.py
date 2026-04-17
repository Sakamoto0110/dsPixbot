import sys
import importlib
import pkgutil
import traceback
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
        from pixbot.bot import Pixbot
        from engine import function_handler
        from engine.command_handler.models import CommandTemplate

        cmd_id = len(Pixbot.COMMAND_MAP)
        
        # 1. Create the engine objects
        fHandler =  function_handler.Function(_callable, cmd_id)            
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
    








    @staticmethod
    def unload_all() -> dict:
        """Stops modules and clears engine memory."""
        prefix = "pixbot.commands"
        from pixbot.bot import Pixbot
        old_commands = set(Pixbot.COMMAND_MAP.keys())
        unloaded_modules = []
        
        target_modules = [m for n, m in sys.modules.items() if n.startswith(prefix)]
        
        for module in target_modules:
            teardown = getattr(module, "teardown", None)
            if callable(teardown):
                try: teardown()
                except Exception: print(traceback.format_exc())
            
            unloaded_modules.append(module.__name__)
            
        Pixbot.COMMAND_MAP.clear()
        Pixbot.TEMPLATE_MAP.clear()
        
        return {
            "modules": unloaded_modules, # List of strings
            "commands": old_commands     # Set of command names
        }

    @staticmethod
    def load_all() -> dict:
        """Discovers and imports all command modules."""
        import pixbot.commands 
        from pixbot.bot import Pixbot

        prefix = "pixbot.commands"
        loaded_modules = []
        
        for loader, name, is_pkg in pkgutil.walk_packages(pixbot.commands.__path__, prefix + "."):
            if is_pkg: continue
            try:
                importlib.import_module(name)
                loaded_modules.append(name)
            except Exception: print(traceback.format_exc())
                
        return {
            "modules": loaded_modules,      # List of strings
            "commands": set(Pixbot.COMMAND_MAP.keys()) # Set of command names
        }

    @staticmethod
    def perform_hot_reload() -> dict:
        """Conducts the full cycle and returns the delta report."""
        # 1. Capture what we HAD
        unload_data = CommandFactory.unload_all()
        
        # 2. Scorch the python cache
        prefix = "pixbot.commands"
        for mod_name in list(sys.modules.keys()):
            if mod_name.startswith(prefix):
                del sys.modules[mod_name]
                
        # 3. Capture what we HAVE NOW
        load_data = CommandFactory.load_all()
        
        # 4. Calculate the Delta
        old_cmds = unload_data["commands"]
        new_cmds = load_data["commands"]
        
        return {
            "modules_unloaded": unload_data["modules"], # FULL LIST
            "modules_loaded": load_data["modules"],     # FULL LIST
            "commands_added": list(new_cmds - old_cmds),
            "commands_removed": list(old_cmds - new_cmds),
            "commands_maintained": list(new_cmds & old_cmds)
        }

    @staticmethod
    def clear_module_cache():
        # Purge commands AND the bot's core files
        prefixes = ("pixbot.commands", "pixbot.Pixbot", "engine.")
        for mod_name in list(sys.modules.keys()):
            if mod_name.startswith(prefixes):
                del sys.modules[mod_name]
        # 2. Clear the Filesystem Cache (Hard Drive Index)
        # This forces Python to physically re-read the folders for new/deleted files
        importlib.invalidate_caches()




# import pixbot.commands 
# from pixbot.bot import Pixbot
 
        """Gracefully shuts down modules before they are purged."""
        prefix = "pixbot.commands"
        
        # 1. Identify all currently loaded command modules
        # We use a list copy because sys.modules might change during iteration
        target_modules = [
            mod for name, mod in sys.modules.items() 
            if name.startswith(prefix)
        ]
        
        for module in target_modules:
            # 2. Check for a 'teardown' hook
            # (You could also use 'unload', just pick one convention)
            teardown_func = getattr(module, "teardown", None)
            
            if callable(teardown_func):
                try:
                    teardown_func()
                    # If you want to support async teardowns:
                    # if asyncio.iscoroutinefunction(teardown_func):
                    #     asyncio.create_task(teardown_func())
                except Exception:
                    print(f"  [ERROR] Teardown failed in {module.__name__}")
                    print(traceback.format_exc())

        # 3. Clear the engine maps
        from pixbot.bot import Pixbot
        Pixbot.COMMAND_MAP.clear()
        Pixbot.TEMPLATE_MAP.clear()