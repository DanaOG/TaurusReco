import re
import nmap
import datetime as datetime
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
#variables
ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
open_ports=re.compile("[0-9]+:")
port_min = 0
port_max = 65535
find_open_ports_udp=''
open_ports_udp=[]
nm=nmap.PortScanner()


#Calculate the time using datetime package
def time_start():
    time_now1 = datetime.datetime.now()
    current_time1 = time_now1.strftime("%H:%M:%S")
    print(red1+"Time started: {}".format(current_time1)+reset)

def time_finish():
    time_now2=datetime.datetime.now()
    current_time2 = time_now2.strftime("%H:%M:%S")
    print(red1+"Time Finished: {}".format(current_time2)+reset)

#check validate of Ip address
def valid_ipaddress_UPD():
    while True:
        ip_add_entered = input(Lyellow + "\nPlease enter the ip address that you want to scan: " + reset)
        if ip_add_pattern.search(ip_add_entered):
            print(LightC + f"{ip_add_entered} is a valid ip address" + reset)
            general_udp_scanning(ip_add_entered)
            UDP_Scanning(ip_add_entered)
            break
        else:
            print(red1 + "Invalid Ip address please Try Again ..... " + reset)


def general_udp_scanning(ip):
    result = nm.scan(hosts=ip, arguments=f"-sU  ")
    scanresult = nm.scaninfo()
    # os_scan = nm.scan(hosts=ip, arguments=" -O ")
    print(LightC + bold + "═" * 20 + " General Scanning " + "═" * 20 + reset)
    print('[name]: ' + LightB + result['scan'][ip]['hostnames'][0]['name'] + reset
          + '\n[state]: ' + LightB + result['scan'][ip]['status'][
              'state'] + reset + '\n[Reason]: ' + LightB + result['scan'][ip]['status']['reason'] + reset)

    print("[method] : " + LightB + scanresult['udp']['method'] + reset + '\n[list of services] : ' + LightB +
          scanresult['udp'][
              'services'] + reset + '\n[Total Hosts]:' + LightB + result['nmap']['scanstats'][
              'totalhosts'] +reset+ '\n[up hosts]: ' +LightB+
          result['nmap']['scanstats']['uphosts'] + reset + '\n[down hosts]: ' + LightB + result['nmap']['scanstats'][
              'downhosts'] + reset)


#UDP Method
def UDP_Scanning(ip):
    while True:
        print(Lyellow+bold+"═" * 25 + " Please choose a number " + "═" * 25+reset)
        choice = input( Lwhite+
            "1 ╠════To choose specific range═══╣\n"
            "2 ╠════Return to the main menu════╣\n"+reset)

       #scan specific ports
        if choice == '1':
            print(LightC+"═"*25 + " Starting Scan " + str(ip) + "═"*25+reset )
            time_start()
            while True:
                print(LightB+"Please enter the range of ports you want to scan in format: <int>-<int> (ex: 60-120)"+reset)
                port_range = input(cyan+"Enter port range: "+reset)
                port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))
                if port_range_valid:
                    port_min = int(port_range_valid.group(1))
                    port_max = int(port_range_valid.group(2))
                    break
                else:
                    print(red1 + "Invalid Port Number please Try Again ..... " + reset)

            print(Black+"═" * 50 + '\nList of open ports:'+reset)
            # to List all  ports Info
            for port in range(port_min, port_max + 1):
                try:
                    result = nm.scan(hosts=ip, arguments=f"-sU -p {port}")

                    print(cyan+f' Port {port}:'+reset)
                    port = int(port)
                    print('[name]: ' +LightB +result['scan'][ip]['udp'][port]['name'] + reset+'\n[state]: '+LightB +result['scan'][ip]['udp'][port]['state'] + reset+'\n[Reason]: ' + LightB+result['scan'][ip]['udp'][port]['reason'] + '\n'+reset)
                    print(Black+"═" * 50+reset)
                except Exception:
                    pass
            time_finish()

        elif choice == '2':
            break

        # error handling
        else:
            print(red + "Please Enter a Correct Option " + reset)

