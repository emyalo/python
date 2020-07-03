#Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    z = [a, b, c]
    z.remove(min(a, b, c))
    return sum(z)
print(f'Сумма двух наибольших чисел=',my_func(int(input('Введите первое число: ')), int(input('Введите второе число: ')),
              int(input('Введите третье число: '))))

#два альтернативных решения - перевобором комбинаций ( всего есть 3 возможных варианта суммы), выделением перевоба максимумов
#альтернатива 1
def my_func(x, y, z):
    sequence = [x, y, z]
    total = []
    max_1 = max(sequence)
    total.append(max_1)
    sequence.remove(max_1)
    max_2 = max(sequence)
    total.append(max_2)
    return sum(total)
print(f'Сумма двух наибольших чисел=',my_func(int(input('Введите первое число: ')), int(input('Введите второе число: ')),
              int(input('Введите третье число: '))))

#альтернатива 2
def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3
print(f'Сумма двух наибольших чисел=',my_func(int(input('Введите первое число: ')), int(input('Введите второе число: ')),
              int(input('Введите третье число: '))))