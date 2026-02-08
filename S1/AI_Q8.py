#Questão 8:
#programa que calcula quantos números pares tem em um intervalo e a somatória deles

print("Questão 8:")
print("Programa de cálculo de numeros pares e seu somatório em um intervalo entre dois números.")
começo = int(input("Insira o valor que dá inicio ao intervalo:"))
final = int(input("Insira o valor que dá um fim ao intervalo:"))
somatorio = 0

for value in range (começo + 1, final):
    if value % 2 == 0:
        print(value)
        somatorio = somatorio + value
print("O somatório dos números pares entre", começo, "e", final, "é:",somatorio)