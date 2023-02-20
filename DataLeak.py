############################
# Author: KAZAM[A]#9629    #
# Discord: .gg/M382MpNAtm  #
# Github : @KazamaOnGithub #
############################

import getpass,subprocess , requests, json, time, sys, os, socket, base64, random
from pystyle import *
from colorama import Fore,Style,Back, init
from ast import main
from random import choices
from base64 import b64decode
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from os import getlogin, listdir
from json import loads
from re import findall
from urllib.request import Request, urlopen
from subprocess import Popen, PIPE
from datetime import datetime
init(autoreset=True)

#####################
# Variable et trucs #
#####################

 
Cursor.HideCursor()
############################
# Author: KAZAM[A]#9629    #
# Discord: .gg/M382MpNAtm  #
# Github : @KazamaOnGithub #
############################

######################
# Titre du programme #
######################

os.system( "title 𝘿𝙚𝙫 𝙗𝙮 𝙆𝙖𝙯𝙖𝙢𝙖" )


#################
#   Variables   #
#################


UserChannelsAPI = "users/@me/channels"
SendMessageAPI = "v8/channels/{}/messages" 


####################
# Quest menu lobby #
####################


def first_quest_menulobby():
    print(" [" + Fore.RED + "!" + Fore.WHITE + "] Only the figures are taken into account")
    print("\n")
    first_choice = input(" [" + Fore.GREEN + "$" + Fore.WHITE + "] " + "Enter your choice :: ")
    
    # if du database finder
    if first_choice == "1":
        video_a_supp()
    
    # if du pinger
    if first_choice == "2":
        ip_pinger()

    # if du ip locator
    if first_choice == "3":
        ip_locator()

    # if à ne pas remplacer
    if first_choice == "8":
        first_quest_menulobby()

    # if à ne pas remplacer
    if first_choice == "9":
        first_quest_menulobby()

    # if du switch premium
    if first_choice == "6":
        switch_premium()

    if first_choice == "4":
        id_finder()

    # if des mises à jours
    if first_choice == "5":
        mise_a_jour()
    
    else:
        first_quest_menulobby()


####################
# def du id_finder #
#################### 


def id_finder():
  os.system("cls")
  banner_menu()
  id = input("\n [" + Fore.GREEN + "$" + Fore.WHITE + "] Put the discord ID right here " + Fore.GREEN + "═══> " + Fore.WHITE)
  send_id = id.encode('utf-8')
  base64_bytes = base64.b64encode(send_id)
  print("\n" * 3 + Fore.WHITE + Center.XCenter(Box.DoubleCube(" ------ Token result ------ ")) + Fore.WHITE + "\n" * 3 + " [" + Fore.RED + ">" + Fore.WHITE + "] The first part of the Token is " + Fore.GREEN + "═══> " + Fore.WHITE + str(base64_bytes.decode('utf-8')))
  
  retry_idfinder = input("\n" * 2 + " [" + Fore.GREEN + "?" + Fore.WHITE + "] Do you want to restart the program? (y/n): ")
  
  if retry_idfinder == "y" or retry_idfinder == "yes" or retry_idfinder == "Y" or retry_idfinder == "YES" or retry_idfinder == "Yes":
    id_finder()
  
  elif retry_idfinder == "n" or retry_idfinder == "no" or retry_idfinder == "N" or retry_idfinder == "NO" or retry_idfinder == "No":
    print("\n1")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("3")
    time.sleep(0.5)
    print("Back in class...")
    time.sleep(2)
    banner_menu()
    menu1()
  
  else:
    os.system("cls")
    print()
    print(Center.XCenter(Center.YCenter(Box.DoubleCube(" /!\If you don't enter the right answers, the program restarts the page /!\ "))))
    time.sleep(4)
    id_finder()

##################
# video à delete #
##################

def video_a_supp():
    banner_menu()
    input("\n   [" + Fore.GREEN + "1" + Fore.WHITE + "] Enter the keyword ═══> ")
    print("\n('live:1688852848965081', 'xbl:2535407651337301', 'discord:664156099804528652', 'ip:78.219.87.169', 'Kader_Moula'),")
    print("\n\n [" + Fore.RED + "!" + Fore.WHITE + "] Return in 10sec")
    time.sleep(10)
    print("\n1")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("3")
    time.sleep(0.5)
    print("Back in class...")
    time.sleep(2)
    banner_menu()
    menu1()
    
#####################
# Switch to premium #  
#####################


