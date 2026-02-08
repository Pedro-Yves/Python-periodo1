#Questão 10:
#Programa pra ler idades de várias pessoas e calcular a média entre as idades (parar apeans quando alguém digitar idade 0)
print ("Questão 10: ")

total = 0 
quantidade = 0

idade = int(input("Digite a sua idade (ou 0 para encerrar):"))

while idade != 0:
    total = total + idade
    quantidade = quantidade + 1
    idade = int(input("Digite a sua idade (ou 0 para encerrar):"))

media = total / quantidade
print ("A média das idades é:", media)
