from CommandHandler.Parameter import *
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
            param = Parameter(param_obj.name,param_obj.annotation)
            if param_obj.kind == inspect._empty:
                self.minArgs += 1            
            args_string += " {0}".format(param.name)
            self.parameters[param_key] = param
            
     
    

