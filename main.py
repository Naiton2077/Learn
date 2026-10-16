#   Калькулятор
#   Автор: Naiton

def calculator(num1, num2, operation):
    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        if num2 != 0:
            return num1 / num2
        else:
            return "Ошибка: Деление на ноль невозможно"
    else:
        return "Ошибка: Неверная операция"
    
print("Добро пожаловать в калькулятор!\n""Выберите операцию:\n""1. Сложение\n""2. Вычитание\n""3. Умножение\n""4. Деление")

try:
    operation = input("Введите номер операции (1/2/3/4): ")
    if operation not in ('1', '2', '3', '4'):
        raise ValueError
except ValueError:
    print("Ошибка: Введите корректный номер.")
    exit()

try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
except ValueError:
    print("Ошибка: Введите корректные числа.")
    exit()

result = calculator(num1, num2, operation)

print(f"Результат: {result}")   


'''
print("Добро пожаловать в калькулятор!")
print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

print ("Введите номер операции (1/2/3/4): ")
operation = input("->  ")

if operation in ('1', '2', '3', '4'):
    num1 = float(input("Введите первое число: "))
    def parse_price(value):
        try:
            return int(value)
        except ValueError:
            return None
    num2 = float(input("Введите второе число: "))
    
    if operation == '1':
        print(num1, "+", num2, "=", num1 + num2)

    elif operation == '2':
        print(num1, "-", num2, "=", num1 - num2)

    elif operation == '3':
        print(num1, "*", num2, "=", num1 * num2)

    elif operation == '4':
        if num2 != 0:
            print(num1, "/", num2, "=", num1 / num2)
        else:
            print("Ошибка: Деление на ноль невозможно")'''