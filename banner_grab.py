#! /usr/bin/python3
import socket

def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        
        # Try immediate recv
        try:
            
            banner = s.recv(1024)
            if banner:
                print(f"Received banner immediately from {ip}:{port}")
        except socket.timeout:
            banner = b""
        
        # For HTTP-like ports, send a request
        if port in (80,8080):
            s.send(b"GET / HTTP/1.0\r\n\r\n")
            banner = s.recv(1024)
        
        s.close()
        return banner
    except Exception as e:
        return e

if __name__ == "__main__":
    ip = input("Enter the target IP you want to grab: ")
    # for port in range(900, 1024):
    for port in [902,912]:
        banner = grab_banner(ip, port)
        if banner:
            print(f"Received banner from {ip}:{port} - {banner}")
        else:
            print(f"Could not retrieve banner from {ip}:{port}")
    