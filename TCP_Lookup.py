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
Lwhite=Fore.LIGHTWHITE_EX
Lyellow=Fore.LIGHTYELLOW_EX
#variables
ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
open_ports=re.compile("[0-9]+:")
port_min = 0
port_max = 65535
find_open_ports_tcp=''
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


def valid_ipaddress_TCP():
    while True:
        ip_add_entered = input(Lyellow+bold+"\nPlease enter the ip address that you want to scan: "+reset)
        if ip_add_pattern.search(ip_add_entered):
            print(LightC+f"{ip_add_entered} is a valid ip address"+reset)
            # general_tcp_scanning(ip_add_entered)
            Tcp_Scanning(ip_add_entered)
            break
        else:
            print(red1+"Invalid Ip address please Try Again ..... "+reset)





def general_tcp_scanning(ip):
    print(LightC + bold + "═" * 20 + " General Scanning " + "═" * 20 + reset)
    result = nm.scan(hosts=ip, arguments=f"-sS  ")
    scanresult = nm.scaninfo()
    os_scan = nm.scan(hosts=ip, arguments=" -O ")
    print(LightC + bold + "═" * 20 + " General Scanning " + "═" * 20 + reset)
    print('[name]: ' + LightB +result['scan'][ip]['hostnames'][0]['name'] + reset+'\n[operating system]: '+ LightB+os_scan['scan'][ip]['osmatch'][0]['name']
          +reset +'\n[state]: ' + LightB +result['scan'][ip]['status'][
              'state'] + reset+'\n[Reason]: ' + LightB+result['scan'][ip]['status']['reason'] + reset)

    print("[method] : " +LightB+ scanresult['tcp']['method'] + reset+'\n[list of services] : ' + LightB +scanresult['tcp'][
        'services'] + reset+'\n[Total Hosts: ]' + LightB+result['nmap']['scanstats']['totalhosts'] + reset+'\n[up hosts]: ' +
          result['nmap']['scanstats']['uphosts'] + reset+'\n[down hosts]: ' +LightB+ result['nmap']['scanstats']['downhosts']+reset)





def Tcp_Scanning(ip):
    while True:
        print(red1+bold+"\n"+"═" * 25 + " Please choose a number " + "═" * 25+reset)
        choice = input( Lwhite+
            "1 ╠═══════════Scan all the ports═══════════╣\n"
            "2 ╠═══════Scan most popular 100 ports══════╣\n"
            "3 ╠════════To choose specific range════════╣\n"
            "4 ╠═══════════Display Service name═════════╣\n"
            "5 ╠═══════To return to the main menu═══════╣\n"+reset)
        if choice == '1':  # To scan all the ports
            print(LightC+"═"*25 + " Starting Scan " + str(ip) + "═"*25+reset )
            time_start()
            # general_tcp_scanning(ip)
            result = nm.scan(hosts=ip, arguments=f"-sS -p- ")
            # to find open ports number
            find_open_ports_tcp = open_ports.findall(str(result['scan'][ip]['tcp']))
            # to find open ports number without :
            for i in range(len(find_open_ports_tcp)):
                find_open_ports_tcp[i] = str(find_open_ports_tcp[i]).replace(':', '')
            # to list  all open  ports
            print(Black+"═" * 50 + '\nList of open ports:'+reset)
            for port in find_open_ports_tcp:
                print(f'Port {port}:')
                port = int(port)
                print('[name]: ' + LightB+result['scan'][ip]['tcp'][port]['name'] + reset+'\n[state]: ' + LightB+result['scan'][ip]['tcp'][port]['state'] + reset+'\n[Reason]: ' + LightB+result['scan'][ip]['tcp'][port]['reason'] + '\n'+reset)
                print(Black+"═" * 50+reset)
            time_finish()

        elif choice == '2':  # To scan most popular 100 ports
            print(LightC+"═"*25 + " Starting Scan " + str(ip) + "═"*25+reset )
            time_start()
            result = nm.scan(hosts=ip, arguments=f"-sS -F ")
            # general_tcp_scanning(ip)
            # to find open ports number
            find_open_ports_tcp = open_ports.findall(str(result['scan'][ip]['tcp']))

            # to find open ports number without :
            for i in range(len(find_open_ports_tcp)):
                find_open_ports_tcp[i] = str(find_open_ports_tcp[i]).replace(':', '')
            # to list  all open  ports
            print(Black+"═" * 50 + '\nList of open ports:'+reset)
            for port in find_open_ports_tcp:
                print(cyan+f'Port {port}:'+reset)
                port = int(port)
                print('[name]: ' +LightB +result['scan'][ip]['tcp'][port]['name'] + reset+'\n[state]: '+ LightB + result['scan'][ip]['tcp'][port]['state'] + reset+'\n[Reason]: ' +LightB+ result['scan'][ip]['tcp'][port]['reason'] + '\n'+reset)
                print(Black+"═" * 50+reset)
            time_finish()

        elif choice == '3':  # To choose specific range
            # 45.33.32.156
            print(LightC+"═"*25 + " Starting Scan " + str(ip) + "═"*25+reset )
            time_start()
            while True:
                print(LightC+"Please enter the range of ports you want to scan in format: <int>-<int> (ex: 60-120)"+reset)
                port_range = input("Enter port range: ")
                port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))
                if port_range_valid:
                    port_min = int(port_range_valid.group(1))
                    port_max = int(port_range_valid.group(2))
                    break
                else:
                    print(red1 + "Invalid port range please Try Again ..... " + reset)

            print(Black+"═" * 50 + '\nList of open ports:'+reset)
            # to List all  ports Info
            for port in range(port_min, port_max + 1):
                try:
                    result = nm.scan(hosts=ip, arguments=f"-sS -p {port}")

                    print(cyan+f'Port {port}:'+reset)
                    port = int(port)
                    print('[name]: ' +LightB+ result['scan'][ip]['tcp'][port]['name'] +reset+ '\n[state]: ' +LightB+ result['scan'][ip]['tcp'][port]['state'] + reset + '\n[Reason]: ' +LightB+ result['scan'][ip]['tcp'][port]['reason'] + '\n'+reset)
                    print(Black+"*" * 50+reset)
                except Exception:
                    pass
            time_finish()
        elif choice == '4':
            port = input(LightC + 'Enter port number: ' + reset)
            protocolname = 'tcp'
            print(cyan + "Port: %s => service name: %s" % (port, socket.getservbyport(int(port), protocolname)) + reset)

        elif choice == '5':
            break

        else:
            print(red1+ "Please Enter a Correct Option " + reset)



# general_tcp_scanning('45.33.32.156')