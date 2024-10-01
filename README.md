# Python - Sprint 3

Este é um jogo simples de corrida desenvolvido em Python utilizando a biblioteca Pygame. O jogador controla um carro (carro vermelho) e compete contra um carro de computador (carro roxo) em um percurso com obstáculos. O objetivo é completar os níveis, evitando colisões e chegando à linha de chegada. O jogo é apenas um protótipo, contém alguns bugs que serão resolvidos para a Sprint 4!

- Link para vídeo de explicação: https://www.youtube.com/watch?v=QaySOTDh558
  NOTA: No final do vídeo, abrimos o jogo para uma demonstração da gameplay; no entanto, o gravador de tela não conseguiu capturar a janela do 'Pygame'. Por favor, considere apenas a explicação do código.
  
# Bibliotecas Necessárias:
- pygame: Biblioteca para desenvolvimento de jogos em Python.
- time: Manipulação facilitada de tempo
- Math: Cálculo de movimento

# Como Executar o Jogo

Clone o Repositório: Clone este repositório para a sua máquina.

Estrutura de Arquivos: Certifique-se de que as imagens necessárias estão no diretório imgs, com os seguintes arquivos:

- grama.jpg: Imagem do fundo.
- pista.png: Imagem da pista de corrida.
- borda_pista.png: Imagem da borda da pista.
- chegada.png: Imagem da linha de chegada.
- carro_vermelho.png: Imagem do carro do jogador.
- carro_roxo.png: Imagem do carro do computador.

Executar o Jogo: Execute o script Python:

python main.py

# Controles do Jogo
- Tecla W: Acelera o carro do jogador.
- Tecla S: Reverte o carro do jogador.
- Tecla A: Vira o carro do jogador para a esquerda.
- Tecla D: Vira o carro do jogador para a direita.


# Estrutura do Código
O código é organizado em várias classes e funções para gerenciar o estado do jogo e a interação entre os elementos:

Info_jogo: Classe que gerencia o estado do jogo, incluindo níveis e temporização.

CarroGeral: Classe base para os carros, com métodos para movimentação, rotação e colisão.

CarroJogador: Subclasse de CarroGeral, representando o carro controlado pelo jogador.

CarroComputador: Subclasse de CarroGeral, representando o carro controlado pelo computador, que segue um caminho pré-definido.

Funções de Renderização:

- desenhar(): Desenha os elementos do jogo na tela, incluindo o fundo, os carros e a interface do usuário.
- mover_jogador(): Lida com a entrada do teclado e movimenta o carro do jogador.
- lidar_colisao(): Verifica e gerencia colisões entre os carros e outros objetos.

  # Integrantes:
  - Leonardo de Farias
  - Giancarlo Cestarolli
  - Gustavo Laur
