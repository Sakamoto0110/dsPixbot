class Invoker:


    def __init__(self,_func) -> None:
        self.command = None
        self.function = _func
        pass

    
    def Invoke(self,*args):
        return self.function(*args)

    def CheckBinding(self,commandBinding):
        if commandBinding == None:
            return False
        if commandBinding.header != self.function.descriptor.name:
            return False
        if len(commandBinding.args) < self.function.descriptor.minArgs:
            return False
        if len(commandBinding.args) > self.function.descriptor.maxArgs:
            return False
        return True

    def BindCommand(self,command):
        if self.CheckBinding(command):
            self.command = command            
            return True
        
        return False
    def LateInvoke(self):
        if self.command == None:
            print("Unable to perform late call with [{0}], missing command binding".format(self.function.GetName()))
            return
        args = self.command.args
        self.command = None
        return self.Invoke(*args)
        
    pass