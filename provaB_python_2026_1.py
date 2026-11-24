# lista de hóspedes em um hotel:
nome = []
idade = []
while True:
    intera = input("Deseja adicionar um novo hóspede? (SIM/NÃO): ").upper()
    if intera == "SIM":
        nom = input("Digite o nome completo do hóspede: ")
        id = int(input("Digite a idade do hóspede: "))
        if id < 18:
            print("Hóspede não está apto para essa área!")
        else:
            nome.append(nom)
            idade.append(id)
    elif intera == "NÃO" or intera == "NAO":
        print("Encerrando!")
        break
    else:
        print("resposta inválida!")
for i in range (len(nome)):
    print(f"Nome: {nome[i]}   idade: {idade[i]}")

media = sum(idade) + len(idade)

print(f"A média das idades: {media}")
print(f"A quantidade de candidatos: {len(nome)}")
