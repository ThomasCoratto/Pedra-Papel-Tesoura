import random

user_ganha = 0
pc_ganha = 0

options = ["Pedra", "Papel", "Tesoura"]

while True:
    user_input = input("Digite Pedra/Papel/Tesoura ou Q para Sair: ").capitalize()
    if user_input == "Q":
        break

    if user_input not in options:
        print("Opção inválida. Tente novamente.")
        continue

    pc_escolheu = random.choice(options)
    print("PC escolheu", pc_escolheu + ".")

    if (user_input == "Pedra" and pc_escolheu == "Tesoura") or \
       (user_input == "Tesoura" and pc_escolheu == "Papel") or \
       (user_input == "Papel" and pc_escolheu == "Pedra"):
        print("Você Ganhou")
        user_ganha += 1

    elif (user_input == "Pedra" and pc_escolheu == "Papel") or \
         (user_input == "Tesoura" and pc_escolheu == "Pedra") or \
         (user_input == "Papel" and pc_escolheu == "Tesoura"):
        print("Você Perdeu... KEK")
        pc_ganha += 1

    else:
        print("Empate!")

print("Você Ganhou", user_ganha, "vezes.")
print("O PC Ganhou", pc_ganha, "vezes.")
print("Obrigado por Jogar!")

