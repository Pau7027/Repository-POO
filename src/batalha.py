


class Batalha:

    def __init__(self, jogador, inimigo):
        self.jogador = jogador
        self.inimigo = inimigo

    def iniciar(self):

        print("=" * 40)
        print("        INÍCIO DA BATALHA")
        print("=" * 40)

        while self.jogador.esta_vivo() and self.inimigo.esta_vivo():

            print("\n--- STATUS ---")
            self.jogador.mostrar_status()
            self.inimigo.mostrar_status()

            print("\n--- AÇÕES ---")
            print("1 - Atacar")
            print("2 - Usar item")
            print("3 - Fugir")
            if hasattr(self.jogador,"usar_magia"):
                print("4 - Usar magia")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.jogador.atacar(self.inimigo)

            elif opcao == "2":
                usou_item = self.usar_item()
                if usou_item == False: 
                    continue
                

            elif opcao == "3":
                print("Você fugiu da batalha!")
                return
            
            elif opcao == "4" and hasattr(self.jogador,"usar_magia"):
                usou_magia = self.jogador.usar_magia(self.inimigo)
                if usou_magia == False:
                    continue

            else:
                print("Opção inválida.")
                continue

            self.turno_inimigo() #Inimigo ataca jogador

        self.verificar_vencedor() #Verifica quem venceu a batalha


    def usar_item(self):
    ##"""Retorna True se o item foi usado, False se o jogador desistiu."""

        if len(self.jogador.inventario) == 0:
            print("Você não possui itens.")
            return False

        print("\n--- INVENTÁRIO ---")
        for i in range(len(self.jogador.inventario)):
            item = self.jogador.inventario[i]
            print(f"{i + 1} - {item.nome}")
        print("0 - Voltar")

        escolha = input("Escolha um item: ")

        if not escolha.isdigit():
            print("Opção inválida.")
            return False

        numero = int(escolha)

        if numero == 0:
            return False

        if numero < 1 or numero > len(self.jogador.inventario):
            print("Item inexistente.")
            return False

        item = self.jogador.inventario.pop(numero - 1)  # Remove o item (consumível)
        item.usar(self.jogador)
        return True
    
    def turno_inimigo(self):
        if self.inimigo.esta_vivo():
            print("\n--- TURNO DO INIMIGO ---")
            self.inimigo.atacar(self.jogador)
            
    def verificar_vencedor(self):
        print("\n" + "=" * 40)
        if self.jogador.esta_vivo():
            print(f"VITÓRIA! {self.jogador.nome} derrotou {self.inimigo.nome}!")
        else:
            print(f"DERROTA... {self.inimigo.nome} venceu {self.jogador.nome}.")
        print("=" * 40)