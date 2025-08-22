class Tamagoshi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0
        self.tedio = 0

    def alimentar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.fome -= self.fome * (quantidade / 100)
            self.fome = max(0, self.fome) 

    def brincar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.tedio -= self.tedio * (quantidade / 100)
            self.tedio = max(0, self.tedio) 

    def getHumor(self):
        return 100 - ((self.fome + self.tedio) / 2 )
    
    def vida(self):
        if ((self.fome > 50 and self.fome <= 60)) or ((self.tedio > 50 and self.tedio <= 60)):
            self.saude -= 10

        elif ((self.fome > 60 and self.fome <= 80)) or ((self.tedio > 60 and self.tedio <= 80)):
            self.saude -= 30

        elif ((self.fome > 80 and self.fome <= 90)) or ((self.tedio > 80 and self.tedio <= 90)):
            self.saude -= 50

        elif (self.fome > 90 ) or (self.tedio > 90 ):
            print("Estou morrendo...")

        elif (self.fome > 99 ) or (self.tedio > 99 ):
            print("Seu bichinho morreu X_X")

    def tempoPassando(self):
        self.vida()
        self.idade += 0.2
        self.tedio = min(100, self.tedio + 2.5) 
        self.fome = min(100, self.fome + 5) 

# ------------------------

