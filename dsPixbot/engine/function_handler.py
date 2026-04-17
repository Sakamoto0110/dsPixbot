import re
from engine.command_handler.models import Parameter
class FunctionMetadata:
    def __init__(self,_callableObj) -> None:
        import inspect
        self.name = _callableObj.__name__
        self.parameters ={}
        self.minArgs = 0        
        #self.description = ""    
        self._signature = inspect.signature(_callableObj)
        signature  =self._signature
        self.maxArgs = len(signature.parameters.keys())
        args_string = ""
   
        for param_key in  signature.parameters.keys():             
            param_obj = signature.parameters[param_key]            
            param_dft_value = None
            if param_obj.default == inspect._empty:
                self.minArgs += 1       
            else:
                param_dft_value = param_obj.default
            if self.name == "Dummy":
                print("-> " + str(param_obj.default))
            param_name = param_obj.name
            param_description = param_obj.annotation if param_obj.annotation != inspect._empty else "no_description"
            param = Parameter(param_name,param_description,param_dft_value)
            args_string += " {0}".format(param.name)
            self.parameters[param_key] = param

class Function:        
    def __init__(self,_callableObj, _id) -> None:
        self.id = _id
        self.callableObj = _callableObj
        self.descriptor = FunctionMetadata(_callableObj)
        
        pass

    def GetID(self): return self.id
    def GetSignature(self): return self.descriptor._signature
    def GetParameters(self):        
        return self.descriptor.parameters
    def GetInvoker(self):
        from engine.invoker import Invoker
        return Invoker(self)
    def GetParameterString(self):
        result_str = ""
        paramsArr = self.GetParameters()
        for param in paramsArr.keys():
            result_str += "{0} ".format(paramsArr[param].name)
        return result_str.rstrip(" ")

    def __call__(self,*args):
        maxArgs    = self.descriptor.maxArgs
        minArgs    = self.descriptor.minArgs
        nArgs      = len(args)
        # Error handling
        if nArgs < minArgs or nArgs > maxArgs:
            error_str = "Unable to perform \"{0}\" call".format(self.descriptor.name)
            reasson_str =  " missing {0} arguments".format(maxArgs-nArgs) if nArgs < minArgs else " too many arguments[{0},{1}]".format(minArgs,maxArgs)
            print(error_str + reasson_str)        
            #return DEFAULT_ERROR_ASYNC_HANDLER(args, FunctionBadCall(error_str,reasson_str))
            return
        #Fixes variadic argument list        
        if(nArgs >= minArgs and nArgs < maxArgs):                  
            # Merge the tuple with dummy values, results in a list
            paramlist = []
            for k in self.descriptor.parameters.keys():
                paramlist.append(self.descriptor.parameters[k])
            # print("min args       : " + str(minArgs))
            # print("max args       : " + str(maxArgs))
            # print("args len       : " + str(nArgs))
            # print("paramlist len  : " + str(len(paramlist)))
            # print("max - nArgs    : " + str(maxArgs-nArgs))
            args = [*args]+[(paramlist[i].default_value) for i in range(minArgs,maxArgs - nArgs)] 
            
        return self.callableObj(*args)

    def __str__(self):
        param_str = ""
        for param in self.descriptor.parameters:
            param_str += "{0}, ".format(param)
        param_str = param_str.rstrip(", ")
        return "{0}({1})".format(self.descriptor.name,param_str)