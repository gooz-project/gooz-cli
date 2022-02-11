import subprocess
import tempfile
import os
import json

class GoozCLI:
    # Initial Values
    port = ""
    username = ""
    workdir = ""
    template = {"port":"","username":"","workdir":""}
    out = ""
    outputupload = ""
    ignored = ""
    test_out = ""

    def gooz_init(self):
        try:
            f = open('config.json')
            data = json.load(f)
            self.port = data["port"]
            self.username = data["username"]
            self.workdir = data["workdir"]
            return "OK"
        except:
            print("\033[91mconfig.json file not found\033[0m")
            print("\033[91mNeed setup process\033[0m")
            print("\033[94mExample:\033[0m")
            print("\033[94mpython goozcli.py setup\033[0m")
            return "PASS"
    
    def load(self):
        cmd = "ampy -p "+self.port+" ls"
        output = ""
        with tempfile.TemporaryFile() as tempf:
            proc = subprocess.Popen(cmd, stdout=tempf,stderr=tempf,shell=True)
            proc.wait()
            tempf.seek(0)
            output = tempf.read().decode("utf-8")

        self.out = output.splitlines()
    def ls(self):
        print(self.out)
    def upload(self,param):
        clipath = os.getcwd()
        os.chdir(self.workdir)
        print("Workdir -> {}".format(self.workdir))
        with tempfile.TemporaryFile() as tempf:
            proc = subprocess.Popen("dir "+self.workdir+" /B", stdout=tempf,shell=True)
            proc.wait()
            tempf.seek(0)
            output = tempf.read().decode("utf-8")
            self.outputupload = output.splitlines()
        print("These files will be upload")
        f = open(clipath+"\ignored.txt","r",encoding="utf-8")
        self.ignored = f.readlines()
        for i in self.outputupload:
            for a in self.ignored:
                if i == a:
                    self.outputupload.remove(i)
        print(self.outputupload)
        try:
            if param == "-y":
                try:
                    for i in self.outputupload:
                        try:
                            os.system("ampy -p "+self.port+" put "+i)
                            print(f"\U00002714  \033[92m{i} has been uploaded successfully\033[0m")
                        except:
                            print(f"\033[91m{i} could not be uploaded !!\033[0m")
                    print("\U00002705  \033[92mSuccessfully Completed !!!\033[0m")
                except:
                    print("\033[91mThis process haven't completed!!\033[0m")
            else:
                accept = input("\033[93mDo you accept this process? [Y/N] \033[0m")
                if accept == "YES" or accept == "Y" or accept == "yes" or accept == "y" or accept == "Yes":
                    try:
                        for i in self.outputupload:
                            try:
                                os.system("ampy -p "+self.port+" put "+i)
                                print(f"\U00002714  \033[92m{i} has been uploaded successfully\033[0m")
                            except:
                                print(f"\033[91m{i} could not be uploaded !!\033[0m")
                        print("\U00002705  \033[92mSuccessfully Completed !!!\033[0m")
                    except:
                        print("\033[91mThis process haven't completed!!\033[0m")
                else:
                    print("\033[91mProcess has been canceled\033[0m")
        except:
            print("Error")
    def setup(self):
        if os.path.exists("config.json"):
            print("\033[94mConfig file exists. No need setup\033[0m")
        else:
            print("\033[91mconfig.json file not found\033[0m")
            print("\033[94mSetup process has been started\033[0m")
            try:
                self.configuration()
                print("\033[92mSetup has been done successfully\033[0m")
            except:
                print("\033[91mSetup has been failed\033[0m")
    def delete(self,param):
        if param == "-y":
            for i in self.out:
                try:
                    if i[-3:] == ".py":
                        os.system("ampy -p "+self.port+" rm "+i)
                    else:
                        os.system("ampy -p "+self.port+" rmdir "+i)
                    print(f"\U00002714  \033[92m{i} has been deleted successfully\033[0m")
                except:
                    print(f"\033[91m{i} could not be deleted !!\033[0m")
            print("\U00002705  \033[92mSuccessfully Completed !!!\033[0m")
        else:
            accept = input("\033[93mDo you accept this process? [Y/N] \033[0m")
            if accept == "YES" or accept == "Y" or accept == "yes" or accept == "y" or accept == "Yes":
                for i in self.out:
                    try:
                        if i[-3:] == ".py":
                            os.system("ampy -p "+self.port+" rm "+i)
                        elif "." in i:
                            os.system("ampy -p "+self.port+" rm "+i)
                        else:
                            os.system("ampy -p "+self.port+" rmdir "+i)
                        print(f"\U00002714  \033[92m{i} has been deleted successfully\033[0m")
                    except:
                        print(f"\033[91m{i} could not be deleted !!\033[0m")
                print("\U00002705  \033[92mSuccessfully Completed !!!\033[0m")
            else:
                print("\033[91mProcess has been canceled\033[0m")
    def show_parameters(self):
        print("Port -> {}".format(self.port))
        print("Workdir -> {}".format(self.workdir))
        print("Username -> {}".format(self.username))
    
    def get_files(self,param):
        if param == "--all" or param == "-a":
            for i in self.out:
                print(i)
        else:
            cmd = "ampy -p "+self.port+" get "+param
            output = ""
            with tempfile.TemporaryFile() as tempf:
                proc = subprocess.Popen(cmd, stdout=tempf,shell=True)
                proc.wait()
                tempf.seek(0)
                output = tempf.read().decode("utf-8")
            a = output.split("\n")
            f = open("./getfolder"+param,"w+",encoding="utf-8")
            for i in a:
                f.write(i)
            f.close()
            print("\033[92mDEBUG:File has been taken successfully\033[0m")
    
    def test_gooz(self):
        os.system("ampy -p "+self.port+" run test.py")
    
    def configuration(self):
        _port = input("Please enter board port -> ")
        _username = input("Please enter username -> ")
        _workdir = input("Please enter workdir path(OS folders path) -> ")
        #print(_port,_username,_workdir)
        _config = {"port":"","username":"","workdir":""}
        _config["port"] = _port
        _config["username"] = _username
        _config["workdir"] = _workdir
        print("\033[94mConfiguration JSON -> {} \033[0m".format(_config))
        try:
            f = open("config.json","w",encoding="utf-8")
            json.dump(_config,f,indent=4)
            f.close()
            _config = {"port":"","username":"","workdir":""}
            print("\U00002705  \033[92mconfig.json has been changed!\033[0m")
        except:
            print("\U0000274C  \033[91mProcess can not be done!!\033[0m")

    def convert_package(self):
        pkg_template = {"name":"","codes":"","managersnip":""}
        code_template = {"filename":"","code":""}
        cli_path = os.getcwd()
        os.chdir(self.workdir)
        package_name = input("Please enter package name -> ")
        print("Is your package in app or another folder?")
        print("If your package is under app folder please enter only \033[95m'd'\033[0m")
        print("If your package is under another folder please enter folder path")
        print("\033[96mEXAMPLE: /mynewapp/newapp\033[0m")
        print("\033[93mWARNING: Another folder must be under workdir\033[0m")
        package_path = input("Please enter folder -> ")
        if package_path == "d":
            try:
                os.chdir(self.workdir+"/app/"+package_name)
                print(os.listdir())
                files = os.listdir()
                accept=input("\033[93mWARNING: These files convert, do you agree? [y,N]\033[0m -> ")
                if accept == "YES" or accept == "Y" or accept == "yes" or accept == "y" or accept == "Yes":
                    print("\033[92mProcess has been accepted\033[0m")
                    print("\033[94mProcess is doing\033[0m")
                    codes_repo = []
                    for i in files:
                        if i != "manage.py":
                            code_template["filename"] = i
                            f = open(i,"r",encoding="utf-8")
                            codes_file=f.readlines()
                            changed_code_array=[]
                            for i in codes_file:
                                changed_code_array.append(i.replace("\n","pkglineflag"))
                            for i in changed_code_array:
                                print(i)

                            tmp_code = "".join(changed_code_array)
                            tmp_code = tmp_code.replace("\n","pkglineflag")
                            code_template["code"] = tmp_code
                            codes_repo.append(code_template)
                            code_template = {"filename":"","code":""}
                    pkg_template["codes"]=codes_repo
                    pkg_template["name"]=package_name
                    f = open("manage.py","r",encoding="utf-8")
                    manager_snip = f.readlines()
                    manager_snip.insert(0,"pkglineflag")
                    manager_snip[-1] = manager_snip[-1] + "pkglineflag"
                    manager_new_array = []
                    for i in manager_snip:
                        manager_new_array.append(i.replace("\n","pkglineflag"))
                    tmp_manager = "".join(manager_new_array)
                    pkg_template["managersnip"] = tmp_manager
                    os.chdir(cli_path)
                    with open(package_name+".json", "w") as fp:
                        json.dump(pkg_template, fp, indent=4)
                    print("Process has been finished")
                else:
                    print("\033[91mProcess has been canceled\033[0m")    
            except:
                print("\033[91mERROR: This folder can not be reachable\033[0m")
                print("\033[93mWARNING: May be this folder has been deleted\033[0m")
            
        else:
            try:
                os.chdir(self.workdir+package_path+"/"+package_name)
                print(os.listdir())
                files = os.listdir()
                accept=input("\033[93mWARNING: These files convert, do you agree? [y,N]\033[0m -> ")
                if accept == "YES" or accept == "Y" or accept == "yes" or accept == "y" or accept == "Yes":
                    print("\033[92mProcess has been accepted\033[0m")
                    print("\033[94mProcess is doing\033[0m")
                    codes_repo = []
                    for i in files:
                        if i != "manage.py":
                            code_template["filename"] = i
                            f = open(i,"r",encoding="utf-8")
                            codes_file=f.readlines()
                            tmp_code = "".join(codes_file)
                            tmp_code = tmp_code.replace("\n","\\n")
                            code_template["code"] = tmp_code
                            codes_repo.append(code_template)
                            code_template = {"filename":"","code":""}
                    pkg_template["codes"]=codes_repo
                    pkg_template["name"]=package_name
                    f = open("manage.py","r",encoding="utf-8")
                    manager_snip = f.readlines()
                    manager_snip.insert(0,"\\n")
                    manager_snip[-1] = manager_snip[-1] + "\\n"
                    tmp_manager = "".join(manager_snip)
                    tmp_manager = tmp_manager.replace("\n","\\n")
                    pkg_template["managersnip"] = tmp_manager
                    os.chdir(cli_path)
                    with open(package_name+".json", "w") as fp:
                        json.dump(pkg_template, fp, indent=4)
                    print("Process has been finished")
                else:
                    print("\033[91mProcess has been canceled\033[0m")

            except:
                print("\033[91mERROR: This folder can not be reachable\033[0m")
                print("\033[93mWARNING: May be this folder has been deleted\033[0m")

        

