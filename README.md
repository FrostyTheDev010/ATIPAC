ATIPAC (Automatic Tor Internet Protocol Address Changer)
ATIPAC is a powerful tool that automates IP address rotation through the Tor network, enhancing your online privacy and making it harder for third parties to track you. This guide will walk you through every step of installation, configuration, and usage, ensuring you can use ATIPAC without any issues, even if you're new to the tool.

What Is ATIPAC?
ATIPAC (Auto Tor IP Auto Changer) allows you to automatically change your public IP address by cycling through Tor’s exit nodes. Tor is a privacy-focused network that routes your internet traffic through a series of encrypted nodes, masking your real IP address. By automating IP changes, ATIPAC provides better privacy for your online activities.

Why Use ATIPAC?
Enhanced Privacy: Tor’s encryption and distributed network of nodes mask your IP, making it harder for websites or third parties to track your activities.
Dynamic IP Rotation: Changes your public IP at regular intervals, making your online behavior harder to trace.
No Manual Intervention: Fully automated, saving you time and effort while ensuring your IP stays fresh.
Minimal Resources: Lightweight and easy on system resources.
Prerequisites
Before you begin, ensure the following:

Python 3.x: ATIPAC is written in Python, so you’ll need to have Python 3 installed on your system.
Tor: Tor must be installed and running on your system as ATIPAC relies on it to change your IP.
Internet Connection: Since ATIPAC uses the Tor network, you need an active internet connection.
Installation Instructions
Step 1: Clone the Repository
First, you’ll need to get the code for ATIPAC. This can be done by cloning the GitHub repository using the following command:

git clone https://github.com/yourusername/ATIPAC.git
cd ATIPAC

Step 2: Install Dependencies
ATIPAC requires several Python packages. The easiest way to install them is by using the requirements.txt file provided. In your terminal, run the following command to install the necessary dependencies:

pip install -r requirements.txt

This command will automatically install the required dependencies such as requests and colorama.

Step 3: Install Tor
If Tor is not already installed on your system, you’ll need to install it manually. On most Linux distributions (including Kali Linux), you can install Tor using the following commands:

sudo apt update
sudo apt install tor -y

Ensure that the Tor service is running by executing:

sudo service tor start

You can check if Tor is running by using:

sudo service tor status

It should show as "active" if Tor is running correctly.

Step 4: Running the Installer (Optional)
For a smoother experience, you can use the installer script that will automatically set up ATIPAC for you. This step is optional, but highly recommended for ease of use.

Run the following:

python3 ATIPAC_manager.py

Follow the on-screen prompts to either install or uninstall ATIPAC.

Running ATIPAC
Once ATIPAC is installed and Tor is running, you can begin using it. Follow these steps to start the tool:
Step 1:
Configure SOCKS Proxy: To route your traffic through the Tor network, you need to set up your application or system to use the Tor SOCKS proxy, which listens on 127.0.0.1:9050 by default.
Change your SOCKS proxy: In ATIPAC, you’ll be prompted to change your SOCKS proxy to 127.0.0.1:9050. This means that your internet traffic will be routed through the Tor network.
To configure your SOCKS proxy:
For browsers (e.g., Firefox or Chrome), you will need to go into the proxy settings and set the SOCKS5 proxy to 127.0.0.1:9050.
For command-line tools (e.g., curl, wget), use the --proxy option and specify 127.0.0.1:9050.

Step 2: Start ATIPAC
To begin, run the ATIPAC script in your terminal:

python3 ATIPAC.py

Once you execute the script, it will initiate and display a colorful, informative terminal output thanks to the colorama module.

Step 3: Configure IP Change Settings
ATIPAC will ask you for two key inputs:

Time Interval for IP Changes: This is how often you want your IP to change. The value is in seconds. For example:

Enter 60 for a change every minute.
Enter 30 for a change every 30 seconds.
Example prompt:

[+] Time to change IP in seconds (default = 60) >> 60

Number of IP Changes: This specifies how many times you want the IP to change. You can enter 0 for infinite changes (the script will keep running until you stop it) or specify a fixed number of changes.
Example prompt:

[+] How many times do you want to change your IP? (default = infinite) >> 0

Step 4: IP Rotation Begins
Once you provide the interval and number of changes, ATIPAC will begin rotating your IP addresses automatically. The script will periodically display the new IP addresses as they are rotated through Tor’s exit nodes:

[+] Changing IP...
[+] Your new IP is: 123.456.789.012

Step 5: Stopping the Script
To stop ATIPAC from changing your IP, simply press Ctrl + C in the terminal. This will terminate the script, and the IP rotation process will stop.

Uninstalling ATIPAC
If you ever want to remove ATIPAC from your system, you can use the uninstaller script:

python3 ATIPAC_manager.py

Follow the prompts, and ATIPAC will be removed from your system. The script will uninstall both the necessary files and dependencies.

Troubleshooting
1. Tor Not Running
If ATIPAC cannot connect to the Tor network, you may see an error like:

[!] Error: Could not connect to the Tor network.

This happens if Tor isn’t installed or running. To resolve this:

Make sure Tor is installed:

sudo apt install tor

Ensure that the Tor service is running:

sudo service tor start

Check Tor’s status:

sudo service tor status

If Tor is active, try running ATIPAC again.

2. Missing Dependencies
If you receive errors regarding missing dependencies (such as requests or colorama), you can manually install them:

pip install requests colorama

Ensure you're using Python 3 when installing dependencies.

3. Permission Issues
If you face permission issues (e.g., "Permission Denied"), you may need to run the script with elevated privileges (using sudo):

sudo python3 ATIPAC.py

This will grant the script the necessary permissions to interact with the Tor service and modify system files.

Best Practices
Always Use HTTPS: Even though ATIPAC changes your public IP, it’s important to always use HTTPS websites to ensure your communication is encrypted and secure.
Regular Updates: Keep both Tor and ATIPAC up to date. Regularly check for updates to ensure you’re using the latest versions.
Monitor Your Connection: Periodically check that ATIPAC is working as expected. If IP changes aren’t happening as configured, make sure Tor is running correctly.

Key Takeaways
ATIPAC automates IP rotation via Tor for enhanced privacy.
You can configure the time interval between IP changes and specify how many times to change your IP.
Tor must be installed and running for ATIPAC to work.
The script is easy to install and uninstall using simple commands.
Logging and error handling ensure smooth operation with clear feedback in the terminal.

Contributing
ATIPAC is an open-source project, and we welcome contributions! If you encounter any bugs, want to suggest a new feature, or improve the documentation, feel free to open an issue or submit a pull request, you can also email me at Frosty-the-dev@outlook.com or message frosty_v2.0.0.exe on Discord.



MUCH MUCH LOVE, MANY MANY HEARTS, AND A LOT OF THANKS TO FDX100 on GitHub for his original script that i've built upon on. (https://github.com/FDX100/Auto_Tor_IP_changer)


now go and have a secure day!
