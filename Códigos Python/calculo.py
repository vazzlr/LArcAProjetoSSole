
#CALCULO PITAGORICO X E Y

# import math

# # Coordenadas do ponto A (robô)
# robo_x = -1499.9638671875
# robo_y = -1120.0

# # Coordenadas do ponto B (bola)
# bola_x = 303.8662109375
# bola_y = 43.597900390625

# # Cálculo da distância entre os pontos A e B
# distancia = math.sqrt((bola_x - robo_x)**2 + (bola_y - robo_y)**2)

# # Supondo uma velocidade máxima constante do robô (em unidades de distância por segundo)
# velocidade_maxima = 2.5  # ajuste conforme necessário

# # Definindo a metade da distância
# metade_distancia = distancia / 2

# # Cálculo da velocidade proporcional
# if distancia > metade_distancia:
#     velocidade_atual = velocidade_maxima
# else:
#     velocidade_atual = velocidade_maxima * (distancia / metade_distancia)

# # Cálculo das velocidades separadas para as coordenadas X e Y
# velocidade_x = (bola_x - robo_x) / distancia * velocidade_atual
# velocidade_y = (bola_y - robo_y) / distancia * velocidade_atual

# print("Distância até a bola:", distancia)
# print("Velocidade X do robô:", velocidade_x, "m/s")
# print("Velocidade Y do robô:", velocidade_y, "m/s")

#-----------------------------------------------------------------

# É O QUE DEU CERTO ATÉ AGRRR, É SOBRE AS RODAS DAE


import math

# Coordenadas do ponto A (robô)
robo_x = -1499.9638671875
robo_y = -1120.0

# Coordenadas do ponto B (bola)
bola_x = 303.8662109375
bola_y = 43.597900390625

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
    velocidade_angular = (velocidade_x * math.cos(angulo_em_radianos) + velocidade_y * math.sin(angulo_em_radianos))
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

