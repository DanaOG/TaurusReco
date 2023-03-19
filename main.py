import re   #Regular expression
from colorama import Fore, Style    #To add styles and colors in the output
import DNS_Lookup
import TCP_Lookup
import UDP_Lookup
import HOST_Lookup
import UserName_Lookup
cyan=Fore.CYAN
red=Fore.RED
yellow=Fore.YELLOW
green=Fore.GREEN
blue=Fore.BLUE
black=Fore.BLACK
white=Fore.WHITE
magenta=Fore.MAGENTA
Lcyan=Fore.LIGHTCYAN_EX
Lred=Fore.LIGHTRED_EX
Lyellow=Fore.LIGHTYELLOW_EX
Lgreen=Fore.LIGHTGREEN_EX
Lblue=Fore.LIGHTBLUE_EX
Lblack=Fore.LIGHTBLACK_EX
Lwhite=Fore.LIGHTWHITE_EX
Lmagenta=Fore.LIGHTMAGENTA_EX
reset=Style.RESET_ALL


#print(f"{cyan}Cyan {red}red {yellow}yellow {green}green {blue}blue {black}black {white}white {magenta}magenta {reset}")
#print(f"{Lcyan}Lcyan {Lred}Lred {Lyellow}Lyellow {Lgreen}Lgreen {Lblue}Lblue {Lblack}Lblack {Lwhite}Lwhite {Lmagenta}Lmagenta {reset}")

print(f"""{Lyellow} 
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░
{Lred}
████████╗░█████╗░██╗░░░██╗██████╗░██╗░░░██╗░██████╗██████╗░███████╗░█████╗░░█████╗░
╚══██╔══╝██╔══██╗██║░░░██║██╔══██╗██║░░░██║██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗
░░░██║░░░███████║██║░░░██║██████╔╝██║░░░██║╚█████╗░██████╔╝█████╗░░██║░░╚═╝██║░░██║
░░░██║░░░██╔══██║██║░░░██║██╔══██╗██║░░░██║░╚═══██╗██╔══██╗██╔══╝░░██║░░██╗██║░░██║
░░░██║░░░██║░░██║╚██████╔╝██║░░██║╚██████╔╝██████╔╝██║░░██║███████╗╚█████╔╝╚█████╔╝
░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝░╚═════╝░╚═════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░
{reset}
""") #Printing the tool name

print(f"""{white}
                        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                        ░░░░░████░░░░░░░░░░░░░░░████░░░░░
                        ░░░░███░░░░░░░░░░░░░░░░░░░███░░░░
                        ░░░███░░░░░░░░░░░░░░░░░░░░░███░░░
                        ░░███░░░░░░░░░░░░░░░░░░░░░░░███░░
                        ░███░░░░░░░░░░░░░░░░░░░░░░░░░███░
                        ████░░░░░░░░░░░░░░░░░░░░░░░░░████
                        ████░░░░░░░░░░░░░░░░░░░░░░░░░████
                        ██████░░░░░░░███████░░░░░░░██████
                        █████████████████████████████████
                        █████████████████████████████████
                        ░███████████████████████████████░
                        ░░████░███████████████████░████░░
                        ░░░░░░░███▀███████████▀███░░░░░░░
                        ░░░░░░████──▀███████▀──████░░░░░░
                        ░░░░░░█████───█████───█████░░░░░░
                        ░░░░░░███████▄█████▄███████░░░░░░
                        ░░░░░░░███████████████████░░░░░░░
                        ░░░░░░░░█████████████████░░░░░░░░
                        ░░░░░░░░░███████████████░░░░░░░░░
                        ░░░░░░░░░░█████████████░░░░░░░░░░           
                        ░░░░░░░░░░░███████████░░░░░░░░░░░
                        ░░░░░░░░░░███──▀▀▀──███░░░░░░░░░░
                        ░░░░░░░░░░███─█████─███░░░░░░░░░░
                        ░░░░░░░░░░░███─███─███░░░░░░░░░░░
                        ░░░░░░░░░░░░█████████░░░░░░░░░░░░
                        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{reset}
""")#Printing the tool logo

