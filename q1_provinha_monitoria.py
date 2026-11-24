# questão 1 da provinha monitoria

lista = []
for i in range (1,9):
    valor = float(input(f"Digite o {i} valor: "))
    if valor <= 0:
        print ("Valor inválido!")
        continue
    lista.append(valor)
media = sum(lista)/len(lista)
print(f"Soma total dos gastos:{sum(lista)}")
print(f"Média de gastos: R${media:.2f}")
print(f"Maior gasto registrado: R${max(lista)}")

# não precisa colocar lista.pop(vaor, porque esta errado
# não precisa colocar o lista.sort(), é desnecessário
# o uso da estrutura de repetição for ta correto, porém aqui não podemos aplicar essa lógica, porque como a questão pede para ser ignorado números iguais ou menores que 0
# usar o for (1, 9) vai limitar apenas a inserção de 8 valores, mesmo que este seja igual ou menor que 0