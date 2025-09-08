print('Primeiro programa em python')
print('Faça suas somas, subtrações, divisões e multiplicações')

valor = int(input('Digite seu numero desejado: '))
valor2 = int(input('Digite seu numero desejado: '))
tesao = input('operção desejada: ') 
if tesao == 'soma': 
  print('soma', valor + valor2)
elif tesao == 'subtração': 
  print('subtração', valor - valor2)
elif tesao == 'divisão': 
  print('divisão', valor / valor2)
elif tesao == 'multiplicação': 
  print('mutiplicação', valor * valor2)