def switch_premium():   
    banner_menu()
    print(Center.XCenter("\n   [" + Fore.GREEN + "1" + Fore.WHITE + "] Si vous voulez avoir le logiciel complet, lifetime, alors il vous suffit d'upgrade votre grade en premium.\n\n   [" + Fore.GREEN + "2" + Fore.WHITE + "] Je vous explique comment faire juste ici. Tout d'abord veuillez rejoindre ce discord avec lien permanent \n       (copy: " + Fore.GREEN + "https://discord.gg/M382MpNAtm" + Fore.WHITE + ")" + "\n\n   [" + Fore.GREEN + "3" + Fore.WHITE + "] Au niveau des améliorations voici la liste: \n\n   [" + Fore.GREEN + "4" + Fore.WHITE + "] Mise à jour avant tout le monde, annulation des chargment, catégorie supplémentaire, recherche plus rapide,\n       grade" + (Colorate.Horizontal(Colors.yellow_to_red, " DataLeak Premium", 1)) + Fore.WHITE + " etc..."))
    print("\n\n [" + Fore.RED + "!" + Fore.WHITE + "] If you want to have it in English then click on this link: \n     (copy:" + Fore.GREEN + " https://github.com/KazamaOnGithub/DataLeak_English_Trad/blob/main/README.md" + Fore.WHITE + ")\n")
    print(" [" + Fore.GREEN + "$" + Fore.WHITE + "] Mark 'r' or 'return' to return to the basic menu")
    premium_return = input(" [" + Fore.GREEN + ">" + Fore.WHITE + "] I am waiting for more than just your answer: ")

    if premium_return == "r" or premium_return == "return" or premium_return == "R" or premium_return == "Return":
        print("1")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("3")
        time.sleep(0.5)
        print("Back in class...")
        time.sleep(2)
        banner_menu()
        menu1()

    else:
        os.system("cls")
        print()
        print(Center.XCenter(Center.YCenter(Box.DoubleCube(" /!\If you don't enter the right answers, the program restarts the page /!\ "))))
        time.sleep(4)
        switch_premium()


##############
#     Maj    #
##############


def mise_a_jour():
    os.system("cls")
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """ 
                                                          
                         _____ _   _   _ _________   ___   _   _ _______ __   ___ _______ 
                        |  ___| | | | | |.  __  \ \ / | | | | | |.  __  |. | /_  |____  .|
                        | |_  | | | | | || |  | |  V /| | | | | || |  | || |   | |    | | 
                        |  _| | |/ /_/ / | | _| | |\ \| |/ /_/ / | | _| || |___| |    | | 
                        |_|   |_______/  |_||___|_| \_|_______/  |_||___||_______|    | | 
                                                                                      |_| 
                                 
                                          
                       	    Basic Multi-tools Kit For Everyone  |  Dev by Kazama                       
                            
                            """
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write(" \x1b[1;%dm%s%s\n " % (random.choice(colors), line, clear))
        time.sleep(0.05)

    print(Center.XCenter("\n\n [" + Fore.GREEN + "1.0" + Fore.WHITE + "] To install version (Beta) ═══>" + Fore.GREEN + " https://github.com/KazamaOnGithub/DataLeak_1.0_beta"))
    print("\n         [" + Fore.GREEN + "2.0" + Fore.WHITE + "] To install version (Beta) ═══>" + Fore.GREEN + " Coming soon..." + Fore.WHITE + "\n\n         [" + Fore.GREEN + "3.0" + Fore.WHITE + "] To install version (Beta) ═══>" + Fore.GREEN + " Coming soon..." + Fore.WHITE + "\n\n         [" + Fore.GREEN + "4.0" + Fore.WHITE + "] To install version (Beta) ═══>" + Fore.GREEN + " Coming soon..." + Fore.WHITE + "\n\n         [" + Fore.GREEN + "5.0" + Fore.WHITE + "] To install version (Beta) ═══>" + Fore.GREEN + " Coming soon...")
    print("\n\n [" + Fore.RED + "$" + Fore.WHITE + "] Mark 'r' or 'return' to return to the basic menu")
    maj_return = input("\n [" + Fore.GREEN + ">" + Fore.WHITE + "] I am waiting for more than just your answer: ")
    
    if maj_return == "r" or maj_return == "return" or maj_return == "R" or maj_return == "Return":
        print("\n1")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("3")
        time.sleep(0.5)
        print("Back in class...")
        time.sleep(2)
        banner_menu()
        menu1()

    else:
        os.system("cls")
        print()
        print(Center.XCenter(Center.YCenter(Box.DoubleCube(" /!\If you don't enter the right answers, the program restarts the page /!\ "))))
        time.sleep(4)
        mise_a_jour()


##############
# IP locator #
##############


