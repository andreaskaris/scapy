#! /usr/bin/env python3
from scapy.all import *
import sys, getopt

def main(argv):
    ip = ''
    mtu = ''
    try:
        opts, args = getopt.getopt(argv,"hi:m:",["ip=","mtu="])
    except getopt.GetoptError:
        print('icmp_frag_mtu.py -i <ip> -m <mtu>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('icmp_frag_mtu.py -i <ip> -m <mtu>')
            sys.exit()
        elif opt in ("-i", "--ip"):
            ip = arg
        elif opt in ("-m", "--mtu"):
            mtu = arg
    print('Sending the following packet to %s:' % ip)
    i=ICMP(type=3, code=4, nexthopmtu=int(mtu))
    i.display()
    send(IP(dst=ip)/i)

if __name__ == "__main__":
    main(sys.argv[1:])
