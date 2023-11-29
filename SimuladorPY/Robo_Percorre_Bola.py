import pygame
import sys
import math
import random

# Inicialização do Pygame
pygame.init()

# Definições de tela
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simulador de Futebol')

# Cores
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)

# Posições iniciais
robot_pos = [100, 300]
ball_pos = [400, 300]

# Velocidades iniciais
robot_speed = 2
ball_speed = 3

# Carregar imagens
robot_image = pygame.image.load('horngirl.png')  
robot_rect = robot_image.get_rect()

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualizar posição do robô em direção à bola
    angle = math.atan2(ball_pos[1] - robot_pos[1], ball_pos[0] - robot_pos[0])
    robot_pos[0] += robot_speed * math.cos(angle)
    robot_pos[1] += robot_speed * math.sin(angle)

    # Verificar se o robô tocou na bola
    distance_to_ball = math.sqrt((ball_pos[0] - robot_pos[0])**2 + (ball_pos[1] - robot_pos[1])**2)
    if distance_to_ball < 20:
        # Se o robô tocou na bola, mova a bola para uma nova posição aleatória
        ball_pos = [random.randint(100, 700), random.randint(100, 500)]

    # Desenhar campo de futebol
    screen.fill(green)
    pygame.draw.rect(screen, white, (50, 50, width - 100, height - 100), 2)

    # Desenhar robô
    robot_rect.center = (int(robot_pos[0]), int(robot_pos[1]))
    screen.blit(robot_image, robot_rect)

    # Desenhar bola
    pygame.draw.circle(screen, blue, (int(ball_pos[0]), int(ball_pos[1])), 10)

    # Atualizar a tela
    pygame.display.flip()

    # Controlar a taxa de quadros
    pygame.time.Clock().tick(60)
