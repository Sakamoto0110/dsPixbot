class CALLBACK:
    def __init__(self,cb_src):
        self.callback = cb_src
    def __call__(self,*args):
        return self.callback(*args)

async def _CALLBACK_SAY(msgHandler,str):
    
    await msgHandler.channel.send(str)
    
CALLBACK_SAY = CALLBACK(_CALLBACK_SAY)