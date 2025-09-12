usuario = {
  'nome': input('Digite seu nome: '),
  'idade': input('Digite sua idade: '),
  'departamento': input('Digite seu departamento: '),
}

print(f"Olá {usuario['nome']} do departamento {usuario['departamento']}, você tem {usuario['idade']} anos.")

print('Escolha as seguines funções disponiveis para você: (1) Cadastrar, (2) Calculadora, (3) espediente, (4) exit')
função = input('Digite a função que deseja executar: ')

if função == '1':
  print('Você escolheu a função de cadastro.')
  usuario2 = input('Digite seu usuario: ')
  usu = input('Digite sua senha: ')
  print(f'Você se cadastrou como {usuario2} e sua senha é {usu}, obrigado por se cadastrar.')
elif função == '2':
  print('Você escolheu a função de calculadora.')
  preco = int(input('Numeral: '))
  operador = input('Qual seu operador: ')
  preco2 = int(input('Numeral: '))

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
elif função == '4':
  print('Você escolheu a função de exit.')
  exit()
elif função == '3':
  print(f"Você escolheu a função {usuario['departamento']}.")
  turno = input('Qual turno desejado: ')
  print('======================================================')
  if turno == 'manha':
    print('Você ira trabalhar das 8:00 as 12:00')
  elif turno == 'tarde':
    print('Você ira trabalhar das 13:00 as 17:00')
  elif turno == 'noite':
    print('Você ira trabalhar das 18:00 as 22:00')
else:
  print('Função invalida')
