from .inimigo import Inimigo


class Orc(Inimigo):

    def __init__(self, nome):
        super().__init__(
            nome=nome,
            vida=150,
            ataque=25,
            defesa=10
        )