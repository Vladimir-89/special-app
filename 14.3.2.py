def action():
  operation = input('Введите операцию: ')
  first_num = int(input('Введите первое число: '))
  second_num = int(input('Введите второе число: '))
  if operation == '+':
    print(first_num, '+', second_num, '=', first_num + second_num)
  elif operation == '-':
    print(first_num, '-', second_num, '=', first_num - second_num)
  elif operation == '*':
    print(first_num, '*', second_num, '=', first_num * second_num)
  elif operation == '/':
    print(first_num, '/', second_num, '=', first_num / second_num)
  else:
    print('Ошибка ввода.')
  action()

action()