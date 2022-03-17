

from engine.CommandHandler import *
from engine.FunctionHandler import *


__dClient = None
def Init():
    import discord
    from discord import client
    intents = discord.Intents.default()
    intents.members = True
    global __dClient
    __dClient = discord.Client(intents = intents)
def Run(tok):
    global __dClient
    import pixbot.events
    __dClient.run(tok)
    
def discord_event(coro):  
    global __dClient
    if __dClient != None:
        __dClient.event(coro)
class Pixbot:
    JMPTB     : list[Function]        = []
    TMPLTB    : list[CommandTemplate] = []
    
    def __init__(self) -> None:
        
        pass
   
    @staticmethod   
    def __TableAcessors(tb_name, _mode : "read|write|append" = "read"):
        def _getTable(name):            
            if name == "cmd"      : return Pixbot.JMPTB
            if name == "template" : return Pixbot.TMPLTB
            return None 
        if (tb := _getTable(tb_name)) != None:
            def _read(__val,__pred):
                if __val != None and __pred != None:
                    for tb_value in tb:
                        if __pred(tb_value,__val):                         
                            return tb_value
                return tb
            def _write(__val,__pred):
                for i in range(0,len(tb)):
                    if __pred(tb[i],__val):
                        tb[i] = __val
                        return tb[i]
            def _append(__val):
                tb.append(__val)
                return tb[len(tb)-1]
            
            if _mode == "read"     : return _read
            if _mode == "write"    : return _write
            if _mode == "append"   : return _append
            
        return None
            
    @staticmethod
    def __RetrieveData(tb_name, val=None, predicate=None) : return Pixbot.__TableAcessors(tb_name,"read")(val, predicate)   
    @staticmethod
    def __WriteData(tb_name, val, predicate)              : return Pixbot.__TableAcessors(tb_name,"write")(val, predicate)
    @staticmethod
    def __AppendData(tb_name, val)                        : return Pixbot.__TableAcessors(tb_name,"append")(val)

 
    @staticmethod
    def GetTable(tb_name): return Pixbot.__RetrieveData(tb_name, "read")
    
    @staticmethod 
    def GetCommand(cmd_name): return Pixbot.__RetrieveData("cmd", cmd_name, lambda cmd, _name: cmd.descriptor.name == _name)
    
    @staticmethod
    def AppendCommand(cmd): return Pixbot.__AppendData("cmd", cmd)
    
    @staticmethod
    def AppendTemplate(tmpl): return Pixbot.__AppendData("template", tmpl)
    
    @staticmethod
    def GetTemplate(tmpl_id): return Pixbot.__RetrieveData("template", tmpl_id, lambda template, id : template.id == id)
    
    
    @staticmethod 
    def GetSuper(cmd_name):
        cmd = Pixbot.__RetrieveData("cmd", cmd_name, lambda cmd, _name: cmd.descriptor.name == _name)
        if cmd != None:
            tmpl = Pixbot.__RetrieveData("template", cmd.GetID(), lambda template, id : template.id == id)
            return  {
                "commandFunction" : cmd,
                "commandTemplate" : tmpl
            }
       
    
    
    pass



