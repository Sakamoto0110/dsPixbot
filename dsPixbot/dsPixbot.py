
from Pixbot.core import *
from Commands.core import *


VERSION = "0.1"



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

@pixbot_command
def Profile(summoner_name):
    result_msg = " "
    async def OnSucess(msg):
        await CALLBACK_SAY(msg,result_msg)
    lol_api_key = "RGAPI-a84d08d4-8a37-49a9-9236-a90906d9b10b"
    #/lol/match/v5/matches/by-puuid/{puuid}/ids
    url_base = "https://br1.api.riotgames.com"   
    url = "{0}/lol/summoner/v4/summoners/by-name/{1}".format(url_base,str(summoner_name).replace(" ","%20"))
    import requests
    headers = {'X-Riot-Token': lol_api_key}
    response = requests.request("GET", url,headers=headers)
    print("status: {0}".format(response.status_code))
    import json
    obj = json.loads(response.text)
    print(obj["id"])
    url = "{0}/lol/champion-mastery/v4/champion-masteries/by-summoner/{1}".format("https://br1.api.riotgames.com",str(obj["id"]))

    response = requests.request("GET", url,headers=headers)
    print("status: {0}".format(response.status_code))
    h = json.loads(response.text)
    
    result_msg = "{0}".format(h[0]["championPoints"])
    return OnSucess




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

print("Program started")
print("Starting discord server")
import tok
StartDiscordServer(tok.GetDiscordToken())



