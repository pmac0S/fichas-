produto = []
quantidade = []

while True:
    print("\n=== Loja de brinquedos ===")
    print("Opções:")
    print("A. Adicionar um novo produto e sua quantidade;")
    print("V. Visualizar os elementos e quantidades do estoque;")
    print("Q. Quantidade de brinquedos cadastrados;")
    print("S. Encerrar programa.")

    opcao = input("Digite uma opção (A, V, Q, S): ")

    if opcao == "A" or opcao == "a":
        nome = input("Digite o nome do produto: ")
        quant = int(input("Digite a quantidade: "))

        if quant <= 0:
            print("Quantidade inválida!")
        else:
            produto.append(nome)
            quantidade.append(quant)

# duvida que voe tinha para separar os elementos individualmente
    elif opcao == "V" or opcao == "v":
        for i in range(len(produto)):
            print(f"Produto: {produto[i]} | Quantidade: {quantidade[i]}")

    elif opcao == "Q" or opcao == "q":
        print(f"Quantidade de brinquedos: {sum(quantidade)}")

    elif opcao == "S" or opcao == "s":
        if len(produto) == 0:
            print("Nenhum brinquedo foi cadastrado.")
        else:
            print(f"Total: {sum(quantidade)}")
            print(f"Maior estoque: {max(quantidade)}")
            print(f"Menor estoque: {min(quantidade)}")

        print("Encerrando programa!")
        break

    else:
        print("Opção inválida!")
