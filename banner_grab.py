#!/usr/bin/python3
import socket

def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        
        # Try immediate recv
        try:
            
            banner = s.recv(1024)
            # if banner:
            #     print(f"[*] Received banner immediately from {ip}:{port}")
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