#
# ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
web_name_pattern=re.compile("^(www\.)?([a-zA-Z0-9]+(-?[a-zA-Z0-9])*\.)+(com)?$")


def menu():
    print(f"{Lyellow}\n\t\t\t░░░░░░░░░░░ 𝑊ℎ𝑎𝑡 𝑎𝑟𝑒 𝑦𝑜𝑢 𝑙𝑜𝑜𝑘𝑖𝑛𝑔 𝑓𝑜𝑟? ░░░░░░░░░░░ {reset}")
    print(f"""{red}\t\t\t\t\t\tPlease enter the choice number {reset} 
                        1 ╠═══IP Address Scan═══╣
                        2 ╠═Domain Name Look-up═╣
                        3 ╠══UserName Look-up═══╣
                        4 ╠════════Exit═════════╣""")

# def IP_Address_Scan_Menu():
#     print(Lyellow + ""
# "                --------------------------------------------------\n"
# "                Please enter the type of IP Scan you want to run:\n"
# "                --------------------------------------------------"
#           + reset)
#     print(red + """
#                Δ To TCP Scan Well Known Ports Enter (1)
#                Δ To UDP Scan Well Known Ports Enter (2)
#                Δ Back to main menu                  (3)
#
#     """ + reset)


def IP_Address_Scan_Menu():
    print(f"{Lyellow}\n░░░░░░░░░░░ Please enter the type of IP Scan you want to run ░░░░░░░░░░░ {reset}")
    print(f"""{red}Please enter the choice number {reset} 
1 ╠════To TCP Scan Well Known Ports═══╣
2 ╠════To UDP Scan Well Known Ports═══╣
3 ╠════════To Discover Host═══════════╣
4 ╠════════Back to main menu ═════════╣""")


def IP_Address_Scan():

    while True:
        IP_Address_Scan_Menu()
        choice=input(Lyellow+"Please Choose one option "+reset)
        if choice=="1":
           TCP_Lookup.valid_ipaddress_TCP()
        elif choice =="2":
            UDP_Lookup.valid_ipaddress_UPD()
        elif choice=='3':
            HOST_Lookup.valid_ipaddress_Host()
        elif choice == "4":
            main_method()
        else:
            print(red+"invalid input, please try again. "+reset)




def Domain_Name():
    # Make sure that the input is valid DNS
    while True:
        name= input(f"{Lyellow}Enter the web name you want to scan: {reset}")
        if web_name_pattern.search(name):
            print(f"The domain name {name} is valid!")
            break
        else:
            print(f"{red}The domain name {Lwhite}{name}{red} is invalid, please try again with this format (DomainName.com) {reset}\n")

    # Generate a report that contains all the information provided by the tool
    file=open(f"{name}_DNS.txt", "a+")
    file.write(f"░░░░░░░░░░░░░░░░░░  The results of scanning ({name}) ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")

    # Call the functions that will do the DNS lookup and save the output in the file created
    DNS_Lookup.FindRecords(name, file)
    DNS_Lookup.Find_DNS_Info(name, file)

    # Now the file contain all the information, we don't need it so close it
    file.close()
def User_Name():
    while True:
        username=input(Lyellow+"Please Enter Github Username To Scan \nEnter 4 to return to the main menu"+reset)
        if username=="4":
            main_method()
        else:
            UserName_Lookup.gitinformation(username)



def main_method():
    while True:
        menu()
        choice=input()
        if choice =="1":    # IP Address Scan
            IP_Address_Scan()
        elif choice=="2":   # Domain Name Look-up
            Domain_Name()
        elif choice == "3":
            User_Name()
        elif choice =="4":  # Exit
            print(f"{Lyellow}⌧⌧⌧⌧ Thank you for using TaurusReco!!⌧⌧⌧⌧{reset}")
            quit()
        else:               # Wrong input
            print(f"{Lred}Invalid input! Please try again...{reset}")


main_method()