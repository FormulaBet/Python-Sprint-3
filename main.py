import pygame
import time
import math
from utils import escala_imagem, centro_de_rotacao, centralizar_texto
pygame.font.init()

grama = escala_imagem(pygame.image.load("imgs/grama.jpg"), 2.5)
pista = escala_imagem(pygame.image.load("imgs/pista.png"), 0.9)

borda_pista = escala_imagem(pygame.image.load("imgs/borda_pista.png"), 0.9)
mascara_pista = pygame.mask.from_surface(borda_pista)

chegada = pygame.image.load("imgs/chegada.png")
mascara_chegada = pygame.mask.from_surface(chegada)
posicao_chegada = (130, 250)

carro_vermelho = escala_imagem(pygame.image.load("imgs/carro_vermelho.png"), 0.07)
carro_roxo = escala_imagem(pygame.image.load("imgs/carro_roxo.png"), 0.07)

LARGURA, ALTURA = pista.get_width(), pista.get_height()
JANELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Corrida de Fórmula E!")

FONTE_PRINCIPAL = pygame.font.SysFont("modernno20", 50)

FPS = 60
CAMINHO = [(175, 119), (110, 70), (56, 133), (70, 481), (318, 731), (404, 680), (418, 521), (507, 475), (600, 551), (613, 715), (736, 713),
        (734, 399), (611, 357), (409, 343), (433, 257), (697, 258), (738, 123), (581, 71), (303, 78), (275, 377), (176, 388), (178, 260)]


class Info_jogo:
    NIVEIS = 10

    def __init__(self, nivel=1):
        self.nivel = nivel
        self.iniciado = False
        self.tempo_inicio_nivel = 0

    def proximo_nivel(self):
        self.nivel += 1
        self.iniciado = False

    def resetar(self):
        self.nivel = 1
        self.iniciado = False
        self.tempo_inicio_nivel = 0

    def jogo_finalizado(self):
        return self.nivel > self.NIVEIS

    def iniciar_nivel(self):
        self.iniciado = True
        self.tempo_inicio_nivel = time.time()

    def get_tempo_nivel(self):
        if not self.iniciado:
            return 0
        return round(time.time() - self.tempo_inicio_nivel)


class CarroGeral:
    def __init__(self, velocidade_max, velocidade_rotacao):
        self.img = self.IMG
        self.velocidade_max = velocidade_max
        self.velocidade = 0
        self.velocidade_rotacao = velocidade_rotacao
        self.angulo = 0
        self.x, self.y = self.POSICAO_INICIAL
        self.aceleracao = 0.1

    def rotacionar(self, esquerda=False, direita=False):
        if esquerda:
            self.angulo += self.velocidade_rotacao
        elif direita:
            self.angulo -= self.velocidade_rotacao

    def desenhar(self, janela):
        centro_de_rotacao(janela, self.img, (self.x, self.y), self.angulo)

    def mover_para_frente(self):
        self.velocidade = min(self.velocidade + self.aceleracao, self.velocidade_max)
        self.mover()

    def mover_para_tras(self):
        self.velocidade = max(self.velocidade - self.aceleracao, -self.velocidade_max/2)
        self.mover()

    def mover(self):
        radians = math.radians(self.angulo)
        vertical = math.cos(radians) * self.velocidade
        horizontal = math.sin(radians) * self.velocidade

        self.y -= vertical
        self.x -= horizontal

    def colidir(self, mascara, x=0, y=0):
        mascara_carro = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        poi = mascara.overlap(mascara_carro, offset)
        return poi

    def resetar(self):
        self.x, self.y = self.POSICAO_INICIAL
        self.angulo = 0
        self.velocidade = 0


class CarroJogador(CarroGeral):
    IMG = carro_vermelho
    POSICAO_INICIAL = (180, 200)

    def reduzir_velocidade(self):
        self.velocidade = max(self.velocidade - self.aceleracao / 2, 0)
        self.mover()

    def rebater(self):
        self.velocidade = -self.velocidade
        self.mover()


