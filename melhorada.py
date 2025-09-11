#calculator

preco = int(input('Qual seu preço: '))
operador = input('Qual seu operador: ')
preco2 = int(input('Qual seu desconto: '))

print('==============================')

if operador == '%'  :
  print(int(preco - preco * preco2 / 100))
elif operador == '+'  :
  print(int(preco + preco2))
elif operador == '-'  :
  print(int(preco - preco2))
elif operador == '/'  :
  print(int(preco / preco2))
elif operador == '*'    :
  print(int(preco * preco2))
else:
  print('Operador invalido')
