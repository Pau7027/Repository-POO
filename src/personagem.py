from abc import ABC, abstractmethod
from .guerreiro import Guerreiro
from .mago import Mago
from .arqueiro import Arqueiro

class Personagem(ABC):

    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.vida_max = vida
        self.inventario = []
        
    def adicionar_item(self, item):
        self.inventario.append(item)
        print(f"{item} adicionado ao inventário de {self.nome}.")

    def esta_vivo(self):
        return self.vida > 0

    def receber_dano(self, dano):
        dano_real = max(1, int(dano - self.defesa))  # Evita dano nulo ou negativo
        self.vida = max(0, self.vida - dano_real)    # Vida nunca fica negativa
        print(f"{self.nome} recebeu {dano_real} de dano. Vida atual: {self.vida}")
    @abstractmethod
    def atacar(self, alvo):
        pass

    def mostrar_status(self):
        print(
            f"{self.nome} | "
            f"Vida: {self.vida} | "
            f"Ataque: {self.ataque} | "
            f"Defesa: {self.defesa}"
        )



#Função para escolha do personagem
def escolher_personagem():
    print("="*40)
    print("    ESCOLHA SEU PERSONAGEM:")
    print("1 - Guerreiro (VIDA: 100|ATAQUE: 20|DEFESA: 15)")
    print("2 - Mago  (VIDA: 80|ATAQUE: 30|DEFESA: 5)")
    print("3 - Arqueiro(VIDA: 90|ATAQUE: 25|DEFESA: 8)")
    
    nome = input("\nDigite o nome do seu personagem: ")
    if nome.strip()=="":
        nome = "Herói"
    while True:
        opcao = input("Escolha uma opção (1, 2 ou 3): ")
        if opcao == "1":
            return Guerreiro(nome)
        elif opcao == "2":
            return Mago(nome)
        elif opcao == "3":
            return Arqueiro(nome)
        else:
            print("Opção inválida. Tente novamente.")