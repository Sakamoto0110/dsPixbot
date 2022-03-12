from CommandHandler.Command import Command



def PackCommand(command) -> str:
    result_str = "{0} ".format(command.header)
    for _str in command.args:
        result_str += "{0} ".format(_str)
    return result_str
    
def PackCommandArgs(command) -> str:
    result_str = ""
    for _str in command.args: result_str += "{0} ".format(_str)
    return result_str

def UnpackCommand(_str) -> Command:
    _strArr = str(_str).split(" ")
    cmd = Command()
    cmd.header = _strArr[0]
    _strArr.pop(0)
    cmd.args = _strArr
    return cmd    