# Simulador que Cálcula o robô mais próximo da bola
<img src="https://i.ibb.co/VCRF8Lm/ray-so-export-21.png" alt="Importação das Bibliotecas">

## Importação de Bibliotecas:
Importa as bibliotecas necessárias para o desenvolvimento do jogo, incluindo o Pygame para a criação da interface gráfica.
Inicialização do Pygame e Definições de Tela:

## Inicializa o Pygame.
Define as dimensões da tela (800 pixels de largura por 600 pixels de altura).
Cria a janela do jogo com o título "Simulador de Futebol".

## Cores:
Define algumas cores usando o modelo RGB.

<img src="https://i.ibb.co/PtmbCXF/ray-so-export-22.png" alt="Numero de Robos">

## Número de Robôs:
Determina o número de robôs no jogo.

<img src="https://i.ibb.co/FnLRvy3/ray-so-export-23.png">

## Posições Iniciais dos Robôs e Bola:
Gera posições iniciais aleatórias para os robôs (dentro de uma faixa específica) e para a bola.

<img src="https://i.ibb.co/25ZHh00/ray-so-export-24.png">

## Velocidade dos Robôs:
Define a velocidade com que os robôs se movem.

<img src="https://i.ibb.co/NYz8zPw/ray-so-export-25.png">

## Carregamento de Imagens:
Carrega a imagem do robô (representada por 'horngirl.png') e obtém o retângulo correspondente.

<img src="https://i.ibb.co/SJJxQVQ/ray-so-export-26.png">

## Loop Principal e Eventos:
Inicia o loop principal do jogo.
Monitora eventos, como o fechamento da janela.


<img src="https://i.ibb.co/wywWVpW/ray-so-export-27.png">

## Encontrar Robô Mais Próximo:
Usa a função min com uma função lambda para encontrar o índice do robô mais próximo à bola, baseando-se na distância euclidiana.

<img src="https://i.ibb.co/82j8Swj/ray-so-export-28.png">

## Atualizar Posição do Robô Mais Próximo:
 - Calcula o ângulo entre a posição do robô mais próximo e a bola usando a função atan2.
 - Atualiza as coordenadas do robô mais próximo em direção à bola usando funções trigonométricas (cos e sin) para calcular as componentes X e Y do vetor de movimento.

<img src="https://i.ibb.co/jgmSwqn/ray-so-export-29.png">

## Verificar Toque do Robô na Bola:
 - Calcula a distância entre o robô mais próximo e a bola.
 - Se a distância for menor que 20, move a bola para uma nova posição aleatória.

<img src="https://i.ibb.co/dr5SPhY/ray-so-export-30.png">

## Desenhar Campo de Futebol:
 - Preenche a tela com a cor verde.
 - Desenha um retângulo branco representando o campo de futebol.

<img src="https://i.ibb.co/q0wWXbX/ray-so-export-31.png">

## Desenhar Robôs:
Itera sobre as posições dos robôs e desenha cada robô na tela.

<img src="https://i.ibb.co/q1hq7r3/ray-so-export-32.png">

## Desenhar Bola:
Desenha a bola na tela como um círculo azul.

<img src="https://i.ibb.co/tDRPjpD/ray-so-export-33.png">

## Atualizar a Tela:
Atualiza a tela do jogo.

<img src="https://i.ibb.co/B46S1Sk/ray-so-export-34.png">

## Fim do Loop Principal:
O loop continua indefinidamente até que o jogador feche a janela, encerrando o jogo.
