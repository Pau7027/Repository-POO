from .personagem import Personagem


class Arqueiro(Personagem):

    def __init__(self, nome):
        super().__init__(
            nome=nome,
            vida=90,
            ataque=25,
            defesa=8
        )

    def atacar(self, alvo):
        print(f"{self.nome} está atacando {alvo.nome} com uma flecha!")
        alvo.receber_dano(self.ataque)