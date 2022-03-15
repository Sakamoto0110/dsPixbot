NULL_PARAM = -2147483647    
class Parameter:
    
    def __init__(self,name,info,type = 0) -> None:
        self.name = name
        self.info = info
        self.preferedType = type
        pass
    pass