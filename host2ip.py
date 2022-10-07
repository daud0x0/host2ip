#!/usr/bin/env python3

import sys
from socket import gethostbyname

for host in sys.stdin:
    try:
        print(gethostbyname(host.strip()))
    except: 
        pass
