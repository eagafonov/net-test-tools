#!/usr/bin/env python
from scapy.all import *
import time
import sys

vendor = "b8:e8:56:"
destMAC = "FF:FF:FF:FF:FF:FF"

def send_arp():
    randMAC = vendor + ':'.join(RandMAC().split(':')[3:])
    print randMAC
    sendp(Ether(src=randMAC ,dst=destMAC)/ARP(op=2, psrc="0.0.0.0", hwdst=destMAC)/Padding(load="X"*18),verbose=0)
    
count = 1 
delay = 0.3


if len(sys.argv) == 1:
    print("%s <count> [<delay>]" % sys.argv[0])
    sys.exit(0)


if len(sys.argv) > 1:
    count = int(sys.argv[1])

if len(sys.argv) > 2:
    delay = float(sys.argv[2])

    
assert count >= 1

for _ in xrange(count):
    send_arp()
    time.sleep(delay)



