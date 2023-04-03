"""Calculadora com while"""

while True:
    operadores = "+-*/"

    primeiro_numero = int(input("Digite um número: "))
    operacao = input("Digite uma operação (+ - * /): ")

    if operacao not in operadores:
        print("Operador inválido.")
        continue

    if len(operacao) > 1:
        print("Digite apenas um operador.")

    segundo_numero = int(input("Digite outro número: "))

#OPERAÇÕES
    if operacao == "+":
        resultado = primeiro_numero + segundo_numero
    elif operacao == "-":
        resultado = primeiro_numero - segundo_numero
    elif operacao == "*":
        resultado = primeiro_numero * segundo_numero
    elif operacao == "/":
        resultado = primeiro_numero // segundo_numero
    print(resultado)

    sair = input("Quer sair? [s]im: ").lower().startswith("s")
    if sair:
        break