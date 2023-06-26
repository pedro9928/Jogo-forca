import random
import os

print(20*"-")
print(7*" " + "jogos")
print(20*"-")
print("Temos dois temas para forca: \npaises; \nnomes.")
t_forca = str(input("Digite qual tema você quer: "))

def pais():
    print(20*"=-=")
    print(25*" "+"Paises")
    print(20*"=-=")
    pais_secreto = ['brasil', 'australia', 'japao', 'grecia', 'china', 'belgica', 'jamaica', 'alemanha','madagascar', 'eslovaquia', 'montenegro']
    print("Eu escolhi um país entre os seguintes:")
    for pais in pais_secreto:
        print(pais)
    print(20*"=-=")
    random.shuffle(pais_secreto)
    pais_secreto = pais_secreto[0]

    tentativas = 5
    enforcou = False

    while tentativas > 0 and not enforcou:
        guess = str(input("Digite seu chute: "))
        if guess != pais_secreto:
            print("Errou. Tente novamente.")
            tentativas -= 1
            print(f"Você possui {tentativas} tentativas.")
        else:
            enforcou = True

    if enforcou:
        print(f"Parabéns! Você acertou o país: {pais_secreto}")
    else:
        print(f"Suas tentativas acabaram. O país secreto era: {pais_secreto}")

def nome():
    print(20*"=-=")
    print(25*" "+"Nome")
    print(20*"=-=")
    nomes = ['Alice', 'Bob', 'Carol', 'David', 'Eve', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack']
    print("Eu escolhi um país entre os seguintes:")
    for n in nomes:
        print(n)
    print(20*"=-=")
    random.shuffle(nomes)
    nomes_secreto = nomes[0]

    tentativas = 5
    enforcou = False

    while tentativas > 0 and not enforcou:
        guess = str(input("Digite seu chute: "))
        if guess != nomes_secreto:
            print("erroouuu. Tente novamente.")
            tentativas -= 1
            print(f"Você ainda possui {tentativas} tentativas.")
        else:
            enforcou = True
    
    if enforcou:
        print(f"Parabéns! Você acertou o nome: {nomes_secreto}")
    else:
        print(f"Suas tentativas acabaram. O nome secreto era: {nomes_secreto}")

if t_forca == "paises":
    os.system('cls' if os.name == 'nt' else 'clear')
    pais()
elif t_forca == "nomes":
    os.system('cls' if os.name == 'nt' else 'clear')
    nome()
