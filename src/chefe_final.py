from .inimigo import Inimigo


class ChefeFinal(Inimigo):

    def __init__(self, nome):
        super().__init__(
            nome=nome,
            vida=250,
            ataque=35,
            defesa=15
        )