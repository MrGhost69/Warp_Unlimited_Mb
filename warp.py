import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys

# Set console title
os.system("title WARP-PLUS-CLOUDFLARE Mr.Ghost" if os.name == 'nt' else 'clear')

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# ASCII Art and Info
ascii_art = """
 __     __  __       _____ _               _   
 |  \/  |     / ____| |             | |  
 | \  / |_ __| |  __| |__   ___  ___| |_ 
 | |\/| | '__| | |_ | '_ \ / _ \/ __| __|
 | |  | | |_ | |__| | | | | (_) \__ \ |_ 
 |_|  |_|_(_) \_____|_| |_|\___/|___/\__|
"""
print(ascii_art)
print("--------------------------------------------------------------")
print("Author   :- MrGhostX")
print("Telegram :- Cyber Shield Force BD")
print("Github   :- @MrGhost69")
print("Tools    :- 1.1.1.1 / WARP UNLIMITED MB \n")
print("--------------------------------------------------------------")

# Get WARP+ ID from user
referrer = input("[#] Enter the WARP+ ID:")

# Generate random string
def genString(stringLength):
    try:
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(stringLength))
    except Exception as error:
        print(error)

# Generate random digit string
def digitString(stringLength):
    try:
        digit = string.digits
        return ''.join((random.choice(digit) for i in range(stringLength)))    
    except Exception as error:
        print(error)

url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'

# Function to send request
def run():
    try:
        install_id = genString(22)
        body = {
            "key": "{}=".format(genString(43)),
            "install_id": install_id,
            "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
            "referrer": referrer,
            "warp_enabled": False,
            "tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
            "type": "Android",
            "locale": "es_ES"
        }
        data = json.dumps(body).encode('utf8')
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Host': 'api.cloudflareclient.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.12.1'
        }
        req = urllib.request.Request(url, data, headers)
        response = urllib.request.urlopen(req)
        status_code = response.getcode()
        return status_code
    except Exception as error:
        print(error)

g = 0
b = 0
while True:
    result = run()
    if result == 200:
        g = g + 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print("")
        print("                  WARP-PLUS-CLOUDFLARE (script) By Mr.Ghost")
        print("")
        animation = [
            "[■□□□□□□□□□] 10%",
            "[■■□□□□□□□□] 20%",
            "[■■■□□□□□□□] 30%",
            "[■■■■□□□□□□] 40%",
            "[■■■■■□□□□□] 50%",
            "[■■■■■■□□□□] 60%",
            "[■■■■■■■□□□] 70%",
            "[■■■■■■■■□□] 80%",
            "[■■■■■■■■■□] 90%",
            "[■■■■■■■■■■] 100%"
        ]
        for i in range(len(animation)):
            time.sleep(0.5)
            sys.stdout.write("\r[+] Preparing... " + animation[i % len(animation)])
            sys.stdout.flush()
        print(f"\n[-] WORK ON ID: {referrer}")    
        print(f"[:)] {g} GB has been successfully added to your account.")
        print(f"[#] Total: {g} Good {b} Bad")
        print("[*] After 7 seconds, a new request will be sent.")
        time.sleep(7)
    else:
        b = b + 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print("")
        print("                  WARP-PLUS-CLOUDFLARE (script) By Mr.Ghost")
        print("")
        print("[:(] Error when connecting to server.")
        print(f"[#] Total: {g} Good {b} Bad")
