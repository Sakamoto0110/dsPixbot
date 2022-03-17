from pixbot.commands.helpers import *
from engine.CommandHandler.CommandDecorators import *
from engine.callback import CALLBACK_SAY




@pixbot_command
@description("Rolls a Dice")
@minArgs(1)
def Dice(n: "Numero de lados"):
    
    async def OnSucess(cmd):    
     
        import random
        try:
            _n = int(n)
            value = random.randint(0,_n)
            result_str = "Nice! You rolled a {0}.".format(value)
            await CALLBACK_SAY(cmd,result_str)
        except ValueError:
            pass
    
    
    
    return OnSucess

def Slots():
    
    from random import randint
    vMin = 1
    vMax = 3
    a = 0
    b = 0
    c = 0
    a = randint(vMin,vMax)
    b = randint(vMin,vMax)
    c = randint(vMin,vMax)
    result_str = "Values rolled: [{0}, {1}, {2}] ".format(a,b,c)
    if a == b and b == c:
        result_str += "You WIN!!!"        
    else:
        result_str += "You lose :(. Better luck next time."

    async def OnSucess(cmd):    
        await CALLBACK_SAY(cmd,result_str)
    
    
    return OnSucess
