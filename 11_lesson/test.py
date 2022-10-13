def calculate(a, b, operation):
   result = None

   if operation == '+':
       result = sum(a, b)
   elif operation == '-':
       result = subtract(a, b)
   elif operation == '/':
       result = divide(a, b)
   elif operation == '*':
       result = multiply(a, b)
   else:
       print('huo')

def run_calculator():
   # Запрашиваем данные
   a = int(input('Введите первое число: '))
   b = int(input('Введите второе число: '))

   # Запрашиваем тип операции
   operation = ask_operation()

   # Производим вычисления
   result = calculate(a, b, operation)

   # Выводим результат в консоль
   print(f'Результат вычислений: {result}')
