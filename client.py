#!/usr/bin/env python
import socket
import subprocess
import sys
import re
from datetime import datetime


def measure_time(fun):
    def inner(*args):
        t = datetime.now()
        fun(*args)
        print(f"Finished in {datetime.now() - t}")
    return inner

def resolve(IP): return IP if re.fullmatch("\d+.\d+.\d+.\d+", IP) else socket.gethostbyname(IP)

@measure_time
def scan(IP, interval = (1,65535)):
    try:
        for port in range(*interval):  
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((server, port))
            if result == 0:
                print(f"Port {port} is open")
            sock.close()

    except KeyboardInterrupt:
        print("canceled")
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

if __name__ == '__main__':
    subprocess.call('clear', shell=True)
    server = resolve(sys.argv[1] if len(sys.argv) > 1 else input("Enter a host to scan: "))
    print("wait, scanning host ports", server, end="\n\n")
    scan(server, (int(sys.argv[2]), int(sys.argv[3]))) if len(sys.argv) >= 4 else scan(server)

