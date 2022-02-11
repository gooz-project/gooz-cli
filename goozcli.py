import sys
from goozlib import GoozCLI

process = GoozCLI()
flag = process.gooz_init()
try:
    process.load()
    if flag == "OK":
        print("\033[92mDEBUG: Your device has been connected successfully\033[0m")
    else:
        raise Exception("ERROR")
except:
    print("\033[91mERROR: Your device can not be reachable\033[0m")
if sys.argv[1] == "ls":
    process.ls()
elif sys.argv[1] == "config":
    process.configuration()
elif sys.argv[1] == "delete":
    try:
        process.delete(sys.argv[2])
    except:
        process.delete("-")
elif sys.argv[1] == "upload":
    try:
        process.upload(sys.argv[2])
    except:
        process.upload("-")
elif sys.argv[1] == "param":
    process.show_parameters()
elif sys.argv[1] == "convert":
    process.convert_package()
elif sys.argv[1] == "get":
    process.get_files(sys.argv[2])
elif sys.argv[1] == "test":
    process.test_gooz()
    print("\033[93mTest process has been done\033[0m")
elif sys.argv[1] == "setup":
    process.setup()