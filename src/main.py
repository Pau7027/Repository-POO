from .guerreiro import Guerreiro
from .inimigo import Inimigo
from .batalha import Batalha
from .item import Pocao_de_vida


def main():

    jogador = Guerreiro("Arthur")

    inimigo = Inimigo(
        nome="Goblin",
        vida=100,
        ataque=15,
        defesa=5
    )

    # Adiciona um item ao inventário do jogador
    jogador.inventario.append(Pocao_de_vida("Poção de Vida", 20, 30))

    batalha = Batalha(jogador, inimigo)

    batalha.iniciar()


if __name__ == "__main__":
    main()
