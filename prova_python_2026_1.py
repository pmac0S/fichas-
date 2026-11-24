# lista de voluntários
nome = []
idade = []

# estrutura de repetição
while True:
    # a cada interação o código vai perguntar
    interacao = input("Deseja adicionar um novo candidato? (SIM/NÃO): ").upper() # .upper() deixa a resposta maiúscula
    if interacao == "SIM":
        nom = input("Digite o nome completo do candidato: ")
        id = int(input("Digite a idade do candidato: "))

        # aceitar só candidatos acima de 18 anos
        if id < 18:
            print("Candidato não está ápto!")
        else:
            nome.append(nom)
            idade.append(id)

    elif interacao == "NÃO" or interacao == "NAO":
        print("Encerrando programa.")
        break
    else:
        print("Resposta inválida!")

# código para visualizar cada candidato correspondete a sua idade (visualizar cada nome)
for i in range(len(nome)):
    print(f"{nome[i]} {idade[i]} anos")

# código para média de idades na lista
media = sum(idade) / len(idade) # sum soma tudo, len conta quantos elementos

# saída de dados
print(f"A média dos candidatos:{media}")
print(f"A quantidade de candidatos áptos foi: {len(nome)}")

# FALTANDO:
# precisar descobrir o voluntário mais novo e o mais velho
