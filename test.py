import gooz_engine
import dev.gooz_thread
import os
from system.config import find_value

username = find_value('system/username')
password = find_value('system/password')
test_commands = [
    "ls",
    "pwd",
    "usage",
    "wifi connect asd asd",
    "wifi on",
    "wifi status",
    "wifi ls",
    "ifconfig",
    "curl http:example",
    "shutdown"
]
login_flag = True

while(login_flag):
    success = 0
    for msg in test_commands:
        print("\033[96mTEST DEBUG: {} command\033[0m".format(msg))
        cmd_list = gooz_engine.command_analyzator(msg)
        try:
            gooz_engine.add_run_commands(cmd_list)
            print("\033[92mDEBUG: {} Test Success\033[0m".format(msg))
            success += 1
        except:
            print("\033[91mERROR: {} Test Failed\033[0m".format(msg))
        gooz_engine.history.append(cmd_list)
    
    if cmd_list[0] == "shutdown":
        os.chdir("/")
        print("System will be shutdown")
        print("\033[93mRESULT: {}/{} Success Test\033[0m".format(success,len(test_commands)))
        dev.gooz_thread.exit_flag = 1
        break
