class Tamagoshi():
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0
        self.tedio = 0

    def alimentar(self, quantidade):
        if 0 <= quantidade <= 100:
            self.fome -= self.fome * (quantidade / 100)
            if self.fome < 0:
                self.fome = 0

    def brincar(self, quantidade):
        if 0 <= quantidade <= 100:
            self.tedio -= self.tedio * (quantidade / 100)
            if self.tedio < 0:
                self.tedio = 0

    def getHumor(self):
        return 100 - ((self.fome + self.tedio) / 2)

    def vida(self):
        if (50 < self.fome <= 60) or (50 < self.tedio <= 60):
            self.saude -= 10
        elif (60 < self.fome <= 80) or (60 < self.tedio <= 80):
            self.saude -= 30
        elif (80 < self.fome <= 90) or (80 < self.tedio <= 90):
            self.saude -= 50
        elif self.fome > 90 or self.tedio > 90:
            print("Estou morrendo... ")
        if self.fome > 99 or self.tedio > 99:
            print("Seu bichinho morreu X_X")

    def tempoPassando(self):
        self.vida()
        self.idade += 0.2
        self.tedio += 2.5
        self.fome += 5

# vou deixar com comentarios pra eu entender
# HAMSTER
class Hamster(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.bochechas = 0  # Quantidade de comida guardada

    def tempoPassando(self):
        self.vida()
        self.idade += 0.1  # Hamsters vivem menos
        self.tedio += 4    # Fica entediado mais rápido
        self.fome += 6     # Fome aumenta um pouco mais rápido

    def rodar_na_roda(self):
        # Diminui o tédio com o exercicio
        self.tedio -= 15
        if self.tedio < 0:
            self.tedio = 0
        print(f"{self.nome} está se exercitando.")

    def guardar_na_bochecha(self, quantidade):
        # Guarda comida na bochecha e só cabe até 20 unidades
        if quantidade < 0:
            print("Quantidade inválida.")
            return

        if self.bochechas + quantidade > 20:
            print(f"{self.nome} está com as bochechas cheias. ")
            return

        self.bochechas += quantidade
        print(f"{self.nome} guardou {quantidade} rações nas bochechas. ")

    def usar_comida_da_bochecha(self):
        # Come a comida guardada
        if self.bochechas <= 0:
            print(f"{self.nome} não tem mais ração nas bochechas.")
            return

        self.fome -= self.bochechas * 2  # cada ração diminui 2 de fome
        if self.fome < 0:
            self.fome = 0
        print(f"{self.nome} comeu toda a ração. ")
        self.bochechas = 0



