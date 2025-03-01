import os
import subprocess
import sys
from colorama import init, Fore, Style

# Initialize Colorama
init(autoreset=True)

def install():
    try:
        # Give the script proper permissions
        subprocess.run(['chmod', '777', 'ATIPAC.py'], check=True)

        # Create installation directories
        os.makedirs('/usr/share/atipac', exist_ok=True)

        # Copy the script to /usr/share/atipac
        subprocess.run(['cp', 'ATIPAC.py', '/usr/share/atipac/ATIPAC.py'], check=True)

        # Create a command to run the script easily
        cmnd = '#! /bin/sh\nexec python3 /usr/share/atipac/ATIPAC.py "$@"'
        with open('/usr/bin/atipac', 'w') as f:
            f.write(cmnd)

        # Make everything executable
        subprocess.run(['chmod', '+x', '/usr/bin/atipac', '/usr/share/atipac/ATIPAC.py'], check=True)

        print(Fore.GREEN + "ATIPAC installed successfully. Type 'atipac' in terminal to run.")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"[!] Error during installation: {e}")

def uninstall():
    try:
        # Remove installed files
        subprocess.run(['rm', '-r', '/usr/share/atipac'], check=True)
        subprocess.run(['rm', '/usr/bin/atipac'], check=True)

        print(Fore.GREEN + "ATIPAC has been uninstalled successfully.")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"[!] Error during uninstallation: {e}")

# Main program execution
if __name__ == "__main__":
    choice = input(Fore.CYAN + '[+] To install, press (Y). To uninstall, press (N): ').lower()

    if choice == 'y':
        install()
    elif choice == 'n':
        uninstall()
    else:
        print(Fore.RED + "[!] Invalid option. Please press 'Y' to install or 'N' to uninstall.")
