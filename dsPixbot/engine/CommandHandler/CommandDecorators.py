## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
## DECORATORS            
from  engine.CommandHandler import *
def pixbot_command(_callable) : return CommandFactory.Register(_callable)
def description(value)        : return CommandFactory.Property("description",value)
def minArgs(value)            : return CommandFactory.Property("minArgs",value)
def role(value)               : return CommandFactory.Appender("roles",value)
