<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=85C1E9&height=120&section=header"/>

> [!NOTE]
> Simulador em Python de um robô que segue a direção da bola, usando cálculos Trigonométricos

# 1. Inicialização do Pygame e Definição da Tela
<img src="https://i.ibb.co/jDnHYPz/ray-so-export-15.png" alt="Inicialização do Pygame e Definição da Tela">

### Aqui, eu inicializo a biblioteca Pygame e configuro a janela do simulador de futebol. A tela possui uma largura (width) de 800 pixels e uma altura (height) de 600 pixels.

# 2. Cores e Posições Iniciais
<img src="https://i.ibb.co/mv12M18/ray-so-export-16.png" alt="Cores e Posições Iniciais">

### Aqui, eu defino algumas cores em formato RGB (branco, verde e azul) e as posições iniciais do robô (posicao_robo) e da bola (posicao_bola).

# 3. Velocidades Iniciais e Carregamento de Imagens
<img src="https://i.ibb.co/25xQKJS/ray-so-export-17.png" alt="Velocidades Iniciais e Carregamento de Imagens">

### Eu defino as velocidades iniciais do robô e da bola. Além disso, eu carrego uma imagem para representar o robô e obtenho o retângulo que a envolve.

# 4. Loop Principal
<img src="https://i.ibb.co/L0Ywrr5/ray-so-export-18.png" alt="Loop Principal">

### Eu inicio o loop principal que executa indefinidamente. Dentro desse loop, eu verifico eventos do Pygame, como a tentativa de fechar a janela.

# 5. Atualização da Posição do Robô em Direção à Bola
<img src="https://i.ibb.co/kXwgHgN/ray-so-export-19.png" alt="Atualização da Posição do Robô em Direção à Bola">

### Eu calculo o ângulo entre minha posição e a posição da bola usando funções trigonométricas. Em seguida, eu atualizo minhas coordenadas com base nesse ângulo, movendo-me em direção à bola.

# Código Completo:
<img src="https://i.ibb.co/N7mV5zV/ray-so-export-20.png" alt="Código Completo">

  <img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=85C1E9&height=120&section=footer"/>
