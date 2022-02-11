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
### Config Part
Firstly config.json have to be configured
```
{
    "port": "COM3",
    "username": "User1",
    "workdir": "Workpath"
}
```
These values will be changed by user

### Config Part on CLI
Config parameters can be changed via Gooz CLI commands
```
python3 gooz.py config 
```
or
```
python gooz.py config 
```
For changing specific config parameter,
```
python3 gooz.py config username
```
```
python3 gooz.py config workdir 
```
```
python3 gooz.py config port 
```

### Config Parameters Meanings
| Parameter | Value |
| :---: | :---: |
| Port | COMx |
| Workdir | Work path |
| Username | Any Username |

Work path is related with user. Gooz CLI takes your OS codes from workdir.

## Upload
![Success Upload](https://github.com/gooz-project/gooz-cli/blob/main/uploadedGooz.PNG)<br/>
Upload your codes to your MicroPython device<br/>
**IMPORTANT : This process will upload everything from your MicroPython device**
```
python3 gooz.py upload
```
or
```
python3 gooz.py upload -y
```


## Delete
![Success Delete](https://github.com/gooz-project/gooz-cli/blob/main/deleteGooz.PNG)<br/>
Delete your codes from your MicroPython device<br/>
**IMPORTANT : This process will delete everything from your MicroPython device**
```
python3 gooz.py delete
```
or
```
python3 gooz.py delete -y
```

## Planning Tasks
- [ ] Management your codes which are in MicroPython device
- [ ] Username and Password supporting
- [ ] Run GoozOS from Gooz CLI
- [ ] DevOps Microservices
