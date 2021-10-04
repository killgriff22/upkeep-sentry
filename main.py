from os import system as sys
from platform import system as osver
os = osver()
packages = ["colorama","requests","--update pip"]
try:
  from requests import get as get
  from colorama import Fore,init,Back
except:
  if os == "Linux":
    print("please install required packages\ncolorama\nrequests")
    exit()
  elif os == "Darwin":
    for package in packages: 
      sys("pip3 install " + package)
  elif os == "Windows":
    for package in packages:
      sys("pip install " + package)
  from requests import get as get
  from colorama import Fore,init,Back
init()
from time import sleep
def checkforupdates():
  if get("https://raw.githubusercontent.com/killgriff22/upkeep-sentry/master/main.py").text() != open("main.py","r").read():
    open("update.py","w").write("import requests\nopen(\"main.py\",\"w\").write(requests.get(\"https://raw.githubusercontent.com/killgriff22/upkeep-sentry/master/main.py\").text())\nimport os\nos.system(\"python3 main.py\")")
    sys("python update.py")
amt = int(input(Fore.CYAN+Back.BLACK+"please write the amount of servers that need to be upkept\n"))
iparr = []
for x in range(amt):
  iparr.append(input(Fore.CYAN+Back.BLACK+"please input the ip or domain to be upkept\n"))
  print(Fore.RESET,Back.RESET)
while True:
  checkforupdates()
  sleep(3)
  for i in range(len(iparr)):
    ip = iparr[i]
    if ip[0]+ip[1]+ip[2]+ip[3]+ip[4] not in ["https", "http:"]:
      ip = "http://" + ip
    try:
      r=get(ip)
    except:
      print(Fore.BLACK,Back.RED,"failed to connect to " + ip + " please check the server or your internet connection",Fore.RESET,Back.RESET)
    if r.status_code != 200:
      print(Fore.BLACK,Back.RED,ip + " has returned " + str(r.status_code) + " as its response! please check on the server!!!!!",Fore.RESET,Back.RESET)
    else:
      print(Fore.GREEN,Back.BLACK,ip + " has been upkept!")