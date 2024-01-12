import time
from math import sqrt
op = input('Calculadora 2.0\nSelecione uma das opções abaixo: \n[1] Operadores básicos \n[2] Fatorial \n[3] Média\n[4] Tabuada \n[5] Raiz quadrada \n[6] Potência \n[7] Sair\nOpção: ')

while op.isnumeric() != True:
    print('Apenas valores numéricos!')
    time.sleep(3)
    op = input('Calculadora: Selecione uma das opções abaixo: \n[1] Operadores Básicos \n[2] Fatorial \n[3] Média \n[4] Tabuada \n[5] Raiz Quadrada \n[6] Potência \n[7] Sair\nOpção: ')

op = int(op)
while op > 7 or(op < 1):
    print('Selecione um dos valores descritos nas opções!')
    time.sleep(3)
    op = input('Calculadora: Selecione uma das opções abaixo: \n[1] Operadores Básicos \n[2] Fatorial \n[3] Média \n[4] Tabuada \n[5] Raiz Quadrada \n[6] Potência \n[7] Sair\nOpção: ')
    op = int(op)

while op != 7:
    op = int(op)
    if op == 0:
        op = input('Calculadora: Selecione uma das opções abaixo: \n[1] Operadores Básicos \n[2] Fatorial \n[3] Média \n[4] Tabuada \n[5] Raiz Quadrada \n[6] Potência \n[7] Sair\nOpção: ')
        op = int(op)    
    elif op == 1:
        operador = int(input('Selecione o operador:\n[1] Soma\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n[5] Potenciação\n[6] Voltar\nOpção: '))
        if operador == 1:
            n1 = int(input('Primeiro valor: '))
            n2 = int(input('Segundo valor: '))
            print(f'{n1} + {n2} = {n1 + n2}')
        elif operador == 2:
            n1 = int(input('Primeiro valor: '))
            n2 = int(input('Segundo valor: '))
            print(f'{n1} - {n2} = {n1 - n2}')
        elif operador == 3:
            n1 = int(input('Primeiro valor: '))
            n2 = int(input('Segundo valor: '))
            print(f'{n1} X {n2} = {n1 * n2}')
        elif operador==4:
            n1 = int(input('Primeiro valor: '))
            n2 = int(input('Segundo valor: '))
            print(f'{n1} / {n2} = {n1 / n2}')
        elif operador==5:
            n1 = int(input('Primeiro valor: '))
            n2 = int(input('Segundo valor: '))
            print(f'{n1} ** {n2} = {n1 ** n2}')
        elif operador==6:
            op = 0
        op = 0
    elif op == 2:
        c = int(input('Valor a ser calculado: '))
        total = c
        for c in range(c,1,-1):
            total = total * (c - 1)
        print(f'Fatorial = {total}')
        op = 0
    elif op == 3:
        n1 = float(input('Digite um valor:'))
        cont = 0
        soma = 0
        while n1 != 000:
            soma = soma + n1
            cont = cont + 1
            n1 = float(input('Insira mais um valor. Para continuar digite 000. '))
        else:
            total = soma / cont
            print(f'Média total: {total}')
        op = 0
    elif op == 4:
        n1 = int(input('Qual a tabuada que deseja? '))
        c = 1
        while c < 11:
            print(f'{n1} * {c} = {n1 * c}')
            c = c + 1
        op = 0
    elif op == 5:
        n1 = float(input('Valor a ser calculado: '))
        print(f'Raiz quadrada de {n1} = {sqrt(n1)}')
        op = 0
    else:
        n1 = int(input('Base: '))
        n2 = int(input('Expoente: '))
        print(f"{n1} elevado a {n2} é igual a {n1 ** n2}")
        op = 0
print('Até a próxima!')