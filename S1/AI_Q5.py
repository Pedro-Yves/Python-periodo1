#Questão 5:
#programa de verificação de categorias de atletismo de acordo com a idade
print("Questão 5:")
idade = int(input("Digite sua idade para verificar qual categoria de atletas você pertence:"))
if idade >= 5 and idade <= 7:
    print("Você está na categoria Infantil (5 a 7 anos de idade).")
elif idade >= 8 and idade <= 10:
    print("Você está na categoria Iniciado ( 8 a 10 anos de idade).")
elif idade >= 11 and idade <= 13:
    print("Você está na categoria Juvenil ( 11 a 13 anos de idade).")
elif idade >= 14 and idade <= 17:
    print("Você está na categoria Junior ( 14 a 17 anos de idade).")
elif idade >= 18:
    print("Você está na categoria Senior (18 anos de idade ou mais).")
