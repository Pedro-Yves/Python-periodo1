#Questão 6:
#programa de cálculo do valor de venda de um produto
print("Questão 6:")
print("Seja bem vindo(a). Para calcular o valor de venda do produto,")
valor_compra = float(input("insira o valor de compra: "))


if 10 > valor_compra:
    taxa = 0.70
elif 10 <= valor_compra and valor_compra < 30:
    taxa = 0.50
elif 30 <= valor_compra and valor_compra < 50:
    taxa = 0.40
else:
    taxa = 0.30

valor_venda = valor_compra * (1 + taxa)

print(f"Valor de compra: R${valor_compra:.2f}")
print("Taxa de lucro: ",taxa * 100, "%")
print(f"Valor de venda: R${valor_venda:.2f}")