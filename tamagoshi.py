class Tamagoshi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0
        self.tedio = 0
        self.vivo = True  # Novo atributo

    # ------------------------
    # Método auxiliar
    def limitar(self, valor, minimo=0, maximo=100):
        return max(minimo, min(valor, maximo))

    # ------------------------
    def alimentar(self, quantidade):
        if not self.vivo:
            print(f"{self.nome} morreu.")
            return
        if 0 <= quantidade <= 100:
            self.fome = self.limitar(self.fome - self.fome * (quantidade / 100))

    def brincar(self, quantidade):
        if not self.vivo:
            print(f"{self.nome} morreu.")
            return
        if 0 <= quantidade <= 100:
            self.tedio = self.limitar(self.tedio - self.tedio * (quantidade / 100))

    def getHumor(self):
        if not self.vivo:
            return f"{self.nome} morreu X_X"
        humor = 100 - ((self.fome + self.tedio) / 2)
        if humor > 70:
            return f"{self.nome}: Estou muito feliz 😄"
        elif humor > 40:
            return f"{self.nome}: Estou meio entediado 😐"
        else:
            return f"{self.nome}: Estou triste 😢"

    # ------------------------
    def vida(self):
        if not self.vivo:
            return

        if (50 < self.fome <= 60) or (50 < self.tedio <= 60):
            self.saude -= 10
        elif (60 < self.fome <= 80) or (60 < self.tedio <= 80):
            self.saude -= 30
        elif (80 < self.fome <= 90) or (80 < self.tedio <= 90):
            self.saude -= 50
        elif self.fome > 90 or self.tedio > 90:
            print(f"{self.nome}: Estou morrendo...😭 ")

        if self.fome > 99 or self.tedio > 99 or self.saude <= 0:
            self.vivo = False
            print(f"{self.nome} morreu 😨💀")

    def tempoPassando(self):
        if not self.vivo:
            return
        self.vida()
        self.idade += 0.2
        self.tedio = self.limitar(self.tedio + 2.5)
        self.fome = self.limitar(self.fome + 5)


# ------------------------
# HAMSTER
class Hamster(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.bochechas = 0  # Quantidade de comida guardada
        self.tempo_de_vida = 5  # Limite de idade em anos

    def tempoPassando(self):
        if not self.vivo:
            return
        self.vida()
        self.idade += 0.1  # Hamsters vivem menos
        self.tedio = self.limitar(self.tedio + 4)    # Entediado mais rápido
        self.fome = self.limitar(self.fome + 6)      # Fome aumenta mais rápido
        if self.idade >= self.tempo_de_vida:
            self.vivo = False
            print(f"{self.nome} morreu de velhice 😔")

    def rodar_na_roda(self):
        if not self.vivo:
            print(f"{self.nome} morreu 😰")
            return
        self.tedio = self.limitar(self.tedio - 15)
        self.fome = self.limitar(self.fome + 5)  # rodar dá fome
        print(f"{self.nome} está se exercitando na roda 🎡🐹")

    def guardar_na_bochecha(self, quantidade):
        if not self.vivo:
            print(f"{self.nome} morreu 😰")
            return
        # Cada ração ocupa 2 espaços
        espaco_ocupado = quantidade * 2
        if espaco_ocupado < 0:
            print("Quantidade inválida.")
            return

        if self.bochechas + espaco_ocupado > 20:
            print(f"{self.nome} está com as bochechas cheias ⚠🐹 ")
            return

        self.bochechas += espaco_ocupado
        print(f"{self.nome} guardou {quantidade} rações nas bochechas ✅ ")

    def usar_comida_da_bochecha(self):
        if not self.vivo:
            print(f"{self.nome} morreu 😰")
            return
        if self.bochechas <= 0:
            print(f"{self.nome} não tem mais ração nas bochechas ❌")
            return

        self.fome = self.limitar(self.fome - self.bochechas)  # 1 espaço = 1 de fome
        print(f"{self.nome} comeu a comida das bochechas 😋🐹 ")
        self.bochechas = 0

# ------------------------
# CACHORRO
class Cachorro(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.energia = 100  # atributo exclusivo do cachorro

    def tempoPassando(self):
        if not self.vivo:
            return
        self.vida()  
        self.idade += 0.3   # cachorros envelhecem mais devagar que hamsters
        self.tedio = self.limitar(self.tedio + 3)   
        self.fome = self.limitar(self.fome + 4)    
        self.energia = self.limitar(self.energia - 2)  

    def abanar_rabo(self):
        # O cachorro abana o rabo quando está feliz e reduz o tédio
        if not self.vivo:
            print(f"{self.nome} morreu 😰")
            return
        self.tedio = self.limitar(self.tedio - 10)  # diminui o tédio
        print(f"{self.nome} está abanando o rabo felizmente 🐶❤️")

    def pegar_bolinha(self):
        # Brincar de pegar bolinha aumenta a fome e diminui a energia
        if not self.vivo:
            print(f"{self.nome} morreu 😰")
            return
        self.tedio = self.limitar(self.tedio - 20)  
        self.fome = self.limitar(self.fome + 8)     # correr aumenta a fome
        self.energia = self.limitar(self.energia - 15)  
        print(f"{self.nome} correu e pegou a bolinha 🥎🐾")

    def latir(self):
        # Latir deixa o cachorro cansado e um pouco entediado
        if not self.vivo:
            print(f"{self.nome} morreu 😰")
            return
        self.tedio = self.limitar(self.tedio + 3)   # latir sozinho pode aumentar o tédio
        self.energia = self.limitar(self.energia - 5)  # gasta energia
        print(f"{self.nome} latiu bem alto! 🐕")

# ------------------------
# PORCO
class Porco(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.limpeza = 100  # atributo exclusivo do porco, quanto mais alto, mais limpo

    def tempoPassando(self):
        if not self.vivo:
            return
        self.vida()
        self.idade += 0.25   # envelhece normal
        self.tedio = self.limitar(self.tedio + 3.5)  # entediado moderadamente
        self.fome = self.limitar(self.fome + 5)      # sente fome rápido
        self.limpeza = self.limitar(self.limpeza - 1)  # vai ficando mais sujo

    def fuçar_no_chao(self):
        # O porco fuça no chão para se divertir
        if not self.vivo:
            print(f"{self.nome} morreu 😰")
            return
        self.tedio = self.limitar(self.tedio - 15)   
        self.fome = self.limitar(self.fome + 5)      # gasta energia, dá fome
        print(f"{self.nome} está fuçando no chão em busca de algo 🐷")

    def rolar_na_lama(self):
        # O porco rola na lama para se refrescar
        if not self.vivo:
            print(f"{self.nome} morreu 😰")
            return
        self.tedio = self.limitar(self.tedio - 20)   
        self.saude = self.limitar(self.saude + 10)   # refrescou, saúde melhora
        self.limpeza = self.limitar(self.limpeza - 30)  # mas fica sujo
        print(f"{self.nome} rolou feliz na lama 🐽🥰")

    def comer_tudo(self):
        # porcos comem bastante de uma vez só
        if not self.vivo:
            print(f"{self.nome} morreu 😰")
            return
        self.fome = self.limitar(self.fome - 40)     # fome quase zera
        if self.fome < 0:
            self.fome = 0
        self.saude = self.limitar(self.saude - 5)    # comer demais pode prejudicar saúde
        print(f"{self.nome} comeu tudo o que encontrou no cocho 🍽️🐖")
