#Questão 3:
#programa que calcula a porcentagem de cada tipo de voto dentro do total de eleitores de uma cidade
print("Questão 3:")
total_eleitores = float(input("Insira o total de eleitores no município: "))
votos_brancos = float(input("Insira o total de votos brancos obtidos: "))
votos_nulos = float(input("Insira o total de votos nulos obtidos: "))
votos_validos = float(input("Insira o total de votos válidos obtidos: "))
pct_nulos = (votos_nulos / total_eleitores) * 100
pct_brancos = (votos_brancos / total_eleitores) * 100
pct_validos = (votos_validos / total_eleitores) * 100

if (votos_brancos + votos_nulos + votos_validos) > total_eleitores:
    print("O total de votos não pode ser maior que a quantidade de eleitores")

else:
    print("A quantidade de votos nulos corresponde a:",pct_nulos, "%")
    print("A quantidade de votos brancos corresponde a:",pct_brancos, "%")
    print("A quantidade de votos válidos corresponde a:",pct_validos, "%")