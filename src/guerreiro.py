from .personagem import Personagem


class Guerreiro(Personagem):

    def __init__(self, nome):
        super().__init__(
            nome=nome,
            vida=120,
            ataque=20,
            defesa=15
        )

    def atacar(self, alvo):
        print(f"{self.nome} está atacando {alvo.nome}!")
        alvo.receber_dano(self.ataque)

