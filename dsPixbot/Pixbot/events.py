
from pixbot.Pixbot import __dClient,discord_event
@discord_event
async def on_ready():
    print('ok')
    print("Logged in as {0.user}".format(__dClient))
    return


import engine.CommandHandler as cHandler

            
@discord_event
async def on_message(msg):        

    def chkPermissions(author, roles_permited):
        for role in roles_permited:
            for arole in author.roles:
                if arole.name == role:
                    return True
        return False            
    
    
    
    if(msg.author == __dClient.user):
        return
    str = msg.content
    KEY = '!'
    from pixbot.Pixbot import Pixbot
    if str.startswith(KEY):
        str = str.lstrip(KEY)
        command = cHandler.UnpackCommand(str)
        _f = None
        if (f := Pixbot.GetCommand(command.header)) != None:
            t = Pixbot.GetTemplate(f.GetID())
            if len(t.roles) >= 1:  
                found = False              
                for role in t.roles:
                    for arole in msg.author.roles:
                        if arole.name == role:
                            found = True    
                            break
                    if found: 
                        break
                if found:
                    _f = f(*command.args)
                else:
                    print("Acesso negado de {0} ao comando: {1}.".format(msg.author, f.descriptor.name))
                    msg.channel.send("Acesso negado.")
            else:                                    
                _f = f(*command.args)            
            if _f != None:
                await _f(msg)
            
            
            
        
            
@discord_event
async def on_member_join(member):
    
    print("ok")
    for channel in __dClient.get_all_channels():
        if channel.name == 'geral':
            await channel.send(
                f'Hi {member.mention}, Message to send when member joins')
    return