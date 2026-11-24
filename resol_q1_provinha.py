lista = []
while len(lista) < 8:
    valor = float(input(f"Digite o {len(lista) + 1} valor: "))
    if valor <=0:
        print ("Valor inválido!")
        continue
    lista.append(valor)
media = sum(lista) / len(lista)
print (f"Soma total dos gastos: R${sum(lista)}")
print(f"Média dos gastos: R${media:.2f}")

# raciocínio para o primeiro gasto acima de 100
for i in range (len(lista)):
    if lista[i] > 100:
        print(f"Posição do primeiro gasto acima de R$100,00: {i}")
    else:
        print("Nenhum gasto acima de R$100,00 foi encontrado")
print(f"Maior gasto registrado: R${max(lista):.2f}")
