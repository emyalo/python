# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый
# текстовый файл.


russian = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_my_file = []
with open('004.txt', 'r') as my_file:
    for i in my_file:
        i = i.split(' ', 1)
        new_my_file.append(russian[i[0]] + '  '+ i[1])
with open('004new.txt', 'w') as my_file_new:
    my_file_new.writelines(new_my_file)