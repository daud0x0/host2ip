import socket

host = input("Enter your target:"))

ip = socket.gethostbyname(host)

print(f"Your target {host} ip is {ip}
