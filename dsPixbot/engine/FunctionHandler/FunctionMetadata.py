from engine.FunctionHandler.Parameter import *
class fMetadata:
    def __init__(self,_callableObj) -> None:
        import inspect
        self.name = _callableObj.__name__
        self.parameters ={}
        self.minArgs = 0        
        #self.description = ""    
        signature = inspect.signature(_callableObj)
        self.maxArgs = len(signature.parameters.keys())
        args_string = ""
   
        for param_key in  signature.parameters.keys():             
            param_obj = signature.parameters[param_key]            
            if param_obj.default == inspect._empty:
                self.minArgs += 1        
            param_name = param_obj.name
            param_description = param_obj.annotation if param_obj.annotation != inspect._empty else "no_description"
            param = Parameter(param_name,param_description)
            args_string += " {0}".format(param.name)
            self.parameters[param_key] = param
            
     
    

