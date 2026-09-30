from src.guerreiro import Guerreiro
from src.mago import Mago
from src.inimigo import Inimigo

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
    # TODO
    pass

def test_inimigo_ataca():
    inimigo = Inimigo("Goblin", 30, 30, 2)
    guerreiro = Guerreiro("Arthur")
    inimigo.atacar(guerreiro)
    assert guerreiro.vida == 105 

def teste_receber_dano_com_limite_minimo():
    guerreiro = Guerreiro("Arthur")
    guerreiro.receber_dano(10)  # Dano menor que a defesa
    assert guerreiro.vida == 119  # Vida deve diminuir apenas em 1