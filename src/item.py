from abc import ABC, abstractmethod
class Item(ABC):

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    @abstractmethod
    def usar(self, personagem):
        pass

class Pocao_de_vida(Item):
    def __init__(self, nome, valor, cura):
        super().__init__(nome, valor)
        self.cura = cura

    def usar(self, personagem):
        vida_recuperada = min(self.cura, personagem.vida_max - personagem.vida)
        personagem.vida += vida_recuperada
        print(f"{personagem.nome} usou {self.nome} e recuperou {vida_recuperada} de vida. Vida atual: {personagem.vida})")
