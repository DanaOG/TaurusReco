import dns.resolver
from colorama import Fore, Style    #To add styles and colors in the output
import subprocess   #To execute the command on terminal
import re   #Regular expression
import os

#Will be used to query DNS to get information about specific record
DNSresolver=dns.resolver.Resolver()

#Define colors to be used in printing the output
LightC=Fore.LIGHTCYAN_EX
cyan=Fore.CYAN
lightB=Fore.LIGHTBLUE_EX
red=Fore.RED
bold=Style.BRIGHT
reset=Style.RESET_ALL

# Regex
status_pattern=re.compile("\[[^\[]*\]", re.MULTILINE)

#This method will find all DNS records, print it on the screen
# and write the output to a file, there is "###" after each writing to the file statement
def FindRecords(name, file):
    #Find all IPv4 associated with the DNS (Record A)
    IPv4=DNSresolver.resolve(name, "A")
    print(LightC+bold+"\n\n█████ Record 'A' █████"+reset)
    file.write(f"█████ Record 'A' █████\n") ###
    if IPv4:
        print(cyan+f"There is/are {len(IPv4)} IPv4 addresses, which is/are:"+reset)
        file.write(f"There is/are {len(IPv4)} IPv4 addresses, which is/are:\n") ###
        number=0
        for ip in IPv4:
            number+=1
            print(f"IPv4 [{number}] is: {lightB}{ip.to_text()}{reset}")
            file.write(f"IPv4 [{number}] is: {ip.to_text()}\n") ###
    else:
        print(red+"There is no IPv4 associated with this DNS")
        file.write(f"There is no IPv4 associated with this DNS \n") ###



    #Find all IPv6 associated with the DNS (Record AAAA)
    IPv6 = DNSresolver.resolve(name, "AAAA", raise_on_no_answer=False)
    print(LightC+bold+"\n\n█████ Record 'AAAA' █████"+reset)
    file.write(f"█████ Record 'AAAA' █████\n")  ###
    if IPv6:
        print(cyan+f"There is/are {len(IPv6)} IPv6 addresses, which is/are:"+reset)
        file.write(f"There is/are {len(IPv6)} IPv6 addresses, which is/are:\n")  ###
        number=0
        for ip in IPv6:
            number+=1
            print(f"IPv6 [{number}] is: {lightB}{ip.to_text()}{reset}")
            file.write(f"IPv6 [{number}] is: {ip.to_text()}\n")  ###
    else:
        print(red+"There is no IPv6 associated with this DNS")
        file.write(f"There is no IPv6 associated with this DNS \n")  ###



    #Find all Canonical names associated with the DNS (Record CNAME)
    CNAME = DNSresolver.resolve(name, "CNAME", raise_on_no_answer=False)
    print(LightC+bold+"\n\n█████ Record 'CNAME' █████"+reset)
    file.write(f"█████ Record 'CNAME' █████\n") ###
    if CNAME:
        print(cyan+f"There is/are {len(CNAME)} Canonical names, which is/are:")
        file.write(f"There is/are {len(CNAME)} Canonical names, which is/are:\n") ###
        number=0
        for ip in CNAME:
            number+=1
            print(f"Canonical name [{number}] is: {lightB}{ip.to_text()}{reset}")
            file.write(f"Canonical name [{number}] is: {ip.to_text()}\n") ###
    else:
        print(red+"There is no Canonical names associated with this DNS")
        file.write(f"There is no Canonical names associated with this DNS \n") ###



    #Find all Mail Exchangers associated with the DNS (Record MX)
    MX = DNSresolver.resolve(name, "MX", raise_on_no_answer=False)
    print(LightC+bold+"\n\n█████ Record 'MX' █████"+reset)
    file.write(f"█████ Record 'MX' █████\n")  ###
    if MX:
        print(cyan+f"There is/are {len(MX)} Mail servers to handle {name} emails, which is/are:"+reset)
        file.write(f"There is/are {len(MX)} Mail servers to handle {name} emails, which is/are:\n") ###
        number=0
        for ip in MX:
            number+=1
            print(f"Mailserver [{number}] is: {lightB}{ip.to_text()}{reset}")
            file.write(f"Mailserver [{number}] is: {ip.to_text()}\n") ###
    else:
        print(red+"There is no Mail Servers associated with this DNS")
        file.write(f"There is no Mail Servers associated with this DNS \n") ###



    #Find all nameservers associated with the DNS (Record NS)
    NS = DNSresolver.resolve(name, "NS", raise_on_no_answer=False)
    print(LightC+bold+"\n\n█████ Record 'NS' █████"+reset)
    file.write(f"█████ Record 'NS' █████\n")  ###
    if NS:
        print(cyan+f"Ther is/are {len(NS)} name servers to store a copy of the original DNS records in {name}, which is/are:"+reset)
        file.write(f"There is/are {len(NS)} name servers to store a copy of the original DNS records in {name}, which is/are:\n") ###
        number=0
        for ip in NS:
            number+=1
            print(f"nameserver[{number}] is: {lightB}{ip.to_text()}{reset}")
            file.write(f"nameserver [{number}] is: {ip.to_text()}\n")  ###
    else:
        print(red+"There is no name servers associated with this DNS")
        file.write(f"There is no name servers associated with this DNS \n") ###



