from pixbot.commands.core import *
from  pixbot.Pixbot import *
from engine.CommandHandler.CommandDecorators import *
VERSION  = "0.1"
BOT_NAME = "Pixbot"

#TODO
# Options ( dynamic and saving )
# wellcome msg ( when bot joins in server for the first time)


@pixbot_command
@role("dev")
@role("aaaa")
def Dummy(_champion_name, _img_style : "valid values: centered | loading | splash | tiles" = "centered",  _skin_index = 0):
    result_msg = " "
    async def OnSucess(msg):
        await CALLBACK_SAY(msg,result_msg)
    def OnFail():
        print(result_msg)
    from RiotAPIAcessor.RiotDataDragonAcessor import GetChampionImageURL
    result_msg = GetChampionImageURL(_champion_name,_img_style,_skin_index)
    
    return OnSucess




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

print("Program started")
print("Starting discord server")
import MyTokens as tok
Init()
Run(tok.GetDiscordToken())




