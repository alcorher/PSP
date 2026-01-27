import ipaddress

ip1 = ipaddress.IPv4Address("224.0.0.1")
ip2 = ipaddress.IPv4Address("192.168.1.10")


print("Ejercicio 1 ")

print("1.1")
print(f"IP 1: {ip1}")
print(f"Multicast {ip1.is_multicast}")
print(f"Privada {ip1.is_private}")
print(f"Publica {ip1.is_global}")
print(f"Reservada {ip1.is_reserved}")
print(f"Loopback {ip1.is_loopback}")
print(f"Uso local {ip1.is_link_local}")

print()

print(f"IP 2: {ip2}")
print(f"Multicast {ip2.is_multicast}")
print(f"Privada {ip2.is_private}")
print(f"Publica {ip2.is_global}")
print(f"Reservada {ip2.is_reserved}")
print(f"Loopback {ip2.is_loopback}")
print(f"Uso local {ip2.is_link_local}")

print()

print("1.2")
print(ip2)
print(f"IP siguiente: {ip2 + 1}")
print(f"IP anterior:  {ip2 - 1}")

print()

print("1.3")
if ip1 > ip2:
    print(f"{ip1} es mayor que {ip2}")
    print(f"{ip2} es menor que {ip1}")
else:
    print(f"{ip2} es mayor que {ip1}")
    print(f"{ip1} es menor que {ip2}")

