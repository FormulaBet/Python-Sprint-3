+---------------------------+
| Inicialização do Jogo      |
+---------------------------+
| - Carrega imagens          |
| - Inicializa fontes        |
| - Configura tela           |
| - Define parâmetros globais|
+---------------------------+
           |
           v
+---------------------------+
| Criação dos Objetos        |
+---------------------------+
| - Carro do jogador         |
| - Carro do computador      |
| - Informação do jogo       |
| (níveis, tempo, etc.)      |
+---------------------------+
           |
           v
+---------------------------+
| Laço Principal do Jogo     |
+---------------------------+
| - Captura eventos (teclado)|
| - Atualiza posição e estado|
| - Desenha objetos na tela  |
| - Detecta colisões         |
| - Gerencia níveis          |
+---------------------------+
           |
           v
+---------------------------+
| Lógica de Controle         |
+---------------------------+
| Controle do Carro Jogador: |
| - Acelerando, freando,     |
| - Girando, reduzindo vel.  |
+---------------------------+
| Controle do Carro IA:      |
| - Segue caminho pré-definido|
| - Calcula ângulo, move-se  |
| - Atualiza o ponto-alvo    |
+---------------------------+
           |
           v
+---------------------------+
| Detecção de Colisões       |
+---------------------------+
| - Verifica colisão com      |
|   borda, chegada e pista    |
| - Aplica penalidades        |
| - Avança nível ou reinicia  |
+---------------------------+
           |
           v
+---------------------------+
| Verificação de Condição    |
| Final do Jogo              |
+---------------------------+
| - Se jogador venceu:       |
|   "Você ganhou!"           |
| - Se jogador perdeu:       |
|   "Você perdeu!"           |
+---------------------------+
           |
           v
+---------------------------+
| Finalização do Jogo        |
+---------------------------+
| - Encerra Pygame           |
+---------------------------+
