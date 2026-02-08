#Questão 4:
#programa pra mostrar a idade em dias
print("Questão 4:")
print("Digite a sua idade em anos, meses e dias.")
anos = int(input("Insira quantos anos de idade você tem:"))
meses = int(input("Insira quantos meses:"))
dias = int(input ("Insira quantos dias:"))
anos_emdias = anos * 365
meses_emdias = meses * 30 
idade_emdias = (anos_emdias + meses_emdias + dias)
print("A sua idade em dias é:",idade_emdias,"dias")
