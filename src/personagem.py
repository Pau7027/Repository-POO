from abc import ABC, abstractmethod


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
