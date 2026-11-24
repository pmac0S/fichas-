# atividade de operadores e condicionais
preço = float(input("Digite o preço da impressão (R$): "))
quantidade = int(input("Digite a quantidade de panfletos: "))
preco_total = preço * quantidade
if quantidade >= 500:
    preco_total = preco_total - (preco_total * 0.3) # voce não estava guardando o valor do desconto em preco_total

print(f"Valor final: R${preco_total:.2f}")
