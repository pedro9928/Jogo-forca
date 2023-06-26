import random
import os


def play():
    ppt = ["pedra" ,"papel" ,"tesoura"]
    user = input("escolha(Pedra,papel e tesoura): ")
    maquina = random.choice(ppt)

    pm = 0
    pu = 0
    empates = 0

    #caso a maquina escolha pedra 
    if maquina == "pedra" and user == "pedra":
        print(f"Você jogou {user} e eu joguei {maquina} \nempatamos.")
        empates += 1
    elif maquina == "pedra" and user == "papel":
        print(f"Você jogou {user} e eu joguei {maquina} \nEu perdi. Parabéns")
        pu += 1
    elif maquina == "pedra" and user == "tesoura":
        print(f"Você jogou {user} e eu joguei {maquina} \nEu ganhei. kkkkk muito ruim." )
        pm += 1 
    
    #caso a maquina escolha papel
    elif maquina == "papel" and user == "papel":
        print(f"Você jogou {user} e eu joguei {maquina} \nEmpatamos.")
        empates += 1
    elif maquina == "papel" and user == "pedra":
        print(f"Você jogou {user} e eu joguei {maquina} \nEu ganhei. kkkkk muito ruim.")
        pm += 1
    elif maquina == "papel" and user == "tesoura":
        print(f"Você jogou {user} e eu joguei {maquina} \nVocê ganhou. Parabéns.")
        pu += 1

    #caso a maquina escolha tesoura
    elif maquina == "tesoura" and user == "tesoura":
        print(f"Você jogou {user} e eu joguei {maquina} \nEmpatamos.")
        empates += 1
    elif maquina == "tesoura" and user == "papel":
        print(f"Você jogou {user} e eu joguei {maquina} \neu ganhei. kkkkkk muito ruim")
        pm += 1
    elif maquina == "tesoura" and user == "pedra":
        print(f"Você jogou {user} e eu joguei {maquina} \nVocê ganhou. Parabéns")
        pu += 1


    return(pm , pu, empates)


total_pm = 0
total_pu = 0
total_empates = 0

for _ in range(3):
    pm, pu, empates = play()
    total_pm += pm
    total_pu += pu
    total_empates += empates

os.system('cls' if os.name == 'nt' else 'clear')
print("Placar final:")
print(f"Você ganhou {total_pu} vezes.")
print(f"Eu ganhei {total_pm} vezes.")
print(f"Tivemos {total_empates} empates.")

