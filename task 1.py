# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

try:
    def division(x, y):
        a = x / y
        return round(a,3)
    print(f'Результат деления -', division(int(input('Введите числитель: ')), int(input('Введите знаменатель: '))))
except ValueError:
    print('Нельзя делить не на число! Введите число.')
except ZeroDivisionError:
    print('Нельзя делить на ноль! Введите другое число.')