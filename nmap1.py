import nmap

# https://nmap.org/download.html

# pip3 install python-nmap

scanner = nmap.PortScanner()

ip = input("Inserte una direccon ip: ")
print("Esta es la direccion ip que escribiste:", ip)
scanner.scan(ip)

print(scanner.all_hosts())

# Resultado:

# Inserte una direccon ip: 192.168.1.0/24
# Esta es la direccion ip que escribiste: 192.168.1.0/24
# ['192.168.1.1', '192.168.1.110', '192.168.1.123', '192.168.1.132', '192.168.1.140', '192.168.1.169', '192.168.1.190', '192.168.1.199', '192.168.1.224', '192.168.1.241', '192.168.1.244']



