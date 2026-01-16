import ipaddress
network = ipaddress.IPv4Network("192.168.1.0/24")

print(f"Direccion de red: {network.network_address}")
print(f"Direccion de broadcast: {network.broadcast_address}")
print(f"Máscara de red: {network.netmask}")
print(f"Longitud prefijo: {network.prefixlen}")
print(f"Numero total direcciones: {network.num_addresses}")
print(f"Red con máscara de red: {network.with_netmask}")
print(f"Red con máscara de host: {network.with_hostmask}")