eixo_X = float(input())
eixo_Y = float(input())
if eixo_X >= 0 and eixo_Y >= 0:
    print("I")
elif eixo_X <= 0 and eixo_Y > 0:
    print("II")
elif eixo_X >= 0 and eixo_Y < 0:
    print("IV")
elif eixo_X < 0 and eixo_Y < 0:
    print("III")
else:
    print("Valor inválido!")
