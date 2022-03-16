# Gooz CLI
## New Features
- Engine
GoozOS has been rewritten with a brand new engine. Thus, it has been made more performance and dynamic. The engine can be viewed from the link here : https://github.com/gooz-project/goozengine
- New Package Formula for New Engine
Along with the changes in the engine, there were some differences in the manifest files required for package installation. All these glitches have been fixed in the new version of GoozCLI.
- Backend Converter for WebGooz
Thanks to the WebGooz package, you can now implement your IoT API applications with GoozOS. It has a number of features to simplify its complex and powerful structure and to benefit more clearly from its efficiency. One of them is that easy backend functions can be developed. The JSON files that will be needed can be developed with the new version of GoozCLI.
## Prerequisites
- Adafruit-Ampy Module
### How To Install Prerequisites
```
pip install adafruit-ampy
```
or
```
pip3 install adafruit-ampy
```
### How To Test Prerequisites
Using CMD, PowerShell or Bash Terminal
```
ampy --help
```
## Gooz CLI
### Setup
Before you start using Gooz CLI, you need to do the setup process. This process is quite easy and the following process needs to be followed.
```
python3 goozcli.py setup
```
At the initial installation stage, it will be sufficient to do the following.
```python
config.json file not found
Need setup process     
Example:
python goozcli.py setup
ERROR: Your device can not be reachable
config.json file not found    
Setup process has been started
Please enter board port -> COM6
Please enter username -> Gorki
Please enter workdir path(OS folders path) -> C:\GoozOS
Configuration JSON -> {'port': 'COM6', 'username': 'Gorki', 'workdir': 'C:\\GoozOS'} 
✅  config.json has been changed!
Setup has been done successfully
```
After a successful setup, config.json will be visible in the directory where Gooz CLI is located.

### Config Parameters Meanings
| Parameter | Value |
| :---: | :---: |
| Port | COMx |
| Workdir | Work path |
| Username | Any Username |

Work path is related with user. Gooz CLI takes your OS codes from workdir.

### Changing Config Parameters
If you are working in a different development environment or for different situations, you can make changes to the config.json file.
```bash
python3 goozcli.py config
```
Ex Usage:
```python
DEBUG: Your device has been connected successfully
Please enter board port -> COM6
Please enter username -> Gorki
Please enter workdir path(OS folders path) -> D:\Gooz\GoozNew
Configuration JSON -> {'port': 'COM6', 'username': 'Gorki', 'workdir': 'D:\\Gooz\\GoozNew'} 
✅  config.json has been changed!
```

## Viewing Files on the Board
If you want to view the files inside your board after connecting it, you can use the command below.
```
python3 goozcli.py ls
```
Ex Output:
```
DEBUG: Your device has been connected successfully
['/app', '/dev', '/docs', '/gooz_engine.py', '/lib', '/main.py', '/system']
```
## Upload
Upload your codes to your MicroPython device<br/>
**IMPORTANT : This process will upload everything from your MicroPython device**
```
python3 goozcli.py upload
```
or
```
python3 goozcli.py upload -y
```
## Delete
Delete your codes from your MicroPython device<br/>
**IMPORTANT : This process will delete everything from your MicroPython device**
```
python3 goozcli.py delete
```
or
```
python3 goozcli.py delete -y
```
## Convert Gooz Packages to JSON
You can convert the packages you write into JSON files that can be read by Gooz OS via Gooz CLI.
Ex:
```
python3 goozcli.py convert
```
Ex Output:
```
DEBUG: Your device has been connected successfully
Please enter package name -> webgooz
Is your package in app or another folder?
If your package is under app folder please enter only 'd'       
If your package is under another folder please enter folder path
EXAMPLE: /mynewapp/newapp
WARNING: Another folder must be under workdir
Please enter folder -> d
['gooz_web.py', 'manage.py']
WARNING: These files convert, do you agree? [y,N] -> 
```
## Test Your Gooz OS
Gooz OS included in the board can be tested via Gooz CLI. For this, test.py must be located in the folder where Gooz CLI is installed. The sample test file is in the repo.
```
python3 goozcli.py test
```
Ex Output:
```
DEBUG: ifconfig Test Success
TEST DEBUG: curl http:example command
ERROR: curl http:example Test Failed
TEST DEBUG: shutdown command

DEBUG: shutdown Test Success
System will be shutdown
RESULT: 9/10 Success Test
Test process has been done
```
## Get Specific File
You can pull any file you want from Gooz OS to your media via Gooz CLI.
```
python3 goozcli.py get [FILE_NAME]
```
## WebGooz Backend Converter
You can create backend manifests for WebGooz Package
```shell
python goozcli.py backend [BACKEND_PYTHON_FILE_PATH]
```
## Planning Tasks
- [ ] Management your codes which are in MicroPython device
- [ ] Username and Password supporting
- [ ] Run GoozOS from Gooz CLI
- [ ] DevOps Microservices
