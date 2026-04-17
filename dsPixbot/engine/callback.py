# made by gemini
class CALLBACK:
    # made by gemini
    def __init__(self, cb_src):
        self.callback = cb_src
    def __call__(self, *args):
        return self.callback(*args)

async def _CALLBACK_SAY(context, text):
    # made by gemini
    if context == None:
        print(text)
        return
    # Now uses the normalized reply method instead of .channel.send
    await context.reply(text)
    
CALLBACK_SAY = CALLBACK(_CALLBACK_SAY)