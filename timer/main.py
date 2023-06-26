import time 

def timer(segundo):
    Start = time.time()
    end = Start + segundo

    while time.time() < end:
        tempo_restante = int(end - time.time()) 
        minutos = tempo_restante // 60 
        segundos = tempo_restante % 60 
        print(f"Tempo restante: {minutos:02d}:{segundos:02d}", end ="\r")
        time.sleep(1)
    print("Tempo esgotado!")


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = "Tempo restante: {:02d}:{:02d}".format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Tempo esgotado!")

timer_select = input("Qual tipo de timer vc quer(regresivo, normal): ")

if timer_select == "normal":
    tempo_total = int(input("Digite o tempo em segundo:"))
    timer(tempo_total)
elif timer_select == "regressivo":
    t = int(input("Digite o tempo em segundo: "))
    countdown(int(t))



