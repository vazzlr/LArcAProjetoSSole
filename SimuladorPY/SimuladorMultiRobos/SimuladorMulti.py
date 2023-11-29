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
red = (255, 0, 0)

# Número de robôs
num_robots = 5

# Posições iniciais dos robôs e bola
robot_positions = [[random.randint(50, 750), random.randint(50, 550)] for _ in range(num_robots)]
ball_pos = [random.randint(50, 750), random.randint(50, 550)]

# Velocidade dos robôs
robot_speed = 2

# Carregar imagens
robot_image = pygame.image.load('horngirl.png')  
robot_rect = robot_image.get_rect()

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Encontrar o robô mais próximo da bola
    closest_robot_index = min(range(num_robots), key=lambda i: math.sqrt((robot_positions[i][0] - ball_pos[0])**2 + (robot_positions[i][1] - ball_pos[1])**2))

    # Atualizar posição do robô mais próximo em direção à bola
    angle = math.atan2(ball_pos[1] - robot_positions[closest_robot_index][1], ball_pos[0] - robot_positions[closest_robot_index][0])
    robot_positions[closest_robot_index][0] += robot_speed * math.cos(angle)
    robot_positions[closest_robot_index][1] += robot_speed * math.sin(angle)

    # Verificar se o robô mais próximo tocou na bola
    distance_to_ball = math.sqrt((ball_pos[0] - robot_positions[closest_robot_index][0])**2 + (ball_pos[1] - robot_positions[closest_robot_index][1])**2)
    if distance_to_ball < 20:
        # Se o robô mais próximo tocou na bola, mova a bola para uma nova posição aleatória
        ball_pos = [random.randint(50, 750), random.randint(50, 550)]

    # Desenhar campo de futebol
    screen.fill(green)
    pygame.draw.rect(screen, white, (50, 50, width - 100, height - 100), 2)

    # Desenhar robôs
    for i in range(num_robots):
        robot_rect.center = (int(robot_positions[i][0]), int(robot_positions[i][1]))
        screen.blit(robot_image, robot_rect)

    # Desenhar bola
    pygame.draw.circle(screen, blue, (int(ball_pos[0]), int(ball_pos[1])), 10)

    # Atualizar a tela
    pygame.display.flip()

    # Controlar a taxa de quadros
    pygame.time.Clock().tick(60)
