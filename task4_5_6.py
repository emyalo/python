# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
# передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
# на уроках по ООП.

class ОfficeEquipment:
    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name=name
        self.price=price
        self.quantity=quantity
        self.numb = number_of_lists
        self.store_full = []
        self.store = []
        self.unit = {'Наименование техники: ': self.name, 'Стоимость: ': self.price, 'Количество: ': self.quantity}
    def __str__(self):
        return f'{self.name} стоит {self.price}  за единицу, количество товара на складе {self.quantity}'

    def write(self):
        try:
            unit = input(f'Введите наименование техники: ')
            unit_p = int(input(f'Введите стоимость за единцу: '))
            unit_q = int(input(f'Введите количество товара:  '))
            i = {'Наименование техники: ': unit, 'Стоимость: ': unit_p, 'Количество: ': unit_q}
            self.unit.update(i)
            self.store.append(self.unit)
            print(f'Сейчас введено: {self.store}')
        except:
            return f'Что-то явно пошло не так...'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.store_full.append(self.store)
            print(f'Весь склад: {self.store_full}')
            return f'Введение данных завершено пользователем'
        else:
            return ОfficeEquipment.write(self)

class Printer(ОfficeEquipment):
    def __init__(self, name, price, quantity, number_of_lists):
        super(Printer,self).__init__(name, price, quantity, number_of_lists)
    def go_print(self):
        return f'Принтер будет печатать {self.numb} страниц'

class Scaner(ОfficeEquipment):
    def __init__(self, name, price, quantity, number_of_lists):
        super(Scaner,self).__init__(name, price, quantity, number_of_lists)
    def go_scan(self):
        return f'Сканер будет сканировать {self.numb} страниц'

class Xerox(ОfficeEquipment):
    def __init__(self, name, price, quantity, number_of_lists):
        super(Xerox,self).__init__(name, price, quantity, number_of_lists)
    def go_copy(self):
        return f'Ксерокс будет копировать  {self.numb} страниц'


unit_1 = Printer('QWE', 100, 1, 10)
unit_2 = Scaner('ASD', 50, 2, 10)
unit_3 = Xerox('ZXC', 80, 3, 10)
print(unit_1.write())
print(unit_2.write())
print(unit_3.write())

print(unit_1.go_print())
print(unit_2.go_scan())
print(unit_3.go_copy())