def ip_locator():
    os.system("cls")
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """ 
                                                          
                         _____ _   _   _ _________   ___   _   _ _______ __   ___ _______ 
                        |  ___| | | | | |.  __  \ \ / | | | | | |.  __  |. | /_  |____  .|
                        | |_  | | | | | || |  | |  V /| | | | | || |  | || |   | |    | | 
                        |  _| | |/ /_/ / | | _| | |\ \| |/ /_/ / | | _| || |___| |    | | 
                        |_|   |_______/  |_||___|_| \_|_______/  |_||___||_______|    | | 
                                                                                      |_| 
                                 
                                          
                       	    Basic Multi-tools Kit For Everyone  |  Dev by Kazama                       
                            
                            """
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write(" \x1b[1;%dm%s%s\n " % (random.choice(colors), line, clear))
        time.sleep(0.05)
    print()
    ip = input(" [" + Fore.GREEN + ">" + Fore.WHITE + "] Enter the IP address (target): "); ip.replace(" ", "")


    r = requests.get(f"http://ip-api.com/json/{ip}")
    r2 = requests.get(f"https://ipinfo.io/{ip}")
    values = json.loads(r.text)
    data = r2.json()
    city = data["city"]
    location = data["loc"].split(",")
    latitude = location[0]
    longitude = location[1]

    print()
    print(Center.XCenter(Box.DoubleCube(" ------ Informations list ------\n")))
    print("\n   [" + Fore.GREEN + "1" + Fore.WHITE +"] Country" + Fore.GREEN + " ═══> "+ Fore.WHITE + values["country"] + f" [{values['countryCode']}]")
    print("\n   [" + Fore.GREEN + "2" + Fore.WHITE +"] Region Name" + Fore.GREEN + " ═══> "+ Fore.WHITE + values["regionName"] + f" [{values['region']}]")
    print("\n   [" + Fore.GREEN + "3" + Fore.WHITE +"] City" + Fore.GREEN + " ═══> "+ Fore.WHITE + city)
    print("\n   [" + Fore.GREEN + "4" + Fore.WHITE +"] Time Zone" + Fore.GREEN + " ═══> "+ Fore.WHITE + values["timezone"])
    print("\n   [" + Fore.GREEN + "5" + Fore.WHITE +"] ISP" + Fore.GREEN + " ═══> "+ Fore.WHITE + values["isp"])
    print("\n"*2 + " [" + Fore.RED + "!" + Fore.WHITE + "] You have 15 seconds before being redirected to the main menu!")
    time.sleep(15)
    banner_menu() 
    menu1()



#############
# IP pinger #
#############


def ip_pinger():
    os.system("cls")
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """ 
                                                          
                         _____ _   _   _ _________   ___   _   _ _______ __   ___ _______ 
                        |  ___| | | | | |.  __  \ \ / | | | | | |.  __  |. | /_  |____  .|
                        | |_  | | | | | || |  | |  V /| | | | | || |  | || |   | |    | | 
                        |  _| | |/ /_/ / | | _| | |\ \| |/ /_/ / | | _| || |___| |    | | 
                        |_|   |_______/  |_||___|_| \_|_______/  |_||___||_______|    | | 
                                                                                      |_| 
                                 
                                          
                       	    Basic Multi-tools Kit For Everyone  |  Dev by Kazama                       
                            
                            """
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write(" \x1b[1;%dm%s%s\n " % (random.choice(colors), line, clear))
        time.sleep(0.05)

    print()
    ip = input(" [" + Fore.GREEN + "$" + Fore.WHITE + "]" + " Enter the IP (target): ")
    print("\n [" + Fore.RED + "!" + Fore.WHITE + "] Press CTRL + C for stop it\n")
    os.system('cmd /k '"ping " + ip + " -t")


#################
#   menu lobby  #
#################


def menu1():
    print("\n"*2)
    print(Fore.GREEN + "                        [" + Fore.WHITE + "1" + Fore.GREEN + "]" + Fore.WHITE + " Database Finder    " + Fore.GREEN + " [" + Fore.WHITE + "2" + Fore.GREEN + "]" + Fore.WHITE + " IP Pinger    " + Fore.GREEN + " [" + Fore.WHITE + "3" + Fore.GREEN + "]" + Fore.WHITE + " IP Locator    ")
    print()
    print(Fore.GREEN + "                        [" + Fore.WHITE + "4" + Fore.GREEN + "]" + Fore.WHITE + " Token Finder       " + Fore.GREEN + " [" + Fore.WHITE + "5" + Fore.GREEN + "]" + Fore.WHITE + " Update       " + Fore.GREEN + " [" + Fore.WHITE + "6" + Fore.GREEN + "]" + Fore.WHITE + " Switch to" + (Colorate.Horizontal(Colors.yellow_to_red, " Premium     ", 1)))
    print("\n"*3)
    first_quest_menulobby()

##############
#   Banner   #
##############

def banner_menu():
    os.system("cls")
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """ 
                                                          
                         _____ _   _   _ _________   ___   _   _ _______ __   ___ _______ 
                        |  ___| | | | | |.  __  \ \ / | | | | | |.  __  |. | /_  |____  .|
                        | |_  | | | | | || |  | |  V /| | | | | || |  | || |   | |    | | 
                        |  _| | |/ /_/ / | | _| | |\ \| |/ /_/ / | | _| || |___| |    | | 
                        |_|   |_______/  |_||___|_| \_|_______/  |_||___||_______|    | | 
                                                                                      |_| 


                       	    Basic Multi-tools Kit For Everyone  |  Dev by Kazama                       
                            
                            """
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write(" \x1b[1;%dm%s%s\n " % (random.choice(colors), line, clear))
        time.sleep(0.05)

banner_menu()

menu1()

############################
# Author: KAZAM[A]#9629    #
# Discord: .gg/M382MpNAtm  #
# Github : @KazamaOnGithub #
############################
