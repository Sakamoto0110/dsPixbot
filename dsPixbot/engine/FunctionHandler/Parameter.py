

from asyncio.windows_events import NULL


NULL_PARAM = -2147483647    
class Parameter:
    
    def __init__(self,name,info,dft_value = None,type = 0) -> None:
        self.name = name
        self.info = info
        self.default_value = dft_value 
        if self.name == "_img_style":
            print("<" + str(self.default_value))
        self.preferedType = type
        pass
    pass