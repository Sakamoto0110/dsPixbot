from pixbot.commands.helpers import *
from engine.CommandHandler.CommandDecorators import *

@pixbot_command
@description("Pokes the target user with a stick")
@minArgs(1)
def Poke(target):
    async def OnSucess(msg):
        aid = GetAuthorMentionString(msg)
        tid = GetTargetMentionString(msg,target)
        
        await msg.channel.send("{0} poked {1}, with a sitck.".format(aid,tid))
        pass
    return OnSucess
    
@pixbot_command
@description("Sends a hug to another user")
@minArgs(1)
def Hug(target):
    async def OnSucess(msg):
        aid = GetAuthorMentionString(msg)
        tid = GetTargetMentionString(msg,target)
        
        await msg.channel.send("{0} sended a hug to {1}".format(aid,tid))
        pass
    return OnSucess


@pixbot_command
@description("Sends a kiss to another user")
@minArgs(1)
def Kiss(target):
    async def OnSucess(msg):
        aid = GetAuthorMentionString(msg)
        tid = GetTargetMentionString(msg,target)
                    
        await msg.channel.send("{0} sended a kiss to {1}".format(aid,tid))
        pass
    return OnSucess

@pixbot_command
@description("Says something to another user")
@minArgs(2)
def Say(_msg,target):
    async def OnSucess(msg):
        aid = GetAuthorMentionString(msg)
        tid = GetTargetMentionString(msg,target)
                     
        await msg.channel.send("{0} says {1} to {2}".format(aid,_msg,tid))
        pass
    return OnSucess



@pixbot_command
@description("Gives a slap in another user")
@minArgs(0)
def Slap(target):
    async def OnSucess(msg):
        aid = GetAuthorMentionString(msg)
        tid = GetTargetMentionString(msg,target)
                        
        await msg.channel.send("{0} slaps {1}".format(aid,tid))
        pass
    return OnSucess


@pixbot_command
@description("Gives something beautiful to another user")
@minArgs(1)
def Give(obj: "Something beautfull",target: "The lucky one"):
    async def OnSucess(msg):
        aid = GetAuthorMentionString(msg)
        tid = GetTargetMentionString(msg,target)
                    
        await msg.channel.send("{0} gives a beautiful {1} to {2}".format(aid,obj,tid))
        pass
    return OnSucess