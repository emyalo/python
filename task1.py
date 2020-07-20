# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, d_m_y):
        self.d_m_y = str(d_m_y)
    @classmethod
    def get_date(cls, d_m_y):
        my_date = []
        for i in d_m_y.split():
            if i != '.': my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])
    @staticmethod
    def check(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if  0<= year<= 2020:
                    return f'Дата введена правильно'
                else:
                    return f'Введен год вне диапазона'
            else:
                return f'Введен неправильный месяц, их всего 12'
        else:
            return f'Введен неправильный день, их всего 31'
    def __str__(self):
        return f'Текущая дата {Date.get_date(self.d_m_y)}'


print(Date.check(20, 7, 2022))
print(Date.get_date('20 . 7 . 2020'))
print(Date.check(10, 8, 2020))
