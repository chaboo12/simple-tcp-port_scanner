# simple-tcp-port_scanner
Beginner cybersecurity project that scans a target system to identify open and closed ports and displays the associated services running on open ports. 

Description

This project is a simple TCP Port Scanner built using Python. The program scans a target system to check whether ports are open or closed. When an open port is found, the scanner also displays the commonly associated service running on that port.

This project demonstrates the basic concept of port scanning, which is widely used in network security and cybersecurity for identifying active services on a system.

Features

 .Scan ports on a target IP address

 .Identify open and closed ports

 .Display service names for open ports

 .Simple and beginner-friendly implementation

Technologies Used

 .Python 3

 .Socket Programming
 
How It Works

1.The user enters a target IP address.

2.The program scans a range of ports on the target system.

3.It attempts to establish a TCP connection to each port.

4.If the connection succeeds, the port is marked OPEN.

5.The scanner then displays the default service associated with that port.

Example Output

Enter target IP address: 127.0.0.1

Scanning target: 127.0.0.1
--------------------------------
Port 22 is OPEN (Service: ssh)
Port 80 is OPEN (Service: http)
Port 443 is OPEN (Service: https)
 
