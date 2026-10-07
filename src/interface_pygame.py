import sys
import math
import random
import pygame

from .guerreiro import Guerreiro
from .mago import Mago
from .arqueiro import Arqueiro
from .inimigo import Inimigo
from .orc import Orc
from .chefe_final import ChefeFinal
from .item import Pocao_de_vida
from .batalha import Batalha

# ============================================================
# CONFIGURAÇÕES
# ============================================================

LARGURA = 800
ALTURA = 600
FPS = 60

FUNDO = (25, 25, 40)
BRANCO = (255, 255, 255)
VERMELHO = (230, 60, 60)
VERDE = (70, 210, 100)
AZUL = (70, 130, 240)
PELE = (240, 200, 160)

CLASSES = {"Guerreiro": Guerreiro, "Mago": Mago, "Arqueiro": Arqueiro}

SKINS = {
    "Guerreiro": [(60, 110, 220), (200, 60, 60)],
    "Mago": [(130, 60, 200), (40, 160, 90)],
    "Arqueiro": [(40, 150, 70), (150, 100, 50)],
}

STATS_TEXTO = {
    "Guerreiro": "Vida 120 | Atq 20 | Def 15",
    "Mago": "Vida 80 | Atq 30 | Def 5",
    "Arqueiro": "Vida 90 | Atq 25 | Def 8",
}

ESCALAS = {"Orc": 1.1, "Dragão Ancião": 1.4}

CHAO_Y = 385          # altura dos pés dos personagens
POS_JOGADOR_X = 180
POS_INIMIGO_X = 620
DURACAO_ANIMACAO = 40  # frames


# ============================================================
# DESENHO DOS PERSONAGENS (tudo com formas, sem imagens)
# Cada função desenha numa superfície de 200x200.
# Os pés ficam em y=190 e o personagem olha para a direita.
# ============================================================

def escurecer(cor):
    """Retorna a mesma cor, mais escura."""
    return (int(cor[0] * 0.6), int(cor[1] * 0.6), int(cor[2] * 0.6))


def desenhar_guerreiro(s, cor):
    metal = (170, 170, 185)
    pygame.draw.rect(s, (60, 60, 75), (80, 150, 14, 40))
    pygame.draw.rect(s, (60, 60, 75), (106, 150, 14, 40))
    pygame.draw.rect(s, cor, (72, 90, 56, 70), border_radius=8)
    pygame.draw.circle(s, PELE, (100, 70), 20)
    pygame.draw.rect(s, metal, (80, 48, 40, 20), border_radius=8)
    pygame.draw.circle(s, (30, 30, 40), (93, 74), 3)
    pygame.draw.circle(s, (30, 30, 40), (107, 74), 3)
    pygame.draw.rect(s, (210, 210, 220), (140, 40, 8, 110))
    pygame.draw.rect(s, (120, 80, 30), (130, 118, 28, 7))
    pygame.draw.ellipse(s, metal, (45, 100, 32, 52))
    pygame.draw.ellipse(s, cor, (52, 112, 18, 28))


def desenhar_mago(s, cor):
    escuro = escurecer(cor)
    pygame.draw.polygon(s, cor, [(100, 75), (60, 190), (140, 190)])
    pygame.draw.circle(s, PELE, (100, 72), 18)
    pygame.draw.circle(s, (30, 30, 40), (94, 74), 3)
    pygame.draw.circle(s, (30, 30, 40), (106, 74), 3)
    pygame.draw.polygon(s, escuro, [(100, 5), (76, 56), (124, 56)])
    pygame.draw.rect(s, escuro, (68, 52, 64, 8), border_radius=3)
    pygame.draw.rect(s, (120, 80, 30), (145, 45, 6, 145))
    pygame.draw.circle(s, (120, 220, 255), (148, 40), 13)
    pygame.draw.circle(s, BRANCO, (144, 36), 4)


