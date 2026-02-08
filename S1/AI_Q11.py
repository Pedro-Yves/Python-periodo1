#Questão 11:
#programa que recebe nome, altura e peso de duas pessoas e diz o nome do mais alto e do mais pesado ao final

print("Questão 11:")

nome1 = input("Digite o nome da primeira pessoa:")
alt1= input("Digite a altura da primeira pessoa:")
altura1 = float(alt1.replace(",", "."))
p1 = (input("Digite o peso da primeira pessoa:"))
peso1 = float(p1.replace(",", ".").replace("kg", ""))
nome2 = input("Digite o nome da segunda pessoa:")
alt2 = (input("Digite a altura da segunda pessoa:"))
altura2 = float(alt2.replace(",", "."))
p2= (input("Digite o peso da segunda pessoa:"))
peso2 = float(p2.replace(",", ".").replace("kg", ""))

if altura1 > altura2:
    print("A pessoa mais alta é:", nome1)
else: 
    print("A pessoa mais alta é:", nome2)
if peso1 > peso2:
    print("A pessoa mais pesada é:", nome1)
else: 
    print("A pessoa mais pesada é:", nome2)