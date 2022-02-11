# Gooz CLI
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

### Config Parameters Meanings
| Parameter | Value |
| :---: | :---: |
| Port | COMx |
| Workdir | Work path |
| Username | Any Username |

Work path is related with user. Gooz CLI takes your OS codes from workdir.

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

## Planning Tasks
- [ ] Management your codes which are in MicroPython device
- [ ] Username and Password supporting
- [ ] Run GoozOS from Gooz CLI
- [ ] DevOps Microservices
