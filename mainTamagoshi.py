from tamagoshi import Tamagoshi
from animais import Hamster, Cachorro, Porco


def mostrarStatus(bicho):
    print("\n===== 📊 STATUS =====")
    print(f"Nome: {bicho.nome}")
    print(f"Idade: {round(bicho.idade, 1)}")
    print(f"Fome: {round(bicho.fome, 1)} / 100")
    print(f"Tédio: {round(bicho.tedio, 1)} / 100")
    print(f"Saúde: {round(bicho.saude, 1)} / 100")
    if isinstance(bicho, Hamster):
        print(f"Bochecha: {bicho.bochecha} / 20")
    print("==================\n")


def menuHamster(bicho):
    while True:
        mostrarStatus(bicho)
        print("Escolha uma ação para o Hamster:")
        print("1 - Alimentar")
        print("2 - Brincar")
        print("3 - Rodar na roda")
        print("4 - Guardar comida na bochecha")
        print("5 - Usar comida da bochecha")
        print("0 - Sair do jogo")
        
        op = input("Digite a opção: ")
        

        if op == "1":
            qtd = int(input("Quanto deseja alimentar? (0 a 100):"))
            bicho.alimentar(30)
        elif op == "2":
            qtd = int(input("Quanto deseja brincar? (0 a 100):"))
            bicho.brincar(qtd)
        elif op == "3":
            qtd = int(input("Quanto tempo deseja rodar na roda? (0 a 100):"))
            bicho.rodarNaRoda(qtd)
        elif op == "4":
            qtd = int(input("Quanto deseja guardar na bochecha? (0 a 20):"))
            bicho.guardarComidaNaBochecha(qtd)
        elif op == "5":
            qtd = int(input("Quanto deseja usar da bochecha? (0 a 20):"))
            bicho.usarComidaNaBochecha(qtd)
        elif op == "0":
            break
        else:
            print("Opção inválida!")

        bicho.tempoPassando()


def menuCachorro(bicho):
    while True:
        mostrarStatus(bicho)
        print("Escolha uma ação para o Cachorro:")
        print("1 - Alimentar")
        print("2 - Brincar")
        print("3 - Abanar o rabo")
        print("4 - Buscar a bola")
        print("5 - Pedir carinho")
        print("0 - Sair do jogo")
        
        op = input("Digite a opção: ")

        if op == "1":
            qtd = int(input("Quanto deseja alimentar? (0 a 100):"))
            bicho.alimentar(qtd)
        elif op == "2":
            qtd = int(input("Quanto deseja brincar? (0 a 100):"))
            bicho.brincar(qtd)
        elif op == "3":
            qtd = int(input("Quantas vezes deseja abanar o rabo? (0 a 100):"))
            bicho.abanarRabo(qtd)
        elif op == "4":
            qtd = int(input("Quantas vezes deseja jogar a bola? (0 a 100):"))
            bicho.buscarBola(qtd)
        elif op == "5":
            bicho.pedirCarinho()
        elif op == "0":
            break
        else:
            print("Opção inválida!")

        bicho.tempoPassando()


def menuPorco(bicho):
    while True:
        mostrarStatus(bicho)
        print("Escolha uma ação para o Porco:")
        print("1 - Alimentar")
        print("2 - Brincar")
        print("3 - Rolar na lama")
        print("4 - Fuçar no chão")
        print("5 - Grunhir")
        print("0 - Sair do jogo")
        
        op = input("Digite a opção: ")

        if op == "1":
            qtd = int(input("Quanto deseja alimentar? (0 a 100):"))
            bicho.alimentar(qtd)
        elif op == "2":
            qtd = int(input("Quanto deseja brincar? (0 a 100):"))
            bicho.brincar(qtd)
        elif op == "3":
            qtd = int(input("Quanto tempo deseja rolar na lama? (0 a 100):"))
            bicho.rolarNaLama(qtd)
        elif op == "4":
            qtd = int(input("Quanto tempo deseja fuçar no chão? (0 a 100):"))
            bicho.fucarNoChao(qtd)
        elif op == "5":
            bicho.grunhir()
        elif op == "0":
            break
        else:
            print("Opção inválida!")

        bicho.tempoPassando()


# ==================== MAIN ====================
print(" ✨ Bem-vindo ao Tamagoshi! ✨ ")
print("Escolha seu animal:")
print("1 - Hamster 🐹")
print("2 - Cachorro 🐶")
print("3 - Porco 🐷")

escolha = input("Digite a opção: ")
nome = input("Dê um nome para o seu bichinho: ")

if escolha == "1":
    pet = Hamster(nome)
    menuHamster(pet)
elif escolha == "2":
    pet = Cachorro(nome)
    menuCachorro(pet)
elif escolha == "3":
    pet = Porco(nome)
    menuPorco(pet)
else:
    print("Opção inválida! Saindo do jogo... 💤")
