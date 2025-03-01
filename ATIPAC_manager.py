import os
import shutil
import platform
import subprocess
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# Define the installation and uninstallation paths for different OSes
WINDOWS_INSTALL_PATH = os.path.join(os.environ['APPDATA'], 'ATIPAC')
LINUX_INSTALL_PATH = "/usr/local/bin/ATIPAC"

def install_windows():
    print(Fore.GREEN + "[+] Installing ATIPAC on Windows...")
    atipac_script = os.path.join(os.getcwd(), "ATIPAC.py")
    if not os.path.exists(WINDOWS_INSTALL_PATH):
        os.makedirs(WINDOWS_INSTALL_PATH, exist_ok=True)
    
    try:
        # Move the script to the AppData directory
        shutil.move(atipac_script, WINDOWS_INSTALL_PATH)
        print(Fore.GREEN + "[+] ATIPAC script moved successfully.")
        
        # Create the batch script to execute ATIPAC
        batch_script = os.path.join(WINDOWS_INSTALL_PATH, "atipac.bat")
        with open(batch_script, "w") as f:
            f.write(f'python "{WINDOWS_INSTALL_PATH}\\ATIPAC.py" %*')
        
        print(Fore.GREEN + "[+] Batch script created.")
        
        # Set environment variables to run from anywhere
        user_path = os.environ['USERPROFILE']
        path_var = os.environ.get('PATH', '')
        new_path = f'{user_path}\\AppData\\Roaming\\ATIPAC'
        os.environ['PATH'] = new_path + ';' + path_var

        print(Fore.GREEN + "[+] ATIPAC installed and ready for use.")
        
    except Exception as e:
        print(Fore.RED + f"[!] Error during installation: {e}")

def install_linux():
    print(Fore.GREEN + "[+] Installing ATIPAC on Linux...")
    atipac_script = os.path.join(os.getcwd(), "ATIPAC.py")
    if not os.path.exists(LINUX_INSTALL_PATH):
        os.makedirs(LINUX_INSTALL_PATH, exist_ok=True)
    
    try:
        # Move the script to the /usr/local/bin directory
        shutil.move(atipac_script, LINUX_INSTALL_PATH)
        print(Fore.GREEN + "[+] ATIPAC script moved successfully.")

        # Make the script executable
        subprocess.run(['chmod', '+x', LINUX_INSTALL_PATH], check=True)

        # Create a symbolic link to run the script globally
        subprocess.run(['ln', '-s', LINUX_INSTALL_PATH, '/usr/local/bin/atipac'], check=True)
        
        print(Fore.GREEN + "[+] ATIPAC installed and ready for use.")
        
    except Exception as e:
        print(Fore.RED + f"[!] Error during installation: {e}")

def uninstall_windows():
    print(Fore.YELLOW + "[+] Uninstalling ATIPAC on Windows...")
    try:
        # Remove the batch script and Python script
        atipac_script = os.path.join(WINDOWS_INSTALL_PATH, "ATIPAC.py")
        batch_script = os.path.join(WINDOWS_INSTALL_PATH, "atipac.bat")
        if os.path.exists(atipac_script):
            os.remove(atipac_script)
        if os.path.exists(batch_script):
            os.remove(batch_script)
        
        # Remove the ATIPAC folder entirely
        shutil.rmtree(WINDOWS_INSTALL_PATH)
        print(Fore.GREEN + "[+] ATIPAC uninstalled successfully, folder deleted.")
        
    except Exception as e:
        print(Fore.RED + f"[!] Error during uninstallation: {e}")

def uninstall_linux():
    print(Fore.YELLOW + "[+] Uninstalling ATIPAC on Linux...")
    try:
        # Remove the ATIPAC script
        atipac_script = os.path.join(LINUX_INSTALL_PATH, "ATIPAC.py")
        if os.path.exists(atipac_script):
            os.remove(atipac_script)
        
        # Remove the symbolic link
        subprocess.run(['rm', '/usr/local/bin/atipac'], check=True)

        # Remove the ATIPAC folder (if exists)
        if os.path.exists(LINUX_INSTALL_PATH):
            shutil.rmtree(LINUX_INSTALL_PATH)
        
        print(Fore.GREEN + "[+] ATIPAC uninstalled successfully, folder deleted.")
        
    except Exception as e:
        print(Fore.RED + f"[!] Error during uninstallation: {e}")

def main():
    print(Fore.CYAN + "[+] ATIPAC Manager")
    user_os = platform.system().lower()

    # Install or uninstall ATIPAC
    choice = input(Fore.CYAN + "[+] To install, press (Y). To uninstall, press (N): ").strip().upper()
    
    if choice == "Y":
        if user_os == "windows":
            install_windows()
        elif user_os == "linux":
            install_linux()
        else:
            print(Fore.RED + "[!] OS not supported.")
    
    elif choice == "N":
        if user_os == "windows":
            uninstall_windows()
        elif user_os == "linux":
            uninstall_linux()
        else:
            print(Fore.RED + "[!] OS not supported.")
    else:
        print(Fore.RED + "[!] Invalid option. Please select (Y) to install or (N) to uninstall.")

if __name__ == "__main__":
    main()