def desenhar_arqueiro(s, cor):
    escuro = escurecer(cor)
    marrom = (120, 80, 30)
    pygame.draw.rect(s, (70, 50, 30), (82, 150, 13, 40))
    pygame.draw.rect(s, (70, 50, 30), (105, 150, 13, 40))
    pygame.draw.rect(s, cor, (74, 92, 52, 62), border_radius=8)
    pygame.draw.circle(s, PELE, (100, 72), 18)
    pygame.draw.polygon(s, escuro, [(100, 40), (76, 80), (124, 80), (118, 55)])
    pygame.draw.circle(s, (30, 30, 40), (94, 74), 3)
    pygame.draw.circle(s, (30, 30, 40), (106, 74), 3)
    pygame.draw.arc(s, marrom, (110, 50, 50, 120), -math.pi / 2, math.pi / 2, 5)
    pygame.draw.line(s, (230, 230, 230), (135, 50), (135, 170), 2)
    pygame.draw.line(s, (200, 200, 200), (100, 110), (150, 110), 3)
    pygame.draw.polygon(s, (200, 200, 200), [(150, 104), (162, 110), (150, 116)])


def desenhar_goblin(s, cor=None):
    verde = (90, 170, 70)
    pygame.draw.rect(s, (70, 130, 55), (84, 165, 12, 25))
    pygame.draw.rect(s, (70, 130, 55), (104, 165, 12, 25))
    pygame.draw.ellipse(s, verde, (72, 115, 56, 62))
    pygame.draw.circle(s, verde, (100, 108), 25)
    pygame.draw.polygon(s, verde, [(78, 102), (40, 85), (80, 122)])
    pygame.draw.polygon(s, verde, [(122, 102), (160, 85), (120, 122)])
    pygame.draw.circle(s, (230, 40, 40), (91, 104), 5)
    pygame.draw.circle(s, (230, 40, 40), (109, 104), 5)
    pygame.draw.line(s, (30, 60, 25), (90, 120), (110, 120), 3)
    pygame.draw.rect(s, (200, 200, 210), (135, 130, 6, 38))
    pygame.draw.rect(s, (120, 80, 30), (131, 166, 14, 6))


def desenhar_orc(s, cor=None):
    verde = (70, 120, 60)
    pygame.draw.rect(s, (50, 90, 45), (76, 150, 20, 40))
    pygame.draw.rect(s, (50, 90, 45), (104, 150, 20, 40))
    pygame.draw.rect(s, verde, (60, 78, 80, 80), border_radius=10)
    pygame.draw.rect(s, (110, 80, 40), (60, 110, 80, 10))
    pygame.draw.circle(s, verde, (100, 58), 26)
    pygame.draw.circle(s, (250, 220, 40), (91, 54), 5)
    pygame.draw.circle(s, (250, 220, 40), (109, 54), 5)
    pygame.draw.polygon(s, BRANCO, [(88, 72), (84, 56), (95, 70)])
    pygame.draw.polygon(s, BRANCO, [(112, 72), (116, 56), (105, 70)])
    pygame.draw.rect(s, (120, 80, 30), (150, 40, 9, 150))
    pygame.draw.polygon(s, (190, 190, 200), [(159, 45), (190, 60), (190, 100), (159, 90)])


def desenhar_dragao(s, cor=None):
    vermelho = (190, 40, 40)
    escuro = (120, 25, 25)
    pygame.draw.polygon(s, escuro, [(90, 100), (60, 20), (110, 50), (130, 10), (140, 100)])
    pygame.draw.polygon(s, vermelho, [(60, 140), (5, 170), (10, 185), (70, 170)])
    pygame.draw.rect(s, escuro, (70, 165, 16, 25))
    pygame.draw.rect(s, escuro, (115, 165, 16, 25))
    pygame.draw.ellipse(s, vermelho, (45, 100, 110, 80))
    pygame.draw.ellipse(s, (230, 170, 90), (60, 130, 80, 40))
    pygame.draw.polygon(s, vermelho, [(125, 110), (150, 60), (170, 70), (150, 130)])
    pygame.draw.ellipse(s, vermelho, (140, 48, 52, 34))
    pygame.draw.polygon(s, escuro, [(150, 52), (145, 28), (162, 48)])
    pygame.draw.circle(s, (250, 230, 40), (174, 58), 5)
    pygame.draw.circle(s, (20, 20, 20), (175, 58), 2)
    pygame.draw.polygon(s, (255, 150, 30), [(190, 64), (199, 70), (190, 78)])


