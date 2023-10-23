

# MYPORT = 10020
# MYGROUP_4 = '224.5.23.2'

# MYTTL = 1  # Increase to reach other networks

# import time
# import struct
# import socket
# import sys
# import messages_robocup_ssl_wrapper_pb2


# def main():
#     receiver(MYGROUP_4)

# def receiver(group):
#     # Look up multicast group address in name server and find out IP version
#     addrinfo = socket.getaddrinfo(group, None)[0]

#     # Create a socket
#     s = socket.socket(addrinfo[0], socket.SOCK_DGRAM)

#     # Allow multiple copies of this program on one machine
#     # (not strictly needed)
#     s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#     # Bind it to the port
#     s.bind(('', MYPORT))

#     group_bin = socket.inet_pton(addrinfo[0], addrinfo[4][0])
#     # Join group
#     if addrinfo[0] == socket.AF_INET:  # IPv4
#         mreq = group_bin + struct.pack('=I', socket.INADDR_ANY)
#         s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
#     else:
#         mreq = group_bin + struct.pack('@I', 0)
#         s.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_JOIN_GROUP, mreq)

#     # Loop, printing any data we receive
#     while True:
#         data, sender = s.recvfrom(4096)
#         wrapper = messages_robocup_ssl_wrapper_pb2.SSL_WrapperPacket()
#         wrapper.ParseFromString(data)

#         # Verifica se o campo de detecção está inicializado
#         if wrapper.detection.IsInitialized():
#             # Escolhe um robô para rastrear (por exemplo, o primeiro robô detectado)
#             if wrapper.detection.robots_blue:
#                 robot_to_track = wrapper.detection.robots_blue[0]
#                 x = robot_to_track.x
#                 y = robot_to_track.y
#                 print(f"Rastreando Robô Azul: X={x}, Y={y}")

# if __name__ == '__main__':
#     main()

#####################################################################################################

                                    # ESSE DEU CERTOOOOOOOOOOOOOOOOO

# MYPORT = 10020
# MYGROUP_4 = '224.5.23.2'

# MYTTL = 1  # Increase to reach other networks

# import time
# import struct
# import socket
# import sys
# import messages_robocup_ssl_wrapper_pb2

# def main():
#     receiver(MYGROUP_4)

# def receiver(group):
#     # Look up multicast group address in name server and find out IP version
#     addrinfo = socket.getaddrinfo(group, None)[0]

#     # Create a socket
#     s = socket.socket(addrinfo[0], socket.SOCK_DGRAM)

#     # Allow multiple copies of this program on one machine
#     # (not strictly needed)
#     s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#     # Bind it to the port
#     s.bind(('', MYPORT))

#     group_bin = socket.inet_pton(addrinfo[0], addrinfo[4][0])
#     # Join group
#     if addrinfo[0] == socket.AF_INET:  # IPv4
#         mreq = group_bin + struct.pack('=I', socket.INADDR_ANY)
#         s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
#     else:
#         mreq = group_bin + struct.pack('@I', 0)
#         s.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_JOIN_GROUP, mreq)

#     # Solicite ao usuário que insira o ID do robô a ser rastreado
#     robot_id_to_track = int(input("Insira o ID do robô que deseja rastrear: "))

#     # Loop, printing any data we receive
#     while True:
#         data, sender = s.recvfrom(4096)
#         wrapper = messages_robocup_ssl_wrapper_pb2.SSL_WrapperPacket()
#         wrapper.ParseFromString(data)

#         # Verifica se o campo de detecção está inicializado
#         if wrapper.detection.IsInitialized():
#             # Procure o robô com o ID especificado
#             robot_to_track = None
#             for robot in wrapper.detection.robots_blue:
#                 if robot.robot_id == robot_id_to_track:
#                     robot_to_track = robot
#                     break

#             if robot_to_track:
#                 x = robot_to_track.x
#                 y = robot_to_track.y
#                 print(f"Rastreando Robô Azul {robot_id_to_track}: X={x}, Y={y}")

# if __name__ == '__main__':
#     main()

#################################################################################################3

#!/usr/bin/env python

MYPORT = 10020
MYGROUP_4 = '224.5.23.2'

MYTTL = 1  # Increase to reach other networks

