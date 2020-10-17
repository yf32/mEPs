# Notas João
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
# Notas Maria
nota4 = float(input())
nota5 = float(input())
nota6 = float(input())

joao_Aprovado = (nota1 >= 7) and (nota2 >= 7) and (nota3 >= 7)
maria_Aprovada = (nota4 >= 7) and (nota5 >= 7) and (nota6 >= 7)

ferias_Eduardo = input()
ferias_Monica = input()
ferias = (ferias_Eduardo == "Sim") and (ferias_Monica == "Sim")

dia_salario_Eduardo = int(input())
dia_salario_Monica = int(input())
salario = (dia_salario_Eduardo <= 15) or (dia_salario_Monica <= 15)

valor_Hotel = float(input())
valor_Passagens = float(input())
valor_Total = valor_Hotel + valor_Passagens
valor_OK = valor_Total <= 10000

irao_Viajar = joao_Aprovado and maria_Aprovada and ferias and salario and valor_OK

# Relatório
print("Joao aprovado em todas as disciplinas?", joao_Aprovado)
print("Maria aprovada em todas as disciplinas?", maria_Aprovada)
print("Eduardo e Monica de ferias de dezembro?", ferias)
print("Pagamento de Eduardo ou Monica liberado a tempo?", salario)
print("Valor total menor ou igual a R$10.000,00?", valor_OK)
print("Irao viajar?", irao_Viajar)
