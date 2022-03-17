from engine.FunctionHandler.FunctionMetadata import fMetadata
import engine.FunctionHandler 





class Function:        
    def __init__(self,_callableObj, _id) -> None:
        self.id = _id
        self.callableObj = _callableObj
        self.descriptor = fMetadata(_callableObj)
        
        pass

    def GetID(self): return self.id
 
    def GetParameters(self):        
        return self.descriptor.parameters
    def GetInvoker(self):
        from engine.Invoker import Invoker
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