import time
import struct
import socket
import sys
import messages_robocup_ssl_wrapper_pb2
import math

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
            # Procure o robô com o ID especificado
            robot_id_to_track = int(input("Insira o ID do robô que deseja rastrear: "))
            robot_to_track = None
            for robot in wrapper.detection.robots_blue:
                if robot.robot_id == robot_id_to_track:
                    robot_to_track = robot
                    break

            if robot_to_track:
                x_robot = robot_to_track.x
                y_robot = robot_to_track.y
                print(f"Rastreando Robô Azul {robot_id_to_track}: X={x_robot}, Y={y_robot}")

                # Use as coordenadas do robô como as coordenadas reais
                robo_x = x_robot
                robo_y = y_robot

                if wrapper.detection.balls:
                    ball = wrapper.detection.balls[0]
                    bola_x = ball.x
                    bola_y = ball.y

                    # Ângulos das rodas (em graus)
                    angulos_das_rodas = [60, 135, 225, 300]

                    # Suponha uma velocidade máxima constante do robô (em m/s)
                    velocidade_maxima = 2.5  # Ajuste conforme necessário

                    # Cálculo da distância entre os pontos A e B
                    distancia = math.sqrt((bola_x - robo_x)**2 + (bola_y - robo_y)**2)

                    # Cálculo da velocidade necessária na direção X e Y para ir em direção à bola
                    if distancia > 0:
                        velocidade_x = (bola_x - robo_x) / distancia * velocidade_maxima
                        velocidade_y = (bola_y - robo_y) / distancia * velocidade_maxima
                    else:
                        velocidade_x = 0
                        velocidade_y = 0

                    # Calcula as velocidades angulares necessárias para todas as rodas
                    velocidades_angulares = []

                    for angulo in angulos_das_rodas:
                        angulo_em_radianos = math.radians(angulo)
                        if distancia > 0:
                            velocidade_angular = (velocidade_x * math.cos(angulo_em_radianos) + velocidade_y * math.sin(angulo_em_radianos))
                        else:
                            velocidade_angular = 0
                        velocidades_angulares.append(velocidade_angular)

                    # Função para determinar a direção (sentido horário ou anti-horário)
                    def direcao(velocidade):
                        if velocidade >= 0:
                            return f"-{abs(velocidade):.2f}"  # Sentido horário com "-" antes do número
                        else:
                            return f"{abs(velocidade):.2f}"   # Sentido anti-horário apenas número positivo

                    # Exibe as velocidades e direções de cada roda
                    for i, velocidade in enumerate(velocidades_angulares):
                        print(f"Roda {i+1}:")
                        print(f"Velocidade Angular: {abs(velocidade):.2f} rad/s")
                        print(f"Direção: {direcao(velocidade)}")
                        print()

if __name__ == '__main__':
    main()


################################################################################

# import struct
# import socket
# import messages_robocup_ssl_wrapper_pb2

# def main():
#     MYPORT = 10020
#     MYGROUP_4 = '224.5.23.2'
#     receiver(MYPORT, MYGROUP_4)

# def receiver(port, group):
#     addrinfo = socket.getaddrinfo(group, None)[0]
#     s = socket.socket(addrinfo[0], socket.SOCK_DGRAM)
#     s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     s.bind(('', port))
#     group_bin = socket.inet_pton(addrinfo[0], addrinfo[4][0])

#     if addrinfo[0] == socket.AF_INET:
#         mreq = group_bin + struct.pack('=I', socket.INADDR_ANY)
#         s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
#     else:
#         mreq = group_bin + struct.pack('@I', 0)
#         s.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_JOIN_GROUP, mreq)

#     # Solicite ao usuário que insira o ID do robô a ser rastreado
#     robot_id_to_track = int(input("Insira o ID do robô que deseja rastrear: "))

#     while True:
#         data, sender = s.recvfrom(4096)
#         wrapper = messages_robocup_ssl_wrapper_pb2.SSL_WrapperPacket()
#         wrapper.ParseFromString(data)

#         if wrapper.detection.IsInitialized():
#             # Procure o robô com o ID especificado
#             robot_to_track = None
#             for robot in wrapper.detection.robots_blue:
#                 if robot.robot_id == robot_id_to_track:
#                     robot_to_track = robot
#                     break

#             if robot_to_track:
#                 x = robot_to_track.x
#                 y = robot_to_track.y
#                 print(f"Rastreando Robô Azul {robot_id_to_track}: X={x}, Y={y}")

# if __name__ == '__main__':
#     main()