class CarroComputador(CarroGeral):
    IMG = carro_roxo
    POSICAO_INICIAL = (150, 200)

    def __init__(self, velocidade_max, velocidade_rotacao, caminho=[]):
        super().__init__(velocidade_max, velocidade_rotacao)
        self.caminho = caminho
        self.ponto_atual = 0
        self.velocidade = velocidade_max

        def desenhar_pontos(self, janela):
            for ponto in self.caminho:
                pygame.draw.circle(JANELA, (255, 0, 0), ponto, 5)

    def desenhar(self, janela):
        super().desenhar(janela)
        # self.desenhar_pontos(janela)

    def calcular_angulo(self):
        target_x, target_y = self.caminho[self.ponto_atual]
        x_diff = target_x - self.x
        y_diff = target_y - self.y

        if y_diff == 0:
            angulo_desejado_radianos = math.pi / 2
        else:
            angulo_desejado_radianos = math.atan(x_diff / y_diff)

        if target_y > self.y:
            angulo_desejado_radianos += math.pi

        diferenca_angulo = self.angulo - math.degrees(angulo_desejado_radianos)
        if diferenca_angulo >= 180:
            diferenca_angulo -= 360

        if diferenca_angulo > 0:
            self.angulo -= min(self.velocidade_rotacao, abs(diferenca_angulo))
        else:
            self.angulo += min(self.velocidade_rotacao, abs(diferenca_angulo))

    def atualizar_ponto_caminho(self):
        target = self.caminho[self.ponto_atual]
        rect = pygame.Rect(
            self.x, self.y, self.img.get_width(), self.img.get_height())
        if rect.collidepoint(*target):
            self.ponto_atual += 1

    def mover(self):
        if self.ponto_atual >= len(self.caminho):
            return

        self.calcular_angulo()
        self.atualizar_ponto_caminho()
        super().mover()

    def proximo_nivel(self, nivel):
        self.resetar()
        self.velocidade = self.velocidade_max + (nivel - 1) * 0.2
        self.ponto_atual = 0


def desenhar(janela, imagens, carro_jogador, carro_computador, info):
    for img, pos in imagens:
        janela.blit(img, pos)

    texto_nivel = FONTE_PRINCIPAL.render(
        f"Nível {info.nivel}", 1, (255, 255, 255))
    janela.blit(texto_nivel, (10, ALTURA - texto_nivel.get_height() - 70))

    texto_tempo = FONTE_PRINCIPAL.render(
        f"Tempo: {info.get_tempo_nivel()}s", 1, (255, 255, 255))
    janela.blit(texto_tempo, (10, ALTURA - texto_tempo.get_height() - 40))

    texto_velocidade = FONTE_PRINCIPAL.render(
        f"Vel: {round(carro_jogador.velocidade, 1)}px/s", 1, (255, 255, 255))
    janela.blit(texto_velocidade, (10, ALTURA - texto_velocidade.get_height() - 10))

    carro_jogador.desenhar(janela)
    carro_computador.desenhar(janela)
    pygame.display.update()


def mover_jogador(carro_jogador):
    teclas = pygame.key.get_pressed()
    movido = False

    if teclas[pygame.K_a]:
        carro_jogador.rotacionar(esquerda=True)
    if teclas[pygame.K_d]:
        carro_jogador.rotacionar(direita=True)
    if teclas[pygame.K_w]:
        movido = True
        carro_jogador.mover_para_frente()
    if teclas[pygame.K_s]:
        movido = True
        carro_jogador.mover_para_tras()

    if not movido:
        carro_jogador.reduzir_velocidade()


def lidar_colisao(carro_jogador, carro_computador, info):
    if carro_jogador.colidir(mascara_pista) != None:
        carro_jogador.rebater()

    ponto_colisao_computador = carro_computador.colidir(
        mascara_chegada, *posicao_chegada)
    if ponto_colisao_computador != None:
        centralizar_texto(JANELA, FONTE_PRINCIPAL, "Você perdeu!")
        pygame.display.update()
        pygame.time.wait(5000)
        info.resetar()
        carro_jogador.resetar()
        carro_computador.resetar()

    ponto_colisao_jogador = carro_jogador.colidir(
        mascara_chegada, *posicao_chegada)
    if ponto_colisao_jogador != None:
        if ponto_colisao_jogador[1] == 0:
            carro_jogador.rebater()
        else:
            info.proximo_nivel()
            carro_jogador.resetar()
            carro_computador.proximo_nivel(info.nivel)


executar = True
relogio = pygame.time.Clock()
imagens = [(grama, (0, 0)), (pista, (0, 0)),
          (chegada, posicao_chegada), (borda_pista, (0, 0))]
carro_jogador = CarroJogador(4, 4)
carro_computador = CarroComputador(2, 4, CAMINHO)
info = Info_jogo()

while executar:
    relogio.tick(FPS)

    if info.jogo_finalizado():
        centralizar_texto(JANELA, FONTE_PRINCIPAL, "Você ganhou!")
        pygame.display.update()
        pygame.time.wait(5000)
        executar = False  # Termina o loop do jogo
        break  # Sai do loop principal

    desenhar(JANELA, imagens, carro_jogador, carro_computador, info)

    while not info.iniciado:
        centralizar_texto(
            JANELA, FONTE_PRINCIPAL, f"Nível {info.nivel}!")
        pygame.display.update()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executar = False
                break

            if evento.type == pygame.KEYDOWN:
                info.iniciar_nivel()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executar = False
            break

    mover_jogador(carro_jogador)
    carro_computador.mover()

    lidar_colisao(carro_jogador, carro_computador, info)


pygame.quit()