import os
import subprocess
from scapy.all import *

# Set the output file
output_file = "network_connections.txt"

def packet_callback(packet):
    try:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        return f"{src_ip} <-> {dst_ip}\n"
    except:
        return f"Unknown\n"

def main():
    with open(output_file, 'w') as f:
        f.write("Connections:\n")

        # Capture active connections using Scapy's sniff function
        packets = sniff(filter="ip")
        for packet in packets:
            f.write(packet_callback(packet))

    

if __name__ == "__main__":
    main()

print("Output written to", output_file)