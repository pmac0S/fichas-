# questão 2 da provinha da monitoria
produto = []
quantidade = []
while True:
    print("\n=== lojda de brinquedos ===")
    print("Opções:")
    print("A.Adicionar um novo produto e sua quantidade;")
    print("V.Visualizar os elementos e quantidades do estoque;")
    print("Q.Quantidade de brinquedos cadastrados;")
    print("S.Encerrar programa.")
    opcao = input("Digite uma opção (A, V, Q, S): ")
    if opcao == "A" or opcao == "a": # falta a validação de quantidades, para quantdades menores que 0
        nome = input("Digite o nome do produto: ")
        quant = int(input("Digite a quantidade: "))
        produto.append(nome)
        quantidade.append(quant)
    elif opcao == "V" or opcao == "v":
        print(f"Elemetos:{produto}.  Quantidade;{quantidade}")
    elif opcao == "Q" or opcao == "q":
        print(f"Quantidade de brinquedos cadastrados até o momento:{sum(quantidade)}") # soma a quantidade de brinquedos cadastrados
    elif opcao == "S" or opcao =="s":
        print("Encerrando programa!")
        break
    else:
        print("Opção inválida!")

# dúvida: como faço para visualizar cada brinquedo/produto individualmente
# porque até aqui eu estou "imprimindo" as listas inteiras, e não cada elemento individualmente

#problemas:
# validação de quantidade. A questão pede que quantidades menores ou iguais a zero sejam rejeitadas.
# foi adicionado a soma das quantidades dos brinquedos com {sum(quantidade)}
# A questão pede que você verifique se o estoque está vazio e, caso contrário, mostre o total, o maior e o menor estoque.
