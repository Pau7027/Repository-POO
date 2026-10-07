from .inimigo import Inimigo
from .batalha import Batalha
from .item import Pocao_de_vida
from .orc import Orc
from .chefe_final import ChefeFinal
from .personagem import escolher_personagem




def main():
    jogador = escolher_personagem()

    
    inimigos = [
    Inimigo("Goblin", 100, 15, 5),
    Orc("Orc"),
    ChefeFinal("Dragão Ancião")
]
    
    # Itens Iniciais
    jogador.inventario.append(Pocao_de_vida("Poção de Vida", 20, 30))
    
    # Loop de Batalhas
    for numero in range(len(inimigos)):
        inimigo = inimigos[numero]
        print(f"\n====BATALHA {numero +1} DE {len(inimigos)}====")
        
        batalha = Batalha(jogador, inimigo)
        batalha.iniciar()
        # O Jogador morreu ou fugiu da batalha(Fim)
        if not jogador.esta_vivo() or inimigo.esta_vivo():
            return
        # Recompensa por vencer as batalhas( não depois da ultima)
        if numero < len(inimigos) - 1:
            jogador.inventario.append(Pocao_de_vida("Poção de Vida", 20, 30))
            print(f"\n{jogador.nome} recebeu uma Poção de Vida como recompensa!")

        
    
    
        

    print("\nPARABÉNS! Você venceu todos os inimigos!")


if __name__ == "__main__":
    main()