# If the string is colored, it will contain the Hex Values of these colors
# so this method will remove these Hex values so the original string will be clear
def remove_style(string):
    string_with_no_style = str(string.replace("", ""))
    li = re.findall('\[[0-9]+m{1}', string_with_no_style)
    for i in li:
        string_with_no_style = str(string_with_no_style.replace(i, ""))
    return string_with_no_style

def Find_DNS_Info(name,file):
    #get informatoin related to DNS using {whatweb} tool
    whatweb_ = str(subprocess.check_output(f"whatweb {name}", shell=True, text=True))
    whatweb_=remove_style(whatweb_)

    # Create a file and write the output of {whatweb} on it
    save1 = open("save.txt", "a")
    save1.write(whatweb_)
    save1.close()

    # We want to iterate through the file content by each line
    save2 = open("save.txt", "r")
    saveFile = save2.readlines()
    save2.close()

    # Apply the following methods on each line
    print(f"{LightC}{bold} \n\n█████ Founded URL's associated with {name} █████")
    print(f"════════════════════════════════════{reset}")
    file.write(f"█████ Founded URL's associated with {name} █████\n")  ###
    number=0
    for line in saveFile:
        number+=1
        # Get the first element in the line, which is the URL
        URL=line.split()[0]
        print(f"URL{number}[{URL}]")
        file.write(f"URL{number}[{URL}]\n") ##


        # Retrieve the status of the link
        status = re.search(status_pattern,line)
        if status:
            print(f"Status{status.group()}")
            file.write(f"Status{str(status.group())}\n") ##


        # If the status is moved? then it is redirected. Find the redirected location
        rediret = re.search("RedirectLocation\[[^\[]*\]", line)
        if rediret:
            print(rediret.group())
            file.write(f"{str(rediret.group())}\n") ##


        # Retrieve the Title of the link
        title = re.search("Title\[[^\[]*\]", line)
        if title:
            print(title.group())
            file.write(f"{str(title.group()  )}\n") ##


        # Retrieve the country of the link's server
        country = re.search("Country\[[^\[]*\]", line)      # Print and write to the file (Country)
        if country:
            print(country.group())
            file.write(f"{str(country.group())}\n") ##


        # Retrieve the HTTPServer type
        HTTPServer = re.search("HTTPServer\[[^\[]*\]", line)         # Print and write to the file (HTTPServer)
        if HTTPServer:
            print(HTTPServer.group())
            file.write(f"{str(HTTPServer.group())}\n")  ##
            print(f"{LightC}════════════════════════════════════{reset}")
            file.write(f"════════════════════════════════════")

    os.remove("save.txt")







