from engine.CommandHandler.CommandDecorators import *
from engine.FunctionHandler import *
from engine.callback import *
from pixbot.core import *
'''
TEMPLATE

def foo(*args):
    # Hard logic here
    # Creates the response message
    # If fail in any way ( like invalid sintax, invalid value, etc), MUST return the apropriate state callback
    def OnSucess(handler):
        # Execute a callback that consumes the response message
        await CALLBACK_SAY(handler,response_string)
    def OnFail(handler):
        # Clear variables, do log, give error feedback
        await CALLBACK_SAY(handler,error_string)
    # default: return OnSucess ---- MUST RETURN THE CALLBACK
    # can return other callbacks for diferent situations


'''

# @pixbot_command
# @description("Provides extra info for the desired command, if no target command is passed, will provide the command list ")
# @minArgs(0)
# def Help(targetCommand= NULL_PARAM):
#     from pixbot.core import ChkIfCommandExists
#     #from pixbot.core import JMPTB
#     #from pixbot.core import TMPLTB
#     from pixbot.Pixbot import Pixbot
#     KEY = '!'
#     result_str = ""
#     #__CMD_MAP = Pixbot.core.GetCommandMap()
#     if(targetCommand != NULL_PARAM):
        
#         if( (i := ChkIfCommandExists(targetCommand)) != -1):   
#             #f = JMPTB[i]
#             #template = TMPLTB[f.GetID()]
            
#             info = f.descriptor
#             result_str += "**Operation name:** {0}\n".format(info.name)
#             result_str += "**Minimum args required:** {0}\n".format(info.minArgs)
#             result_str += "**Maximum args allowed:** {0}\n".format(info.maxArgs)
#             result_str += "**Description:** {0}\n".format(template.description)
#             result_str += "**Usage:** {0}{1} *{2}*\n".format(KEY,info.name,f.GetParameterString())
#             result_str += "**Roles:** {0}\n".format(str(template.roles))
#             result_str += "**Parameters:**\n".format()
#             for parameter in f.GetParameters().keys():
#                 result_str += "    - *{0}*: {1}\n".format(f.GetParameters()[parameter].name, f.GetParameters()[parameter].info)

           
#         else:
#             result_str = "Undefined command"
#     else:                
#         result_str = "Comandos disponiveis:\n"
#         for k in JMPTB: result_str += " > {0}{1} *{2}*\n".format(KEY,k.descriptor.name,k.GetParameterString())
            
#     async def OnSucess(msgHandle):      
        
#         await CALLBACK_SAY(msgHandle,result_str)
#     async def OnFail(msgHandle):
#         await CALLBACK_SAY(msgHandle,"Error")
#     return OnSucess if len(str(result_str))>0  else OnFail


@pixbot_command
@description("Provides extra info for the desired command, if no target command is passed, will provide the command list ")

def Help(targetCommand=None):
    from pixbot.Pixbot import Pixbot
    KEY = '!'
    result_str = ""
    if(targetCommand != None):
        if (f := Pixbot.GetCommand(targetCommand)) != None:
            template = Pixbot.GetTemplate(f.GetID())            
            info = f.descriptor
            result_str += "**Operation name:** {0}\n".format(info.name)
            result_str += "**Minimum args required:** {0}\n".format(info.minArgs)
            result_str += "**Maximum args allowed:** {0}\n".format(info.maxArgs)
            result_str += "**Description:** {0}\n".format(template.description)
            result_str += "**Usage:** {0}{1} *{2}*\n".format(KEY,info.name,f.GetParameterString())
            result_str += "**Roles:** {0}\n".format(str(template.roles))
            result_str += "**Parameters:**\n".format()
            for parameter in f.GetParameters().keys():
                result_str += "    - *{0}*: {1}\n".format(f.GetParameters()[parameter].name, f.GetParameters()[parameter].info)
        
 
        else:
            result_str = "Undefined command"
    else:                
        result_str = "Comandos disponiveis:\n"
        for k in Pixbot.GetTable("cmd"): result_str += " > {0}{1} *{2}*\n".format(KEY,k.descriptor.name,k.GetParameterString())
            
    async def OnSucess(msgHandle):      
        
        await CALLBACK_SAY(msgHandle,result_str)
    async def OnFail(msgHandle):
        await CALLBACK_SAY(msgHandle,"Error")
    return OnSucess if len(str(result_str))>0  else OnFail


@pixbot_command
def Usage(*args):
    result_msg = " "
    error_msg = " "
    async def OnSucess(msgHandler):
        
        await CALLBACK_SAY(msgHandler,"result_msg")
    async def OnFail(msgHandler):
        await CALLBACK_SAY(msgHandler,"error_msg")
    # Logic here
    
    return OnSucess

@pixbot_command
@description("Work In Progress.")
def Info(*args):
    result_msg = " "
    error_msg = " "
    async def OnSucess(msgHandler):
        await CALLBACK_SAY(msgHandler,"result_msg")
    async def OnFail(msgHandler):
        await CALLBACK_SAY(msgHandler,"error_msg")
    # Logic here
    
    return OnSucess

