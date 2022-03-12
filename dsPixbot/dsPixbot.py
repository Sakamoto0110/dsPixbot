
from Pixbot.core import *
from Commands.core import *


VERSION = "0.1"



@CommandFactory.Register
@CommandFactory.Property(prop_name="description", prop_value="happy description")
@addRole("dev")
def Hello():
    result_msg = "a"
    error_msg = " "
    async def OnSucess(msgHandler):
        await CALLBACK_SAY(msgHandler,result_msg)
    async def OnFail(msgHandler):
        await CALLBACK_SAY(msgHandler,"error_msg")
    # Logic here
    
    return OnSucess
'''
# @description(_description="Random kitten images")
# @pixbot_command
# def Kitten():
#     result_msg = "Hello, World!"
#     error_msg = " "
#     async def OnSucess(msgHandler:discord.Message):
        
#         await CALLBACK_SAY(msgHandler,result_msg)
#         await msgHandler.delete()
#     async def OnFail(msgHandler):
#         await CALLBACK_SAY(msgHandler,"error_msg")
#     # Logic here
#     import requests

#     url = "https://api.thecatapi.com/v1/images/search?category_ids=1"

#     headers = {'x-api-key': 'api_key=13f5782a-6c53-42a4-a948-b18b15b0eb9c'}

#     response = requests.request("GET", url)
#     import json
#     obj = json.loads(response.text)[0]
    
#     print("URL: {0}".format(obj["url"]))
#     result_msg = obj["url"]
#     return OnSucess
'''

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
     


print("Program started")
print("Starting discord server")
import MyToken
StartDiscordServer(MyToken.GetDiscordToken())



