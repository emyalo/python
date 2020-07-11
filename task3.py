# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

# from statistics import mean
# with open('003.txt', 'r') as my_file:
#     salary = []
#     low_income = []
#     my_list = my_file.read().split('\n')
#     for line in my_list:
#         i= line.split()
#         salary.append(i[1])
#         if int(i[1]) < 20000:
#             low_income.append(i[0])
# print(f'Оклад меньше 20.000 {low_income}, средний оклад {mean(salary)}')


summa = 0
quantity=0
persons = []
with open("003.txt", "r") as my_file:
    for line in my_file:
        money = line.split(':')
        if int(money[1]) <= 20000:
            persons.append(money[0])
        summa += int(money[1])
        quantity+=1
average=summa/quantity
print(f"Список тех, кто получает меньше 20000: {persons}")
print(f"Средняя зарплата: {average}")