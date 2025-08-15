class Veiculo:
    def __init__(self, marca, ano_fab, cor, qtd_portas, modelo):
        self.marca = marca
        self.ano_fab = ano_fab
        self.cor = cor
        self.qtd_prtas = qtd_portas
        self.modelo = modelo


    def andar(self):
        print(f"{self.modelo} andando")

    def parar(self):
        print(f"{self.modelo} parado")

    def imprimir(self):
        print("O veículo tem caracteristicas:\n"
              f"Modelo: {self.modelo}\n"
              f"Marca: {self.marca}\n"
              f"Ano de Fabricação: {self.ano_fab}\n"
              f"Cor: {self.cor}\n"
              f"Quantidade de Portas: {self.qtd_prtas}"
              )


class Moto(Veiculo):
    def __init__(self, marca, ano_fab, cor, qtd_portas, modelo, cilindradas):
        super().__init__(marca, ano_fab, cor, qtd_portas, modelo)
        self.cilindradas = cilindradas

    def cortar_giro(self):
        print(f"{self.modelo} cortando giro")

    def imprimir(self):
        super().imprimir()
        print(f"Cilindradas: {self.cilindradas}")

    
class Caminhao(Veiculo):
    def __init__(self, marca, ano_fab, cor, qtd_portas, modelo, carga):
        super().__init__(marca, ano_fab, cor, qtd_portas, modelo)
        self.carga = carga

    def quebrar_asa(self):
        print(f"{self.modelo} quebrando asa")

    def imprimir(self):
        super().imprimir()
        print(f"Carga: {self.carga}")

def main():
    # carro1 = Veiculo("Toyota", 2008, "Cinza", 4, "Corolla")
    # carro1.imprimir()
    # carro1.andar()

    moto1 = Moto("Yamaha", 2024, "Azul", 0, "Fazer", 250)
    moto1.imprimir()
    moto1.cortar_giro()

    # caminhao1 = Caminhao("Scania", 2000, "Branco", 2, "P310", "500kg")
    # caminhao1.imprimir()
    # caminhao1.quebrar_asa()

    
main()