DESENHOS_JOGADOR = {
    "Guerreiro": desenhar_guerreiro,
    "Mago": desenhar_mago,
    "Arqueiro": desenhar_arqueiro,
}

DESENHOS_INIMIGOS = {
    "Goblin": desenhar_goblin,
    "Orc": desenhar_orc,
    "Dragão Ancião": desenhar_dragao,
}


def criar_sprite(funcao, cor=None, espelhar=False, escala=1.0):
    """Desenha o personagem numa superfície transparente e a devolve pronta."""
    sprite = pygame.Surface((200, 200), pygame.SRCALPHA)
    funcao(sprite, cor)
    if espelhar:
        sprite = pygame.transform.flip(sprite, True, False)
    if escala != 1.0:
        tamanho = int(200 * escala)
        sprite = pygame.transform.smoothscale(sprite, (tamanho, tamanho))
    return sprite


# ============================================================
# CLASSES AUXILIARES
# ============================================================

class CapturaPrint:
    """Guarda os print() das classes do jogo para mostrar no log da tela."""

    def __init__(self):
        self.linhas = []

    def write(self, texto):
        for linha in texto.split("\n"):
            if linha.strip() != "":
                self.linhas.append(linha.strip())

    def flush(self):
        pass


class Botao:

    def __init__(self, texto, x, y, largura=140, altura=44):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.texto = texto
        self.ativo = True

    def desenhar(self, tela, fonte):
        mouse = pygame.mouse.get_pos()
        if not self.ativo:
            cor = (60, 60, 70)
        elif self.rect.collidepoint(mouse):
            cor = (90, 120, 200)
        else:
            cor = (60, 80, 150)
        pygame.draw.rect(tela, cor, self.rect, border_radius=8)
        pygame.draw.rect(tela, BRANCO, self.rect, 2, border_radius=8)
        imagem = fonte.render(self.texto, True, BRANCO)
        tela.blit(imagem, imagem.get_rect(center=self.rect.center))

    def clicado(self, posicao):
        return self.ativo and self.rect.collidepoint(posicao)


class TextoFlutuante:
    """Número de dano ou cura que sobe e vai sumindo."""

    def __init__(self, texto, x, y, cor):
        self.texto = texto
        self.x = x
        self.y = y
        self.cor = cor
        self.vida = 60

    def atualizar(self):
        self.y -= 1
        self.vida -= 1

    def desenhar(self, tela, fonte):
        imagem = fonte.render(self.texto, True, self.cor)
        imagem.set_alpha(min(255, self.vida * 6))
        tela.blit(imagem, (self.x, self.y))


def desenhar_barra(tela, x, y, largura, atual, maximo, cor):
    proporcao = max(0, atual) / maximo
    pygame.draw.rect(tela, (50, 50, 60), (x, y, largura, 20), border_radius=4)
    pygame.draw.rect(tela, cor, (x, y, int(largura * proporcao), 20), border_radius=4)
    pygame.draw.rect(tela, BRANCO, (x, y, largura, 20), 2, border_radius=4)


# ============================================================
# JOGO
# ============================================================

