from tamagoshi import Hamster, Cachorro, Porco
import time

from tamagoshi import Hamster, Cachorro, Porco
import time

def escolher_animal():
    print("🐾 Escolha um tipo de pet:")
    print("1 - Hamster 🐹")
    print("2 - Cachorro 🐶")
    print("3 - Porco 🐷")
    escolha = input("Digite o número correspondente: ")

    nome = input("Dê um nome ao seu pet: ")

    if escolha == "1":
        return Hamster(nome)
    elif escolha == "2":
        return Cachorro(nome)
    elif escolha == "3":
        return Porco(nome)
    else:
        print("Escolha inválida. Tente novamente.")
        return escolher_animal()

def exibir_status(pet):
    print("\n📊 STATUS ATUAL:")
    print(f"Nome: {pet.nome}")
    print(f"Idade: {round(pet.idade, 2)} anos")
    print(f"Fome: {pet.fome}")
    print(f"Tédio: {pet.tedio}")
    print(f"Saúde: {pet.saude}")
    if isinstance(pet, Hamster):
        print(f"🐹 Bochechas: {pet.bochechas}/20")
    elif isinstance(pet, Cachorro):
        print(f"⚡ Energia: {pet.energia}")
    elif isinstance(pet, Porco):
        print(f"🧼 Limpeza: {pet.limpeza}")
    print(pet.getHumor())

def menu_acao(pet):
    print("\n💡 Escolha uma ação:")
    print("1 - Alimentar")
    print("2 - Brincar")
    if isinstance(pet, Hamster):
        print("3 - Rodar na roda")
        print("4 - Guardar comida na bochecha")
        print("5 - Usar comida da bochecha")
    elif isinstance(pet, Cachorro):
        print("3 - Abanar o rabo")
        print("4 - Pegar bolinha")
        print("5 - Latir")
    elif isinstance(pet, Porco):
        print("3 - Fuçar no chão")
        print("4 - Rolar na lama")
        print("5 - Comer tudo")
    print("0 - Sair")

def executar_acao(pet, escolha):
    if escolha == "1":
        quantidade = int(input("Quanto quer alimentar? (0 a 100): "))
        pet.alimentar(quantidade)
    elif escolha == "2":
        quantidade = int(input("Quanto quer brincar? (0 a 100): "))
        pet.brincar(quantidade)
    elif escolha == "3":
        if isinstance(pet, Hamster):
            pet.rodar_na_roda()
        elif isinstance(pet, Cachorro):
            pet.abanar_rabo()
        elif isinstance(pet, Porco):
            pet.fuçar_no_chao()
    elif escolha == "4":
        if isinstance(pet, Hamster):
            quantidade = int(input("Quantas rações guardar? "))
            pet.guardar_na_bochecha(quantidade)
        elif isinstance(pet, Cachorro):
            pet.pegar_bolinha()
        elif isinstance(pet, Porco):
            pet.rolar_na_lama()
    elif escolha == "5":
        if isinstance(pet, Hamster):
            pet.usar_comida_da_bochecha()
        elif isinstance(pet, Cachorro):
            pet.latir()
        elif isinstance(pet, Porco):
            pet.comer_tudo()
    elif escolha == "0":
        print("Saindo do jogo... 💤")
        exit()
    else:
        print("Opção inválida!")

def main():
    print(" ✨Bem-vindo ao Tamagoshi Pet Simulator!✨ ")
    pet = escolher_animal()

    while pet.vivo:
        exibir_status(pet)
        menu_acao(pet)
        escolha = input("Digite o número da ação: ")
        executar_acao(pet, escolha)
        pet.tempoPassando()
        time.sleep(1)

    print("⚰️ Fim de jogo. Seu pet se foi.")

if __name__ == "__main__":
    main()
