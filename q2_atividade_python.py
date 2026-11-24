unidades = []
preco = []
vendas = []

maior = 0
menor = 0

for i in range(1, 26):
    unidades.append(int(input("Digite a quantidade de unidades vendidas: ")))
    preco.append(float(input("Digite o preço unitário do medicamento (R$): ")))

    valor = unidades[i - 1] * preco[i - 1] # não entendi essa parte
    vendas.append(valor)

    if valor > 50:
        maior += 1
    else:
        menor += 1

mais_cara = max(vendas)
mais_barata = min(vendas)

print(f"Vendas acima de R$50: {maior}")
print(f"Vendas até R$50: {menor}")
print(f"Venda mais cara: R${mais_cara:.2f}")
print(f"Venda mais barata: R${mais_barata:.2f}")

####################################################################################

vendas = []
maior = 0
menor = 0

for i in range(1, 26):
    unidades = int(input("Digite a quantidade vendida: "))
    preco = float(input("Digite o preço unitário: "))

    valor = unidades * preco
    vendas.append(valor)

    if valor > 50:
        maior += 1
    else:
        menor += 1

print(f"Vendas acima de R$50: {maior}")
print(f"Vendas até R$50: {menor}")
print(f"Venda mais cara: R${max(vendas):.2f}")
print(f"Venda mais barata: R${min(vendas):.2f}")
