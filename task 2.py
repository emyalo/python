#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
#имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

name=input('Введите имя: ')
surname=input('Введите фамилию: ')
year=input('Введите год рождения: ')
city=input('Введите город проживания: ')
email=input('Введите email: ')
tel=input('Введите телефон: ')

def information(name, surname, year, city, email, tel):
    return ', '.join([name, surname, year, city, email, tel])
print(f'Введенные данные следующие: ',information(name, surname, year, city, email, tel))

