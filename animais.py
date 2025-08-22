from tamagoshi import Tamagoshi


# HAMSTER
class Hamster(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome) 
        self.bochecha = 0  # comida na bochecha

    def rodarNaRoda(self, tempo):
        if (tempo >= 0) and (tempo <= 100):
            self.tedio -= self.tedio * (tempo / 100)  # diminui tédio
            self.tedio = max(0, self.tedio)
            self.fome = min(100, self.fome + tempo * 0.5)  # aumenta fome
            print(f"\n{self.nome} está rodando na roda por {tempo} tempo 🐹🎡")

    def guardarComidaNaBochecha(self, quantidade):

        b = 20 - self.bochecha


        if b == 0 :
            print(f"\n Bochechas cheias.⚠🐹")

        elif  quantidade <= b :
            self.bochecha += quantidade
            print(f"\n{self.nome} guardou {quantidade} de comida na bochecha. 🐹🥦 Total: {self.bochecha}")

        else:
             print(f"\nDigite uma opção válida.")




        # if quantidade <= 20:
        #         if self.bochecha<=20:
        #             self.bochecha += quantidade
        #             print(f"\n{self.nome} guardou {quantidade} de comida na bochecha. 🐹🥦 Total: {self.bochecha}")

        # else: 
        #      print(f"\nDigite uma opção válida.")

    def usarComidaNaBochecha(self):
        if self.bochecha > 0:
            self.fome -= self.bochecha * 0.8  # usa a comida para diminuir a fome
            self.fome = max(0, self.fome)
            print(f"\n{self.nome} usou {self.bochecha} de comida da bochecha! 😋🍽")
            self.bochecha = 0
        else:
            print(f"\n{self.nome} não tem comida guardada na bochecha. ❌😕")

# ------------------------
# CACHORRO
class Cachorro(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome) 

    def abanarRabo(self, vezes):
        if (vezes >= 0) and (vezes <= 100):
            self.tedio -= self.tedio * (vezes / 200)  # melhora humor e reduz tédio
            self.tedio = max(0, self.tedio)
            self.fome = min(100, self.fome + vezes * 0.3)  # fica com um pouco mais de fome
            print(f"\n{self.nome} abanou o rabo {vezes} vezes! 🐕💕")

    def buscarBola(self, lancamentos):
        if (lancamentos >= 0) and (lancamentos <= 100):
            self.tedio -= self.tedio * (lancamentos / 100)  # diminui tédio 
            self.tedio = max(0, self.tedio)
            self.fome = min(100, self.fome + lancamentos * 0.5)  # aumenta fome
            print(f"\n{self.nome} buscou a bola {lancamentos} vezes! 🥎💦")

    def pedirCarinho(self):
        # Carinho melhora o humor, sem mexer em fome/tédio
        self.saude = min(100, self.saude + 5) 
        print(f"\n{self.nome} pediu carinho e ficou mais feliz! 🐶🥰")


# ------------------------
# PORCO
class Porco(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)  

    def rolarNaLama(self, tempo):
        if (tempo >= 0) and (tempo <= 100):
            self.tedio -= self.tedio * (tempo / 100)  
            self.tedio = max(0, self.tedio)
            self.saude = max(0, self.saude - tempo * 0.2)  # pode perder um pouco de saúde
            print(f"\n{self.nome} rolou na lama por {tempo} minutos! 🤎🐖")

    def fucarNoChao(self, tempo):
        if (tempo >= 0) and (tempo <= 100):
            self.tedio -= self.tedio * (tempo / 150)  # diminui um pouco o tédio
            self.tedio = max(0, self.tedio)
            print(f"\n{self.nome} ficou fuçando no chão! 🐽")

    def grunhir(self):
        self.tedio = max(0, self.tedio - 5)  # grunhir diverte o porco um pouco
        print(f"\n{self.nome} fez OINNC! 🐷🔊")
