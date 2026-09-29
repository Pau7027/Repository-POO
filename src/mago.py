from personagem import Personagem

class Mago(Personagem):

    def __init__(self, nome):
        super().__init__(
            nome=nome,
            vida=80,
            ataque=30,
            defesa=5
        )

        self.mana = 100

    def atacar(self, alvo):
        print(f"{self.nome} está atacando {alvo.nome} com um golpe normal!")
        alvo.receber_dano(self.ataque)
        

    def usar_magia(self, alvo):
        if self.mana >= 20:
            print(f"{self.nome} está atacando {alvo.nome} com magia!")
            alvo.receber_dano(self.ataque * 1.5)   #Magia causa 1.5 do ataque normal
            self.mana -= 20
        else:
            print(f"{self.nome} não possui mana suficiente para usar magia.")
    

        

       
