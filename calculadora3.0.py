from time import sleep
import math

def verificaNumero(op):
    op =int(op)
    while op > 7 or op <1:
        print('Selecione apenas um dos valores do Menu!')
        sleep(3)
        break

def soma():
    n1 = float(input('Valor: '))
    total = 0
    while n1 != 000:
        total = total + n1
        n1 = float(input('Para obter o total digite 000.\nNovo valor: '))
    return total

def subtracao():
    itens = []
    n1 = float(input('Valor: '))
    while n1 != 000:
        n1 = float(input('Para obter o total, digite 000.\nNovo valor: '))
        itens.append(n1)
    else:
        qtd = len(itens)
        c = 0
        for c in range(c, qtd):
            total = itens[qtd] - itens[qtd + 1]
    return total

def multiplica():
    n1 = float(input('Valor: '))
    total = 0
    while n1 != 000:
        total = total * n1
        n1 = float(input('Para obter o total, digite 000.\nNovo valor: '))
    return total

def divide():
    n1 = float(input('Primeiro valor: '))
    n2 = float(input('Segundo valor: '))
    total = n1 / n2
    return total

def pot():
    n1 = int(input('Base: '))
    n2 = int(input('Expoente: '))
    total = print(f'{n1} ** {n2} = {math.pow(n1,n2)}')
    return total

def fatorial():
    c = int(input('Valor a ser calculado: '))
    total = c
    for c in range(c,1,-1):
        total = total * (c - 1)
    final = print(f'Fatorial = {total}')
    return final

def media():
    n1 = float(input('Digite um valor:'))
    cont = 0
    soma = 0
    while n1 != 000:
        soma = soma + n1
        cont = cont + 1
        n1 = float(input('Insira mais um valor. Para continuar digite 000. '))
    else:
        total = soma / cont
        resultado = print(f'Média total: {total}')
    return resultado 

def tabuada():
    tbl_tabuada = []
    n1 = int(input('Qual a tabuada que deseja? '))
    c = 1
    while c < 11:
        resultado = print(f'{n1} * {c} = {n1 * c}')
        tbl_tabuada.append(resultado)
        c = c + 1
    return tbl_tabuada
    
def raiz():
    n1 = float(input('Valor a ser calculado: '))        
    resultado = print(f'Raiz quadrada de {n1} = {math.sqrt(n1)}')
    return resultado

def conversor():
    cot = float(input('Dólar hoje: '))
    dol = float(input('Total de dólares: USD $ '))
    reais = cot * dol
    valor = print('Total em reais: R$ ', reais)
    return valor

op = input('Calculadora:\nSelecione uma das opções abaixo: \n[1] Operadores básicos \n[2] Fatorial \n[3] Média\n[4] Tabuada \n[5] Raiz quadrada \n[6] Conversor de moeda \n[7] Sair\nOpção: ')
verificaNumero(op)

op = int(op)
match op:
    case 1:
        operador = int(input('Selecione o operador:\n[1] Soma\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n[5] Potenciação\n[6] Voltar\nOpção: '))
        if operador == 1:
            print(f'O total dos valores somados é: {soma()}')
        elif operador == 2:
            print(f'O total da subtração solicitada é: {subtracao()}') #FINALIZAR COMANDO DE SUBTRAÇÃO
        elif operador == 3:
            print(f'A muliplicação entre os valores solicitados é {multiplica()}')
        elif operador == 4:
            print(f'Total: {divide()}')
        elif operador==5:
            pot()
        elif operador==6:
            op = 0
    case 2:
        fatorial()
        op = 0
    case 3:
        media()
    case 4:
        tabuada()
        c = 0
        for c in range(0,9):
            print(f'{tabuada[c]}')
            c = c + 1
    case 5:
        raiz()
    case 6:
        conversor()
    case 7:
        print('Obrigado por usar a calcluadora!')
        sleep(2)
        print('Até a próxima.')



