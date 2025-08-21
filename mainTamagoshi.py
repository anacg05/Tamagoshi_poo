from tamagoshi import Hamster, Cachorro, Porco
import time

def escolher_animal():
    print("Escolha seu Tamagoshi:")
    print("1 - Hamster")
    print("2 - Cachorro")
    print("3 - Porco")
    opcao = input("Digite o número: ")

    nome = input("Dê um nome para seu Tamagoshi: ")

    if opcao == "1":
        return Hamster(nome)
    elif opcao == "2":
        return Cachorro(nome)
    elif opcao == "3":
        return Porco(nome)
    else:
        print("Opção inválida, criando Hamster por padrão.")
        return Hamster(nome)

def mostrar_status(animal):
    print("\n--- STATUS ---")
    print(f"Nome: {animal.nome}")
    print(f"Idade: {animal.idade:.1f}")
    print(f"Fome: {animal.fome:.1f}")
    print(f"Tédio: {animal.tedio:.1f}")
    print(f"Saúde: {animal.saude:.1f}")
    if isinstance(animal, Hamster):
        print(f"Bochechas: {animal.bochechas}")
    elif isinstance(animal, Cachorro):
        print(f"Energia: {animal.energia:.1f}")
    elif isinstance(animal, Porco):
        print(f"Limpeza: {animal.limpeza:.1f}")
    print(animal.getHumor())
    print("---------------\n")

def mostrar_menu(animal):
    print("--- MENU ---")
    print("1 - Alimentar")
    print("2 - Brincar")
    print("3 - Ação especial")
    print("0 - Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        qtd = int(input("Quanto quer alimentar (0-100)? "))
        animal.alimentar(qtd)
    elif escolha == "2":
        qtd = int(input("Quanto quer brincar (0-100)? "))
        animal.brincar(qtd)
    elif escolha == "3":
        if isinstance(animal, Hamster):
            print("a - Rodar na roda\nb - Guardar na bochecha\nc - Usar comida da bochecha")
            acao = input("Escolha a ação: ")
            if acao.lower() == "a":
                animal.rodar_na_roda()
            elif acao.lower() == "b":
                qtd = int(input("Quantidade de ração para guardar: "))
                animal.guardar_na_bochecha(qtd)
            elif acao.lower() == "c":
                animal.usar_comida_da_bochecha()
        elif isinstance(animal, Cachorro):
            print("a - Abanar rabo\nb - Pegar bolinha\nc - Latir")
            acao = input("Escolha a ação: ")
            if acao.lower() == "a":
                animal.abanar_rabo()
            elif acao.lower() == "b":
                animal.pegar_bolinha()
            elif acao.lower() == "c":
                animal.latir()
        elif isinstance(animal, Porco):
            print("a - Fuçar no chão\nb - Rolar na lama\nc - Comer tudo")
            acao = input("Escolha a ação: ")
            if acao.lower() == "a":
                animal.fuçar_no_chao()
            elif acao.lower() == "b":
                animal.rolar_na_lama()
            elif acao.lower() == "c":
                animal.comer_tudo()
    
    elif escolha == "0":
        return False
    else:
        print("Opção inválida!")

    return True

def main():
    meu_pet = escolher_animal()
    jogando = True

    while jogando and meu_pet.vivo:
        mostrar_status(meu_pet)
        jogando = mostrar_menu(meu_pet)

    print(f"Fim do jogo. {meu_pet.nome} não está mais entre nós 😢" if not meu_pet.vivo else "Você saiu do jogo.")

if __name__ == "__main__":
    main()
