import requests
import colorama
import asyncio
import time
import threading
import os
import ctypes
from colorama import Fore, Style
from threading import Thread
from sys import stdout
from requests import Session
from time import strftime, gmtime

sent = 0
session = Session()
b = Style.BRIGHT
os = os.system
os('cls')

ctypes.windll.kernel32.SetConsoleTitleW(f"[WEBHOOK SPAMMER] By Cold | Dont Skid Me ;) ")

print(f"""

{b+Fore.BLUE}
 $$$$$$\  $$$$$$\ $$\      $$$$$$$\        
$$  __$$\$$  __$$\$$ |     $$  __$$\       
$$ /  \__$$ /  $$ $$ |     $$ |  $$ |      
$$ |     $$ |  $$ $$ |     $$ |  $$ |      
$$ |     $$ |  $$ $$ |     $$ |  $$ |      
$$ |  $$\$$ |  $$ $$ |     $$ |  $$ |      
\$$$$$$  |$$$$$$  $$$$$$$$\$$$$$$$  |      
 \______/ \______/\________\_______/  
            | |                                   
            |_|                                   
{b+Fore.BLUE} > {Fore.RESET}Webhook Spammer
{b+Fore.BLUE} > {Fore.RESET}Creator: Cold#6660
""")
print(f"[{Fore.GREEN}>{Fore.RESET}] Webhook link ")
webhoo = input("#root~Cold~ ")
print(f"[{Fore.GREEN}>{Fore.RESET}] Message to send ")
msg = input("#root~Cold~ ")

webhook_embed = {
	'content': msg,
}
try:
    time.sleep(0.1)
    r = requests.post(webhoo, json=webhook_embed)
except:
     pass
