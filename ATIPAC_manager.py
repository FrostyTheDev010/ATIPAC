import os
import sys
import shutil
import subprocess

# Detect OS
WINDOWS = sys.platform.startswith("win")
LINUX = sys.platform.startswith("linux")

# Define install paths
if WINDOWS:
    INSTALL_PATH = os.path.join(os.getenv("APPDATA"), "ATIPAC")
    BATCH_FILE = os.path.join(INSTALL_PATH, "atipac.bat")
    PATH_ENV_CMD = f'setx PATH "%PATH%;{INSTALL_PATH}"'
elif LINUX:
    INSTALL_PATH = "/usr/local/bin/ATIPAC"
    PATH_ENV_CMD = "echo 'export PATH=$PATH:/usr/local/bin' >> ~/.bashrc && source ~/.bashrc"

# Install ATIPAC
def install():
    print("[+] Installing ATIPAC...")

    # Ensure the installation directory exists
    os.makedirs(INSTALL_PATH, exist_ok=True)

    # Find ATIPAC.py
    script_source = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ATIPAC.py")
    if not os.path.exists(script_source):
        print("[!] ATIPAC.py not found!")
        sys.exit(1)

    # Move ATIPAC.py to install directory
    shutil.move(script_source, os.path.join(INSTALL_PATH, "ATIPAC.py"))

    if WINDOWS:
        # Create a batch file to run ATIPAC
        with open(BATCH_FILE, "w") as f:
            f.write(f'@echo off\npython "{INSTALL_PATH}\\ATIPAC.py" %*\n')

        # Add ATIPAC to system PATH
        subprocess.run(PATH_ENV_CMD, shell=True)
        
        # Refresh environment variables so "atipac" works immediately
        subprocess.run("powershell -Command $env:Path = [System.Environment]::GetEnvironmentVariable('Path','User')", shell=True)

    elif LINUX:
        # Move script and give execution permission
        shutil.move(script_source, INSTALL_PATH)
        subprocess.run(["chmod", "+x", INSTALL_PATH])

        # Add ATIPAC to system PATH
        subprocess.run(PATH_ENV_CMD, shell=True)

    print("[✔] Installation successful! Run 'atipac' to start.")

# Uninstall ATIPAC
def uninstall():
    print("[+] Uninstalling ATIPAC...")

    if os.path.exists(INSTALL_PATH):
        shutil.rmtree(INSTALL_PATH)
        print("[✔] ATIPAC removed successfully.")

    if WINDOWS and os.path.exists(BATCH_FILE):
        os.remove(BATCH_FILE)

    print("[✔] Uninstallation complete.")

# Main function
def main():
    choice = input("[+] To install, press (Y). To uninstall, press (N): ").strip().lower()
    
    if choice == "y":
        install()
    elif choice == "n":
        uninstall()
    else:
        print("[!] Invalid input!")

if __name__ == "__main__":
    main()
