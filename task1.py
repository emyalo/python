#Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('001.txt','w+') as my_file:
    line=input('Введите текст: ')
    while line:
        my_file.writelines(line +'\n')
        line = input('Введите текст: ')
        if not line:
            break
    my_file.seek(0)
    print(f'Введенный текст:\n', my_file.read())