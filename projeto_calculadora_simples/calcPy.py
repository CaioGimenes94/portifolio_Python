x = float(input('Insira um número: '))
param = ''
l1 = ['+', '-', '/', '*']

while param not in l1:
    param = input('Digite um operador válido (+ - / *): ')

y = float(input('Insira outro número: '))

if param == '+':
      print(f'O resultado é {x + y}')elif
elif param == '-':
    print(f'O resultado é {x - y}')
elif param == '/':
    while y == 0:
        y = float(input('Não é possível dividir por zero. Insira outro valor: '))
    print(f'O resultado é {x / y}')
elif param == '*':
    print(f'O resultado é {x * y}')
