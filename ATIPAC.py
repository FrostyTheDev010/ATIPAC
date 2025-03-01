import time
import os
import subprocess
import requests
import sys
from colorama import init, Fore, Style

# Initialize Colorama
init(autoreset=True)

# Function to check if Tor is running correctly
def check_tor_connection():
    try:
        response = requests.get("https://check.torproject.org/api/ip", proxies={"http": "socks5h://127.0.0.1:9050", "https": "socks5h://127.0.0.1:9050"})
        if response.status_code == 200:
            return True
        else:
            print(Fore.RED + "[!] Error: Tor is not working properly.")
            return False
    except requests.RequestException:
        print(Fore.RED + "[!] Error: Could not connect to the Tor network.")
        return False

# Function to install dependencies securely
def install_dependencies():
    try:
        import requests
    except ImportError:
        print(Fore.GREEN + '[+] Installing missing dependencies: requests...')
        subprocess.run([sys.executable, "-m", "pip", "install", 'requests'], check=True)

    try:
        subprocess.run(['which', 'tor'], check=True, stdout=subprocess.PIPE)
    except subprocess.CalledProcessError:
        print(Fore.GREEN + '[+] Tor is not installed. Installing Tor...')
        subprocess.run(['sudo', 'apt', 'update'], check=True)
        subprocess.run(['sudo', 'apt', 'install', 'tor', '-y'], check=True)
        print(Fore.GREEN + '[!] Tor has been installed.')

# Function to get current public IP through Tor
def get_ip():
    try:
        response = requests.get("https://check.torproject.org/api/ip", proxies={"http": "socks5h://127.0.0.1:9050", "https": "socks5h://127.0.0.1:9050"})
        return response.text
    except requests.RequestException:
        print(Fore.RED + "[!] Failed to retrieve IP.")
        return None

# Function to reload Tor and change the IP
def change_ip():
    if not check_tor_connection():
        print(Fore.RED + "[!] Exiting due to Tor connection issues.")
        return

    print(Fore.GREEN + "[+] Changing IP...")
    subprocess.run(["sudo", "service", "tor", "reload"], check=True)
    print(Fore.GREEN + f'[+] Your new IP is: {get_ip()}')

# Main execution
if __name__ == "__main__":
    install_dependencies()
    os.system("clear")

    print(Fore.CYAN + '''
                _          _______
     /\        | |        |__   __|
    /  \  _   _| |_ ___      | | ___  _ __
   / /\ \| | | | __/ _ \     | |/ _ \| '__|
  / ____ \ |_| | || (_) |    | | (_) | |
 /_/    \_\__,_|\__\___/     |_|\___/|_|
                V 1.0
    ''')

    time.sleep(2)

    print(Fore.YELLOW + "Change your SOCKS to 127.0.0.1:9050")

    x = input(Fore.CYAN + "[+] Time to change IP in seconds (default = 60) >> ") or 60
    lin = input(Fore.CYAN + "[+] How many times do you want to change your IP? (default = infinite) >> ") or 0
    lin = int(lin)

    if lin == 0:
        print(Fore.YELLOW + "Starting infinite IP change. Press Ctrl+C to stop.")
        while True:
            time.sleep(int(x))
            change_ip()
    else:
        for _ in range(lin):
            time.sleep(int(x))
            change_ip()
