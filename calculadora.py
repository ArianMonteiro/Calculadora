
import time
op = input('Calculadora: Selecione uma das opções abaixo: \n[1] Soma \n[2] Subtração \n[3] Multiplicação \n[4] Tabuada \n[5] Divisão \n[6] Potência \n[7] Sair\nOpção: ')

while op.isnumeric() != True:
    print('Apenas valores numéricos!')
    time.sleep(3)
    op = input('Calculadora: Selecione uma das opções abaixo: \n[1] Soma \n[2] Subtração \n[3] Multiplicação \n[4] Tabuada \n[5] Divisão \n[6] Potência \n[7] Sair\nOpção: ')

op = int(op)
while op > 7 or(op < 1):
    print('Selecione um dos valores descritos nas opções!')
    time.sleep(3)
    op = input('Calculadora: Selecione uma das opções abaixo: \n[1] Soma \n[2] Subtração \n[3] Multiplicação \n[4] Tabuada \n[5] Divisão \n[6] Potência \n[7] Sair\nOpção: ')
    op = int(op)

while op != 7:
    op = int(op)
    if op == 0:
        op = input('Calculadora: Selecione uma das opções abaixo: \n[1] Soma \n[2] Subtração \n[3] Multiplicação \n[4] Tabuada \n[5] Divisão \n[6] Potência \n[7] Sair\nOpção: ')
        op = int(op)    
    elif op == 1:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print(f'{n1} + {n2} = {n1 + n2}')
        op = 0
    elif op == 2:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print(f'{n1} - {n2} = {n1 - n2}')
        op = 0
    elif op == 3:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print(f'{n1} * {n2} = {n1 * n2}')
        op = 0
    elif op == 4:
        n1 = int(input('Qual a tabuada que deseja? '))
        c = 1
        while c < 11:
            print(f'{n1} * {c} = {n1 * c}')
            c = c + 1
        op = 0
    elif op == 5:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print(f'{n1} / {n2} = {n1 / n2}')
        op = 0
    else:
        n1 = int(input('Base: '))
        n2 = int(input('Expoente: '))
        print(f"{n1} elevado a {n2} é igual a {n1 ** n2}")
        op = 0
print('Até a próxima!')
