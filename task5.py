#Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

try:
    with open('005.txt', 'w+') as my_file:
        line = input('Введите цифры через пробел: ')
        my_file.writelines(line)
        numbers = line.split()
        print(f'Сумма введенных в файл 005.txt равна ', sum(map(int, numbers)))
except IOError:
    print('Ошибка. Попробуйте еще раз.')
except ValueError:
    print('Вы ввели не числа, введите числа.')