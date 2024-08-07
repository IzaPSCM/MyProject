# demonstração do uso de funções + multiplicacao
def adicao (X, Y):
    W = X + Y
    return W 
def subtracao(X, Y):
    return X - Y
def multiplicacao(X, Y):
    return X * Y
def divisao(X, Y):
    return X / Y

print("Digite dois valores inteiros...")
n1 = int(input("X: "))
n2 = int(input("Y: "))
op = input("Qual operação (+, -, * ou /)?")

if op == "+":
    z = adicao(n1, n2)
    print("Resultado da soma:", z)
elif op == "-":
    z = subtracao(n1, n2)
    print("Resultado da subtração:", z)
elif op == "*":
    z = multiplicacao(n1, n2)
    print("O resultado da multiplicação:", z)
elif op == "/":
    z = divisao(n1, n2)
    print("O resultado da divisão:", z)
else:
    print("Opção digitada inexistente!")
