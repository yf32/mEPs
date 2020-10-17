peso = float(input()) # kg
idade = int(input()) # anos
if idade == 16 or idade == 17:
    documento = input()

saude = input() # S N
uso_Drogas = input() # S N

primeira_Doação = input() # S N
if primeira_Doação == "N":
    ultima_doacao_meses = int(input())
    doacoes_ult_meses = int(input())

sexo_B = input() # M F
if sexo_B == 'F':
    gravidez = input()
    if gravidez == "S":
        amamentando = input()
        if amamentando == 'S':
            idade_bebe = int(input())

# Saída 1
print('Peso:', peso)
print('Idade:', idade)
print('Documento de autorizacao:', documento)
print('Boa saude:', saude)
print('Uso drogas injetaveis:', uso_Drogas)
print('Primeira doacao:', primeira_Doação)
print('Meses desde ultima doacao:', ultima_doacao_meses)
print('Doacoes nos ultimos 12 meses:', doacoes_ult_meses)
print('Sexo biologico:', sexo_B)
print('Gravidez:', gravidez)
print('Amamentando:', amamentando)
print('Meses bebe:', idade_bebe)
