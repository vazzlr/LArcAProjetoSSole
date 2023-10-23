#!/usr/bin/env python
#


MYPORT = 10020
MYGROUP_4 = '224.5.23.2'

MYTTL = 1 # Increase to reach other networks

import time
import struct
import socket
import sys
#import messages_robocup_ssl_detection_pb2 #as SSL_Detection
#import messages_robocup_ssl_geometry_pb2 #as SSL_Geometry
import messages_robocup_ssl_wrapper_pb2 #as SSL_WrapperPacket

def main():
    receiver(MYGROUP_4)

def receiver(group):
    # Look up multicast group address in name server and find out IP version
    addrinfo = socket.getaddrinfo(group, None)[0]

    # Create a socket
    s = socket.socket(addrinfo[0], socket.SOCK_DGRAM)

    # Allow multiple copies of this program on one machine
    # (not strictly needed)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind it to the port
    s.bind(('', MYPORT))

    group_bin = socket.inet_pton(addrinfo[0], addrinfo[4][0])
    # Join group
    if addrinfo[0] == socket.AF_INET: # IPv4
        mreq = group_bin + struct.pack('=I', socket.INADDR_ANY)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    else:
        mreq = group_bin + struct.pack('@I', 0)
        s.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_JOIN_GROUP, mreq)

    # Loop, printing any data we receive
    print("Cheguei aqui....")
    while True:
        print("Cheguei aqui....")
        data, sender = s.recvfrom(4096)
        print(f"Recebido pacote from {sender}")

        wrapper = messages_robocup_ssl_wrapper_pb2.SSL_WrapperPacket()
        wrapper.ParseFromString(data)

        # verifica se o campo de detecção está inicilizado
        if( wrapper.detection.IsInitialized()):
           if( wrapper.detection.balls is not None): # se existe bola, pode existir mais de 1
               for bola in wrapper.detection.balls:
                  print(f"Dados da bola {bola}")
           if( wrapper.detection.robots_yellow is not None): # vários robôs
               for roboY in wrapper.detection.robots_yellow:
                   print(f"Robo amarelo {roboY}")
           if( wrapper.detection.robots_blue is not None): # vários robôs
               for roboB in wrapper.detection.robots_blue:
                   print(f"Robo Azul {roboB}")
                   print(roboB.x,roboB.y)
        
if __name__ == '__main__':
    main()

