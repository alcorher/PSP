import ipaddress
network1 = ipaddress.IPv4Network('192.168.1.0/24')
network2 = ipaddress.IPv4Network('192.168.0.0/16')

print(f"Network 1 : {network1}")
print(f"Network 2: {network2}")

print(f"Se solapan: {network1.overlaps(network2)}")
print(f"Es {network1} subred de {network2} : {network1.subnet_of(network2)}")
print(f"Es {network1} superred de {network2} : {network1.supernet_of(network2)}")
print(f"{network1} comparada con {network2}")
print(network1.compare_networks(network2))