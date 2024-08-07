# Lista de programas indicados
def menor():
    print("Eis, os programas ideais para você:")
    print("Teletubies, Tom & Jerry, Xou da Xuxa...")
    return
def maior():
    print("Eis, boas notícias de carro para comprar:")
    print("Fiat 147, VW fusca, Chevette...")
    return

print("Digite a sua idade:")
idade = int(input())

if idade < 18:
    menor()
else:
    maior()

print("Se beber, não dirija...")