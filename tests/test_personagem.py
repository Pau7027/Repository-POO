import pytest
from src.guerreiro import Guerreiro
from src.mago import Mago
from src.inimigo import Inimigo
from src.item import Pocao_de_vida
from src.orc import Orc
from src.chefe_final import ChefeFinal
from src.arqueiro import Arqueiro
from src.batalha import Batalha

def test_guerreiro_esta_vivo():

    guerreiro = Guerreiro("Arthur")

    assert guerreiro.esta_vivo() is True


def test_personagem_recebe_dano():
    mago = Mago("Merlin")
    mago.receber_dano(10)
    assert mago.vida == 75  


def test_personagem_morre():
    mago = Mago("Merlin")
    mago.receber_dano(100)
    assert mago.esta_vivo() is False


def test_guerreiro_ataca():
    guerreiro = Guerreiro("Arthur")
    inimigo = Inimigo("Goblin", 100, 15, 5)

    guerreiro.atacar(inimigo)

    assert inimigo.vida == 85

def test_inimigo_ataca():
    inimigo = Inimigo("Goblin", 30, 30, 2)
    guerreiro = Guerreiro("Arthur")
    inimigo.atacar(guerreiro)
    assert guerreiro.vida == 105 

def teste_receber_dano_com_limite_minimo():
    guerreiro = Guerreiro("Arthur")
    guerreiro.receber_dano(10)  # Dano menor que a defesa
    assert guerreiro.vida == 119  # Vida deve diminuir apenas em 1


def test_pocao_de_vida():
    guerreiro = Guerreiro("Arthur")
    pocao = Pocao_de_vida("Poção de Vida", 20,30)
    guerreiro.vida = 50
    guerreiro.adicionar_item(pocao)
    
    pocao.usar(guerreiro)
    assert guerreiro.vida == 80  

def test_pocao_nao_passa_da_vida_maxima():
    guerreiro = Guerreiro("Arthur")
    guerreiro.vida = 110
    pocao = Pocao_de_vida("Poção de Vida", 20,30)
    pocao.usar(guerreiro)
    assert guerreiro.vida == 120  # Vida não deve passar de 120

def test_orc():
    orc = Orc("Grom")
    guerreiro = Guerreiro("Arthur")

    assert orc.vida == 150
    assert orc.ataque == 25
    assert orc.defesa == 10

    orc.atacar(guerreiro)

    assert guerreiro.vida == 110

def test_arqueiro():
    arqueiro = Arqueiro("Legolas")
    inimigo = Inimigo("Goblin", 100, 15, 5)

    assert arqueiro.vida == 90
    assert arqueiro.ataque == 25
    assert arqueiro.defesa == 8

    arqueiro.atacar(inimigo)

    assert inimigo.vida == 80

def test_chefe_final():
    chefe = ChefeFinal("Dragão Ancião")
    guerreiro = Guerreiro("Arthur")

    assert chefe.vida == 250
    assert chefe.ataque == 35
    assert chefe.defesa == 15

    chefe.atacar(guerreiro)

    assert guerreiro.vida == 100

#-----------------Funções auxiliares-------------------------------
def simular_entradas(monkeypatch,entradas):
    "Faz o input() retornar os valores da lista de entradas, um por vez."
    iterador = iter(entradas)
    monkeypatch.setattr('builtins.input', lambda _: next(iterador))

def criar_batalha():
    jogador = Guerreiro("Arthur")
    inimigo = Inimigo("Goblin", 100, 15, 5)
    return Batalha(jogador,inimigo)

#----------- turno_do_jogador() ----------------
def test_turno_inimigo_ataca():
    batalha = criar_batalha()
    batalha.turno_do_inimigo()
    #ataque 15 - defesa 15 =0, mas o dano mínimo é 1
    assert batalha.jogador.vida == 119

def test_turno_inimigo_nao_ataca_se_estiver_morto():
    batalha = criar_batalha()
    batalha.inimigo.vida = 0
    batalha.turno_do_inimigo()
    

