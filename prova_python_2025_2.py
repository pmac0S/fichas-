nome = []
idade = []
while True:
    add = input("Deseja adicionar um novo aluno? (SIM/NÃO): ") # essa é a parte de cada interação, perguntar se ele quer algo ou não

    if add == "sim" or add == "SIM":
        nom = input("Digite o nome completo do aluno: ")
        id = int(input("Digite a idade do aluno: "))

        if id < 18:
            print("Aluno não esta ápto ao intercambio")
        else:
            nome.append(nom)
            idade.append(id)

        for i in range(len(nome)):
            print(f"Nome: {nome[i]} | idade: {idade[i]}")

    elif add == "NÃO" or add == "nao" or add =="não" or add == "NÃO":
        break
    else:
        print("Escolha não identificada!")

media = sum(idade) / len(idade)

print(f"quantidade de alunos: {len(nome)}")
print(f"A média de idades:{media:.2f}")

# como faz para atribuir um nome a uma idade? Essa associaçãpo acontece através dos indices
# o nome de tal pessoa, e a idade dessa mesma pessoa?
