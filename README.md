Traffic-analyzer-project:

This tool combines network traffic capturing and abuse checking of IP addresses using the AbuseIPDB API, as well as some error handling for private or recently checked IP addresses. 

Dependencies:
1. Python (version 3 or above)
2. Requests library (for making HTTP requests to the AbuseIPDB API)
3. Time library (for checking when IPs were last checked)
4. JSON library (to handle API responses)
5. Contextlib's suppress library (for error handling in dictionary updates)
6. Scapy library (for network traffic capturing)
7. Subprocess library (for executing shell commands and scripts)
8. OS library (for interacting with operating system like reading environment variables, etc.)

Usage:
This tool is designed to be run directly, however it may need elevated privileges:
```bash
sudo python abuse_checker.py
```

The tool should work on any OS as long as all dependencies are satisfied and it is run with the required permissions.

The tool captures traffic using Scapy and it saves ip addresses to “network_connections.txt”.
The second function of the tool is to run ip adrresess from “network_connections.txt” and prints a verdict: was clean (not abusive) or abusive based on AbuseIPDB's data for the past 20 days. 
The tool checks both source and destination IP addresses in each line of “network_connections.txt” and skips over any private IP addresses or those that have been checked recently.

Please ensure that you have the necessary permissions to run this script and capture network traffic, as well as a valid AbuseIPDB API key for abuse checking functionality. 

Configuration:
To use your own AbuseIPDB API key, replace “abuse_api_key” with your actual API key in the code.

Also, adjust the “days” variable to set how far back you want to check abuse report of an IP (the default is 20 days).

Output Format:
The script prints whether each IP address is clean or abusive based on AbuseIPDB' data. If an error occurs during checking, it will print a message with the error details. 
Private IP addresses and those that have been checked recently, will be skiped with a printed message.
