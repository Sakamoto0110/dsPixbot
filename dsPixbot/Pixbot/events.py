from pixbot.core import ChkIfCommandExists, __dClient


@__dClient.event
async def on_ready():
    print('ok')
    print("Logged in as {0.user}".format(__dClient))
    return


import engine.CommandHandler as cHandler
@__dClient.event
async def on_message(msg):    
    
    from pixbot.core import CMD_MAP
    if(msg.author == __dClient.user):
        return
    str = msg.content
    KEY = '!'
    if str.startswith(KEY):
        str = str.lstrip(KEY)
        command = cHandler.UnpackCommand(str)
        if ChkIfCommandExists(command.header):
            f = CMD_MAP[command.header](*command.args)
            if f != None:
                await f(msg)
            
                
            

@__dClient.event
async def on_member_join(member):
    
    print("ok")
    for channel in __dClient.get_all_channels():
        if channel.name == 'geral':
            await channel.send(
                f'Hi {member.mention}, Message to send when member joins')
    return