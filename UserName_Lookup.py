import os
import requests as res
import json
import re
from colorama import *
from colorama import Fore
import socket

#colors
LightC=Fore.LIGHTCYAN_EX
cyan=Fore.CYAN
LightB=Fore.LIGHTBLUE_EX
red=Fore.RED
red1=Fore.LIGHTRED_EX
perp=Fore.LIGHTMAGENTA_EX
Black=Fore.LIGHTBLACK_EX
bold=Style.BRIGHT
reset=Style.RESET_ALL
Lyellow=Fore.LIGHTYELLOW_EX
Lwhite=Fore.LIGHTWHITE_EX

def gitinformation(username):
	response = res.get("https://api.github.com/users/" + username).text
	data = json.loads(response)
	if str(data['name'])=="None":
		print(red1+"This Username not included in database try "+reset)
	else :
		print(LightC + "Dumping Sensitive information from Github" + reset)
		os.system('tput setaf 9')
		print(LightB + "Name : " + reset, str(data['name']))
		print(LightB + "Location : " + reset, str(data['location']))
		print(LightB + "Website : " + reset, str(data['blog']))
		print(LightB + "Number of public GitHub Repository : " + reset, str(data['public_repos']))
		print(LightB + "Number of public gist Repository : " + reset, str(data['public_gists']))
		response1 = res.get("https://api.github.com/users/%s/events" % (username))
		expression1 = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}', response1.text)
		if expression1 == []:
			print(red1 + "No Emails can found " + reset)
		else:
			print(LightB + "Extracting Email data:\n" + reset, expression1)


