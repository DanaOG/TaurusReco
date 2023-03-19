import re
import nmap
import pyfiglet
import datetime as datetime
from colorama import *
from colorama import Fore


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
#variables
ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
subnet_pattern = re.compile("[0-9]{2,3}")
nm=nmap.PortScanner()

def time_start():
    time_now1 = datetime.datetime.now()
    current_time1 = time_now1.strftime("%H:%M:%S")
    print(red1+"Time started: {}".format(current_time1)+reset)

def time_finish():
    time_now2=datetime.datetime.now()
    current_time2 = time_now2.strftime("%H:%M:%S")
    print(red1+"Time Finished: {}".format(current_time2)+reset)

#check validate of Ip address
def valid_ipaddress_Host():
    while True:
        ip_add_entered = input(Lyellow + "\nPlease enter the ip address that you want to scan: " + reset)
        if ip_add_pattern.search(ip_add_entered):
            print(LightC + f"{ip_add_entered} is a valid ip address" + reset)
            Host_Scanning(ip_add_entered)
            break
        else:
            print(red1 + "Invalid Ip address please Try Again ..... " + reset)
def Host_Scanning(ip_addr):
    subnet = input(Lyellow +"Plaese Enter Subnet Mask: "+reset)
    while True:
        if subnet_pattern.search(subnet):
            print(LightC + f"{subnet} is a valid Subnet mask" + reset)
            break
        else:
            print(red1 + "Invalid Subnet please Try Again ..... " + reset)

    network = ip_addr + '/' + subnet  # merge the IP wit the subnet mask
    print(LightC+"═"*25 + " Starting Scan " + str(network) + "═"*25+reset )
    nm.scan(hosts=network, arguments='-sn')  # -sn to discover alive hosts
    hostList = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]  # save result in a list [Hostnumber ,IP,STATE]
    j = 0
    for i in hostList:
        j = j + 1
        print(LightC+'[' + "Host "+ str(j) + ']'+reset + LightC+'  IP: ' +reset+ i[0] + LightC+'  State: ' +reset+  i[1])
    print(f"there are{LightC} {len(hostList)} {reset} hosts in the network {LightC}{ip_addr}/{subnet}{reset}\n")  # print total devices


