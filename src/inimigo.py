from personagem import Personagem


class Inimigo(Personagem):

    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(
            nome=nome,
            vida=vida,
            ataque=ataque,
            defesa=defesa
        )

    def atacar(self, alvo):
       print(f"{self.nome} está atacando {alvo.nome}!")
       alvo.receber_dano(self.ataque)
    