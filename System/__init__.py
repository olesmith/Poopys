import subprocess,os

def Command_Exec(commands,cd=None):
    cwd=os.getcwd()
    if (cd!=None):
        os.chdir(cd)
        
    try:
        output=os.system(" ".join(commands))
    except:
        output="Warning! Unable to execute system command: "+" ".join(commands)
        
    if (cd!=None):
        os.chdir(cwd)
        
    return output

def Command_Pipe(commands):
    output=""
    try:
        output=subprocess.check_output(commands)
    except:
        output="Warning! Unable to pipe system command: "+" ".join(commands)
        
    return output
