import socket

# Ask user for target
target = input("Enter target IP address: ")

print("Scanning target:", target)
print("----------------------------")

# Scan ports 1 to 100
for port in range(1, 101):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown"
        print(f"Port {port} is OPEN (Service: {service})")

    else:
        print(f"Port {port} is CLOSED")

    s.close()