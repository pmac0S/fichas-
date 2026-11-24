abastecimentos = []
while True:
    aba = float(input("Digite o valor do abastecimento (R$): "))
    if aba <= 0:
        print("PARADA")
        break
    else:
        abastecimentos.append(aba)
        media = sum(abastecimentos) / len(abastecimentos)
print(f"A média: {media}")
print(f"Total de abastecimentos: {len(abastecimentos)}")
print(f"Valor total: R${sum(abastecimentos)}")
