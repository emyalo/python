# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

list1= [7,5,3,2]
print(f'Первоначальный список - {list1}')
try:
    n = int(input('Введи число, которое добавится в рейтинг: '))
    for el in range(len(list1)):
        if list1[el]== n:
            list1.insert(el+1,n)
        elif list1[0]<n:
            list1.insert(0,n)
        elif list1[-1]>n:
            list1.append(n)
        elif list1[el]>n and list1[el+1]<n:
            list1.insert(el+1,n)
    print(f'Результат - {list1}')
except ValueError:
    print('Введено не число! Попробуй еще раз')