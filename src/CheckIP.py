import os
import subprocess
import requests
import time
import json
from contextlib import suppress

abuse_api_key  = "Insert_your_API_key_here" 
url = 'https://api.abuseipdb.com/api/v2/check'
checked_ips = {}  
days = 20

headers = {
    'Accept': 'application/json',
    'Key': abuse_api_key
}

def check_ip(ip):
    # Check if the IP address is private or already checked in last 60 minutes. If yes, then return immediately.
    if ip.startswith(('192.168.', '10.', '172.16.', '169.254', '0.0.0', '::1', '127.')) or (ip in checked_ips and time.time() - checked_ips[ip] < 60 * 60):
        return f"{ip} is private IP or has been checked recently, skipping..."
        
    try:
        response = requests.get(url=url, headers=headers, params={"ipAddress": ip})
        response.raise_for_status()   # Raise an exception for bad status codes
        data = response.json()
        #print (data) Check API response for debug purposes
            
        if 'data' in data and 'abuseConfidenceScore' in data['data'] and float(data['data']['abuseConfidenceScore']) < 35: 
            return f"{ip} is clean"
        else:
            return f"{ip} is abusive"
    except requests.RequestException as e:
        print("Error checking {}: {}".format(ip, str(e)))

def main():
    with open("network_connections.txt", 'r') as f:
        for line in f:
            parts = line.strip().split(' <-> ')
            
            # Check if the line has valid format and skip otherwise
            if len(parts) != 2:
                print(f"Error: invalid line format  - {line}")
                continue
            
            src_ip, dst_ip = parts
            print(check_ip(src_ip))
            print(check_ip(dst_ip))
    
    # Update the checked IPs dictionary after checking all the IP addresses
    with suppress(KeyError):
        for ip in (src_ip, dst_ip):
            checked_ips[ip] = time.time()

if __name__ == "__main__":
    main()
