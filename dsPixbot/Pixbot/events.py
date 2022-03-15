from Pixbot.core import ChkIfCommandExists, __dClient


@__dClient.event
async def on_ready():
    print('ok')
    print("Logged in as {0.user}".format(__dClient))
    return



@__dClient.event
async def on_message(msg):    
    import CommandHandler.CommandParser
    import CommandHandler.Command
    from Pixbot.core import CMD_MAP
    if(msg.author == __dClient.user):
        return
    str = msg.content
    if str.startswith(CommandHandler.Command.Command.KEY):
        str = str.lstrip(CommandHandler.Command.Command.KEY)
        command = CommandHandler.CommandParser.UnpackCommand(str)
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