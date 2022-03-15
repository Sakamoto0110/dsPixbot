from engine._commandHandler.Command import Command



def PackCommand(command) -> str:
    result_str = "{0} ".format(command.header)
    for _str in command.args:
        result_str += "{0} ".format(_str)
    return result_str
    
def PackCommandArgs(command) -> str:
    result_str = ""
    for _str in command.args: result_str += "{0} ".format(_str)
    return result_str

#def UnpackCommand(_str) -> Command:
#    _strArr = [_ for _ in splitStringEx(_str,False)]
#    cmd = Command()
#    cmd.header = _strArr[0]
#    _strArr.pop(0)
#    cmd.args = _strArr
#    return cmd 

def splitStringEx(msg, keepQuotes = False):
    msg = msg.lstrip(" ").rstrip(" ")
    _len = len(msg)
    offset = 0    
    sep = " "
    quote_char = "\""
    for i in range(0,_len):                
        if offset > 0:
            offset -= 1
            continue
        if msg[i] == quote_char:
            sub = ""    
            for j in range(i,_len): 
                sub += msg[j]
                    
                if (msg[j] == quote_char) and j != i:                    
                    break
                offset=j-i+1
            if not keepQuotes: sub = sub.lstrip(quote_char).rstrip(quote_char)    
            yield sub.lstrip(" ").rstrip(" ")  
        elif msg[i] != sep:
            sub = ""    
            for j in range(i,_len): 
                sub += msg[j]
                if (msg[j] == sep) and j != i:                    
                    break
                offset=j-i+1
            yield sub.lstrip(" ").rstrip(" ")

def UnpackCommand(_str) -> Command:
    
    _strArr = [str(_) for _ in splitStringEx(_str,False)]
    
    cmd = Command()
    cmd.header = _strArr[0]
    _strArr.pop(0)
    cmd.args = _strArr
    return cmd    
#def UnpackCommand(_str) -> Command:
    
#    _strArr = str(_str).split(" ")
#    cmd = Command()
#    cmd.header = _strArr[0]
#    _strArr.pop(0)
#    cmd.args = _strArr
#    return cmd    