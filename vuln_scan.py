#!/usr/bin/python3
import socket
import sys
import os
from banner_grab import grab_banner

def load_vulnerabilities(file_path):
    if not os.path.exists(file_path):
        print(f"[*] Vulnerability file {file_path} does not exist.")
        return []
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

def main():
    if len(sys.argv) != 2:
        print("[*] Usage: python3 vuln_scan.py <vuln_file>")
        sys.exit(1)

    vuln_file = sys.argv[1]
    vulnerabilities = load_vulnerabilities(vuln_file)
    if not vulnerabilities:
        print("No valid vulnerabilities found.")
        sys.exit(1)

    for vuln in vulnerabilities:
        print(f"[*] Loaded vulnerability: {vuln}")

    
    ip = input("Enter the target IP you want to grab: ")
    for port in range(1, 1024):
        banner = grab_banner(ip, port)
        for vuln in vulnerabilities:
            if vuln in banner.decode():
                print(f"[*] Vulnerable server {ip}:{port} - {banner}")
            # else:
            #     print(f"[*] Server not vulnerable {ip}:{port}")


if __name__ == "__main__":
    main()