#Questão 9:

#programa que recebe 10 números inteiros e mostra o maior e o menor ao final
print("Questão 9:")

primeiro = int(input("Insira o primeiro número inteiro:"))
maior = primeiro
menor = primeiro

for numero in range (9):
    novo = int(input("Insira um novo número:"))

    if novo > maior:
        maior = novo
    if novo < menor:
        menor = novo

print("Dentre os 10 numeros digitados,")
print("o maior é:", maior)
print("o menor é:", menor)