print('Вариант 1')

def count_num(quantity, operation):
  meaning_num = ''
  meaning = 1
  for num in range(1, quantity + 1):
    number = int(input(f'Введите операнд {num}:'))
    if operation == '+':
      meaning += number
      if num < quantity:
        meaning_num += str(number) + operation # здесь всё работает
      elif num == quantity:
        print(meaning_num + str(number), '=', meaning - 1)
    elif operation == '-':
      meaning -= number
      if num < quantity:
        meaning_num += str(number) + operation # здесь всё работает
      elif num == quantity:
        print(meaning_num + str(number), '=', meaning - 1)
    elif operation == '*':
      meaning *= number
      if num < quantity:
        meaning_num += str(number) + operation # здесь всё работает
      elif num == quantity:
        print(meaning_num + str(number), '=', meaning)
    elif operation == '/':
      meaning /= number
      if num < quantity:
        meaning_num += str(number) + operation # здесь всё работает
      elif num == quantity:
        print(meaning_num + str(number), '=', meaning)
    else:
      print('Ошибка ввода.')
      


def main_menu():
  operation = input('Введите операцию: ')
  quantity = int(input('Сколько операндов? '))
  count_num(quantity, operation)

main_menu()