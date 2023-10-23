
MYPORT = 10020
MYGROUP_4 = '224.5.23.2'

MYTTL = 1  # Increase to reach other networks

import time
import struct
import socket
import sys
import messages_robocup_ssl_wrapper_pb2
import math

def direcao(velocidade):
    if velocidade >= 0:
       return f"-{abs(velocidade):.2f}"  
    else:
       return f"{abs(velocidade):.2f}"  

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
    if addrinfo[0] == socket.AF_INET:  # IPv4
        mreq = group_bin + struct.pack('=I', socket.INADDR_ANY)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    else:
        mreq = group_bin + struct.pack('@I', 0)
        s.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_JOIN_GROUP, mreq)

    while True:
        data, sender = s.recvfrom(4096)
        wrapper = messages_robocup_ssl_wrapper_pb2.SSL_WrapperPacket()
        wrapper.ParseFromString(data)

        # Verifica se o campo de detecção está inicializado
        if wrapper.detection.IsInitialized():
            #print(wrapper.detection)
            if wrapper.detection.robots_yellow:
            # Procure o robô com o ID especificado
                robot_id_to_track = int(input("Insira o ID do robô yellow que deseja rastrear: "))
                robot_to_track = None

                for robot in wrapper.detection.robots_yellow:
                    if robot.robot_id == robot_id_to_track:
                        robot_to_track = robot
                        break

                if robot_to_track:
                    x_robot = robot_to_track.x
                    y_robot = robot_to_track.y
                    print(f"Rastreando Robô Amarelo {robot_id_to_track}: X={x_robot}, Y={y_robot}")

            if wrapper.detection.balls:
                ball = wrapper.detection.balls[0]
                bola_x = ball.x
                bola_y = ball.y

                angulos_das_rodas = [60, 135, 225, 300]
                velocidade_maxima = 2.5  
                distancia = math.sqrt((bola_x - x_robot)**2 + (bola_y - y_robot)**2)
                print(f"Distancia:{distancia}")
                if distancia > 0:
                   velocidade_x = (bola_x - x_robot) / distancia * velocidade_maxima
                   velocidade_y = (bola_y - y_robot) / distancia * velocidade_maxima
                else:
                   velocidade_x = 0
                   velocidade_y = 0
    
                velocidades_angulares = []
                for angulo in angulos_das_rodas:
                   print(f"Calculando.... \n{angulo}\n")
                   angulo_em_radianos = math.radians(angulo)
                   if distancia > 0:
                      velocidade_angular = (velocidade_x * math.cos(angulo_em_radianos) + velocidade_y * math.sin(angulo_em_radianos))
                   else:
                      velocidade_angular = 0
                   velocidades_angulares.append(velocidade_angular)
                print(velocidades_angulares)          
                for i, velocidade in enumerate(velocidades_angulares):
                   print(f"Roda {i+1}:")
                   print(f"Velocidade Angular: {abs(velocidade):.2f} rad/s")
                   print(f"Direção: {direcao(velocidade)}")
                   print()
            else: 
                pass

if __name__ == '__main__':
    main()