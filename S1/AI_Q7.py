#Questão 7:
#programa para verificar se o aluno está reprovado ou aprovado
print("Questão 7:")
ass_entrada = input("Insira a sua assiduidade em porcentagem:")
assiduidade = float(ass_entrada.replace("%", "").replace(",", "."))
nota_entrada = input("Insira a sua nota no teste:")
nota = float(nota_entrada.replace(",", "."))

if 75 > assiduidade:
    print("Seu status atual é: Reprovado (assiduidade insuficiente).")
elif 75 < assiduidade and assiduidade < 100 and 5 > nota:
    print("Seu status atual é: Reprovado (nota insuficiente).")
elif 75 < assiduidade and assiduidade < 100 and 5 <= nota and 9.5 > nota:
    print("Seu status atual é: Realizar novo exame (nota insuficiente).")
else:
    print("Seu status atual é: Aprovado.")