class Jogo:

    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Jogo de Batalha")
        self.relogio = pygame.time.Clock()
        self.fonte = pygame.font.Font(None, 28)
        self.fonte_pequena = pygame.font.Font(None, 24)
        self.fonte_grande = pygame.font.Font(None, 56)

        # Os print() das classes vão para o log da tela
        self.captura = CapturaPrint()
        sys.stdout = self.captura

        self.rodando = True
        self.tempo = 0
        self.textos = []
        self.tela_atual = "escolha_classe"

        # Pré-visualizações da tela de escolha
        self.previas = {}
        self.botoes_classe = []
        posicao = 0
        for nome in CLASSES:
            self.previas[nome] = criar_sprite(DESENHOS_JOGADOR[nome], SKINS[nome][0])
            centro_x = 140 + posicao * 260
            self.botoes_classe.append((nome, Botao(nome, centro_x - 80, 450, 160, 44)))
            posicao += 1

        self.botao_reiniciar = Botao("Jogar de novo", 330, 420, 140, 44)

    # --------------------------------------------------------
    # PREPARAÇÃO
    # --------------------------------------------------------

    def ir_para_skin(self, nome_classe):
        self.classe_escolhida = nome_classe
        self.opcoes_skin = []
        posicao = 0
        for cor in SKINS[nome_classe]:
            sprite = criar_sprite(DESENHOS_JOGADOR[nome_classe], cor)
            centro_x = 270 + posicao * 260
            retangulo = pygame.Rect(centro_x - 110, 190, 220, 220)
            self.opcoes_skin.append((cor, sprite, retangulo))
            posicao += 1
        self.tela_atual = "escolha_skin"

    def iniciar_jogo(self, cor):
        nome_classe = self.classe_escolhida
        self.jogador = CLASSES[nome_classe](nome_classe)
        self.jogador.inventario.append(Pocao_de_vida("Poção de Vida", 20, 30))

        self.inimigos = [
            Inimigo("Goblin", 100, 15, 5),
            Orc("Orc"),
            ChefeFinal("Dragão Ancião"),
        ]
        self.indice = 0
        self.batalha = Batalha(self.jogador, self.inimigos[0])

        self.sprite_jogador = criar_sprite(DESENHOS_JOGADOR[nome_classe], cor)
        self.sprites_inimigos = {}
        for nome_inimigo in DESENHOS_INIMIGOS:
            escala = ESCALAS.get(nome_inimigo, 1.0)
            self.sprites_inimigos[nome_inimigo] = criar_sprite(
                DESENHOS_INIMIGOS[nome_inimigo], None, True, escala)

        # Botões de ação
        nomes = [("atacar", "Atacar"), ("item", "Usar item")]
        if hasattr(self.jogador, "usar_magia"):
            nomes.append(("magia", "Magia"))
        nomes.append(("fugir", "Fugir"))

        self.botoes_acao = []
        posicao = 0
        for acao, texto in nomes:
            self.botoes_acao.append((acao, Botao(texto, 90 + posicao * 160, 420)))
            posicao += 1

        # Estado e animação
        self.estado = "espera"   # espera, anim_jogador, anim_inimigo, morte_inimigo, fim
        self.timer = 0
        self.acao_atual = ""
        self.mensagem_final = ""
        self.deslocamento_jogador = 0
        self.deslocamento_inimigo = 0
        self.tremor_jogador = 0
        self.tremor_inimigo = 0
        self.vida_exibida_jogador = self.jogador.vida
        self.vida_exibida_inimigo = self.batalha.inimigo.vida
        self.captura.linhas = []
        self.textos = []
        self.tela_atual = "batalha"

    def reiniciar(self):
        self.captura.linhas = []
        self.textos = []
        self.tela_atual = "escolha_classe"

    # --------------------------------------------------------
    # EVENTOS
    # --------------------------------------------------------

    def tratar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                self.rodando = False
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                self.tratar_clique(evento.pos)

    def tratar_clique(self, posicao):
        if self.tela_atual == "escolha_classe":
            for nome, botao in self.botoes_classe:
                if botao.clicado(posicao):
                    self.ir_para_skin(nome)

        elif self.tela_atual == "escolha_skin":
            for cor, sprite, retangulo in self.opcoes_skin:
                if retangulo.collidepoint(posicao):
                    self.iniciar_jogo(cor)

        elif self.tela_atual == "batalha":
            if self.estado == "espera":
                for acao, botao in self.botoes_acao:
                    if botao.clicado(posicao):
                        self.clicar_acao(acao)
            elif self.estado == "fim":
                if self.botao_reiniciar.clicado(posicao):
                    self.reiniciar()

    def clicar_acao(self, acao):
        if acao == "fugir":
            self.captura.linhas.append("Você fugiu da batalha!")
            self.mensagem_final = "Você fugiu..."
            self.estado = "fim"
            return

        if acao == "item" and len(self.jogador.inventario) == 0:
            self.captura.linhas.append("Você não possui itens.")
            return  # Não gasta o turno

        if acao == "magia" and self.jogador.mana < 20:  # 20 = custo da magia
            self.captura.linhas.append(f"{self.jogador.nome} não possui mana suficiente.")
            return  # Não gasta o turno

        self.acao_atual = acao
        self.timer = 0
        self.estado = "anim_jogador"

    # --------------------------------------------------------
    # ATUALIZAÇÃO
    # --------------------------------------------------------

    def atualizar(self):
        self.tempo += 1

        restantes = []
        for texto in self.textos:
            texto.atualizar()
            if texto.vida > 0:
                restantes.append(texto)
        self.textos = restantes

        if self.tela_atual != "batalha":
            return

        # Barras de vida suaves
        self.vida_exibida_jogador += (self.jogador.vida - self.vida_exibida_jogador) * 0.1
        inimigo = self.batalha.inimigo
        self.vida_exibida_inimigo += (inimigo.vida - self.vida_exibida_inimigo) * 0.1

        if self.estado == "anim_jogador":
            self.atualizar_anim_jogador()
        elif self.estado == "anim_inimigo":
            self.atualizar_anim_inimigo()
        elif self.estado == "morte_inimigo":
            self.atualizar_morte_inimigo()

    def atualizar_anim_jogador(self):
        self.timer += 1
        proporcao = self.timer / DURACAO_ANIMACAO
        if self.acao_atual != "item":
            self.deslocamento_jogador = math.sin(math.pi * proporcao) * 90

        if self.timer == DURACAO_ANIMACAO // 2:
            self.executar_acao_jogador()

        if self.timer >= DURACAO_ANIMACAO:
            self.deslocamento_jogador = 0
            self.timer = 0
            if self.batalha.inimigo.esta_vivo():
                self.estado = "anim_inimigo"
            else:
                self.estado = "morte_inimigo"

    def executar_acao_jogador(self):
        inimigo = self.batalha.inimigo
        vida_inimigo_antes = inimigo.vida
        vida_jogador_antes = self.jogador.vida

        if self.acao_atual == "atacar":
            self.batalha.jogador_atacar()
        elif self.acao_atual == "magia":
            self.batalha.jogador_usar_magia()
        elif self.acao_atual == "item":
            self.batalha.jogador_usar_item(0)

        dano = vida_inimigo_antes - inimigo.vida
        if dano > 0:
            self.textos.append(TextoFlutuante(f"-{dano}", POS_INIMIGO_X - 20, 220, VERMELHO))
            self.tremor_inimigo = 15

        cura = self.jogador.vida - vida_jogador_antes
        if cura > 0:
            self.textos.append(TextoFlutuante(f"+{cura}", POS_JOGADOR_X - 20, 220, VERDE))

    def atualizar_anim_inimigo(self):
        self.timer += 1
        proporcao = self.timer / DURACAO_ANIMACAO
        self.deslocamento_inimigo = -math.sin(math.pi * proporcao) * 90

        if self.timer == DURACAO_ANIMACAO // 2:
            vida_antes = self.jogador.vida
            self.batalha.turno_inimigo()
            dano = vida_antes - self.jogador.vida
            if dano > 0:
                self.textos.append(TextoFlutuante(f"-{dano}", POS_JOGADOR_X - 20, 220, VERMELHO))
                self.tremor_jogador = 15

        if self.timer >= DURACAO_ANIMACAO:
            self.deslocamento_inimigo = 0
            self.timer = 0
            if self.jogador.esta_vivo():
                self.estado = "espera"
            else:
                self.mensagem_final = f"DERROTA... {self.batalha.inimigo.nome} venceu."
                self.estado = "fim"

    def atualizar_morte_inimigo(self):
        self.timer += 1
        if self.timer >= 40:
            self.proxima_batalha()

    def proxima_batalha(self):
        self.captura.linhas.append(f"{self.batalha.inimigo.nome} foi derrotado!")
        self.indice += 1

        if self.indice == len(self.inimigos):
            self.mensagem_final = "PARABÉNS! Você venceu todos os inimigos!"
            self.estado = "fim"
            return

        self.jogador.inventario.append(Pocao_de_vida("Poção de Vida", 20, 30))
        self.captura.linhas.append(f"{self.jogador.nome} recebeu uma Poção de Vida!")
        self.batalha = Batalha(self.jogador, self.inimigos[self.indice])
        self.vida_exibida_inimigo = self.batalha.inimigo.vida
        self.timer = 0
        self.estado = "espera"

    # --------------------------------------------------------
    # DESENHO
    # --------------------------------------------------------

    def desenhar(self):
        self.tela.fill(FUNDO)

        if self.tela_atual == "escolha_classe":
            self.desenhar_escolha_classe()
        elif self.tela_atual == "escolha_skin":
            self.desenhar_escolha_skin()
        else:
            self.desenhar_batalha()

        for texto in self.textos:
            texto.desenhar(self.tela, self.fonte_grande)

        pygame.display.flip()

    def escrever_centralizado(self, texto, fonte, x, y, cor=BRANCO):
        imagem = fonte.render(texto, True, cor)
        self.tela.blit(imagem, imagem.get_rect(center=(x, y)))

    def desenhar_escolha_classe(self):
        self.escrever_centralizado("JOGO DE BATALHA", self.fonte_grande, LARGURA // 2, 60)
        self.escrever_centralizado("Escolha sua classe", self.fonte, LARGURA // 2, 110)

        posicao = 0
        for nome, botao in self.botoes_classe:
            centro_x = 140 + posicao * 260
            self.tela.blit(self.previas[nome], (centro_x - 100, 150))
            self.escrever_centralizado(STATS_TEXTO[nome], self.fonte_pequena, centro_x, 420)
            botao.desenhar(self.tela, self.fonte)
            posicao += 1

    def desenhar_escolha_skin(self):
        self.escrever_centralizado("Escolha sua skin", self.fonte_grande, LARGURA // 2, 80)
        mouse = pygame.mouse.get_pos()
        for cor, sprite, retangulo in self.opcoes_skin:
            if retangulo.collidepoint(mouse):
                pygame.draw.rect(self.tela, (50, 50, 80), retangulo, border_radius=10)
                pygame.draw.rect(self.tela, BRANCO, retangulo, 3, border_radius=10)
            else:
                pygame.draw.rect(self.tela, (90, 90, 110), retangulo, 2, border_radius=10)
            self.tela.blit(sprite, (retangulo.x + 10, retangulo.y + 10))
        self.escrever_centralizado("Clique em uma skin para começar",
                                   self.fonte, LARGURA // 2, 470)

    def desenhar_personagem(self, sprite, x, deslocamento, tremor, alfa=255, queda=0):
        balanco = int(math.sin(self.tempo * 0.08) * 4)  # "respiração"
        sacudida = 0
        if tremor > 0:
            sacudida = random.randint(-5, 5)

        # Sombra
        pygame.draw.ellipse(self.tela, (15, 15, 25), (x - 50, CHAO_Y - 8, 100, 22))

        imagem = sprite
        if alfa < 255:
            imagem = sprite.copy()
            imagem.set_alpha(alfa)
        retangulo = imagem.get_rect(midbottom=(int(x + deslocamento + sacudida),
                                               CHAO_Y + 8 + balanco + queda))
        self.tela.blit(imagem, retangulo)

    def desenhar_batalha(self):
        inimigo = self.batalha.inimigo

        # Chão
        pygame.draw.rect(self.tela, (40, 40, 65), (0, CHAO_Y + 10, LARGURA, 30))

        self.escrever_centralizado(f"Batalha {self.indice + 1} de {len(self.inimigos)}",
                                   self.fonte, LARGURA // 2, 25)

        # HUD do jogador
        texto_vida = f"{self.jogador.nome}: {self.jogador.vida}/{self.jogador.vida_max}"
        self.tela.blit(self.fonte.render(texto_vida, True, BRANCO), (30, 45))
        desenhar_barra(self.tela, 30, 75, 260, self.vida_exibida_jogador,
                       self.jogador.vida_max, VERDE)
        if hasattr(self.jogador, "mana"):
            self.tela.blit(self.fonte_pequena.render(f"Mana: {self.jogador.mana}/100",
                                                     True, BRANCO), (30, 102))
            desenhar_barra(self.tela, 30, 125, 260, self.jogador.mana, 100, AZUL)

        # HUD do inimigo
        texto_inimigo = f"{inimigo.nome}: {inimigo.vida}/{inimigo.vida_max}"
        self.tela.blit(self.fonte.render(texto_inimigo, True, BRANCO), (510, 45))
        desenhar_barra(self.tela, 510, 75, 260, self.vida_exibida_inimigo,
                       inimigo.vida_max, VERMELHO)

        # Personagens
        self.desenhar_personagem(self.sprite_jogador, POS_JOGADOR_X,
                                 self.deslocamento_jogador, self.tremor_jogador)

        alfa = 255
        queda = 0
        if self.estado == "morte_inimigo":
            alfa = max(0, 255 - self.timer * 6)
            queda = self.timer
        self.desenhar_personagem(self.sprites_inimigos[inimigo.nome], POS_INIMIGO_X,
                                 self.deslocamento_inimigo, self.tremor_inimigo, alfa, queda)

        if self.tremor_jogador > 0:
            self.tremor_jogador -= 1
        if self.tremor_inimigo > 0:
            self.tremor_inimigo -= 1

        # Botões
        if self.estado == "fim":
            self.escrever_centralizado(self.mensagem_final, self.fonte_grande,
                                       LARGURA // 2, 300, (255, 220, 80))
            self.botao_reiniciar.desenhar(self.tela, self.fonte)
        else:
            for acao, botao in self.botoes_acao:
                botao.ativo = (self.estado == "espera")
                botao.desenhar(self.tela, self.fonte)

        # Log
        pygame.draw.rect(self.tela, (15, 15, 25), (30, 485, 740, 105), border_radius=6)
        pygame.draw.rect(self.tela, (90, 90, 110), (30, 485, 740, 105), 2, border_radius=6)
        ultimas = self.captura.linhas[-4:]
        linha_y = 495
        for linha in ultimas:
            self.tela.blit(self.fonte_pequena.render(linha, True, (210, 210, 220)),
                           (42, linha_y))
            linha_y += 24

    # --------------------------------------------------------
    # LOOP PRINCIPAL
    # --------------------------------------------------------

    def executar(self):
        while self.rodando:
            self.tratar_eventos()
            self.atualizar()
            self.desenhar()
            self.relogio.tick(FPS)

        sys.stdout = sys.__stdout__
        pygame.quit()


if __name__ == "__main__":
    jogo = Jogo()
    jogo.executar()