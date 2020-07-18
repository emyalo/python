# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
# инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы
# методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
# деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
# округление значения до целого числа.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.

class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)
    def __str__(self):
        return f'{self.quantity * "*"}'
    def __add__(self, other):
        return f'Результат сложения {Cell(self.quantity + other.quantity)}'
    def __sub__(self, other):
        if (self.quantity - other.quantity) > 0:
            return f'Результат вычитания {Cell(self.quantity - other.quantity)}'
        else:
            return f'Результат вычитания отрицательный'
    def __mul__(self, other):
        return f'Результат умножения {Cell(int(self.quantity * other.quantity))}'
    def __truediv__(self, other):
        return f'Результат деления {Cell(round(self.quantity // other.quantity))}'
    def make_order(self, cells_row):
        row = ''
        for i in range(int(self.quantity / cells_row)):
            row += f'{"*" * cells_row} \\n '
        row += f'{"*" * (self.quantity % cells_row)}'
        return row


cells1 = Cell(10)
cells2 = Cell(5)

print(cells1)
print(cells2)
print(cells1 + cells2)
print(cells1 - cells2)
print(cells2 - cells1)
print(cells1*cells2)
print(cells1 / cells2)
print(cells2.make_order(3))
print(cells1.make_order(2))
