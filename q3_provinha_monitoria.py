# traduzir a temperatura de um termometro
frio = []
moderado = []
quente = []
while True:
    temp = float(input("Digite a temperatura: "))
    if temp < 10:
        print("Muito frio")
        frio.append(temp)
    elif temp >=10 and temp<=23:
        print("Moderada")
        moderado.append(temp)
    elif temp >23:
        print("Muito quente")
        quente.append(temp)
