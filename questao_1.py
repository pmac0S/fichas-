#Questão 1 da ficha de exercício:
notas = 0
while True:
    nota = int(input("Digite a sua nota: "))
    if nota == -1:
        break
    elif nota < -1:
        print("Numero inválido, tente de novo!")
    else:
        notas+= 1
soma = notas + nota
media = soma / notas
print(f"A quantidade de notas foi {notas}.")
print(f"A média das notas foi {media}.")


print("\nseparação\n")


notas = 0
soma = 0
maior = 0
menor = 0

while True:
    nota = int(input("Digite sua nota: "))

    if nota == -1:
        break

    elif nota < 0 or nota > 10:
        print("Número inválido, tente novamente!")


    else:
        notas += 1
        soma += nota

        if notas == 1:
            maior = nota
            menor = nota

        if nota > maior:
            maior = nota

        if nota < menor:
            menor = nota

if notas > 0:
    media = soma / notas

    print(f"Quantidade de notas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Maior nota: {maior}")
    print(f"Menor nota: {menor}")
else:
    print("Nenhuma nota foi informada.")

#teste de atualização do repositório 