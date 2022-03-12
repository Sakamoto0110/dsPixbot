from Pixbot.core import ChkIfCommandExists, CommandFactory, CommandTemplate, __dClient

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
            f = CMD_MAP[command.header]
            r = None
            template = CommandFactory.s_templates[f.GetID()]
            if len(template.roles) >= 1:
                c = 0
                for role in msg.author.roles:                    
                    if role.name in template.roles:
                        c += 1                        
                if len(template.roles) == c:
                    r = f(*command.args)   
                else:
                    print("Acesso negado de {0} ao comando {1}".format(msg.author,f.descriptor.name))             
                    await msg.channel.send("Acesso negado.")
            else:
                r = f(*command.args)
            if r != None:
                await r(msg)
            

@__dClient.event
async def on_member_join(member):
    
    print("ok")
    for channel in __dClient.get_all_channels():
        if channel.name == 'geral':
            await channel.send(
                f'Hi {member.mention}, Message to send when member joins')
    return