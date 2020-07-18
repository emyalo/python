# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height
    def get_coat(self):
        return (self.size/6.5)+0.5
    def get_suit(self):
        return (self.height*2)+0.3
    @property
    def get_full(self):
        return str(f'Суммарный расход ткани составляет '
                   f' {round((self.size/6.5+0.5) + (self.height* 2+0.3), 2)}')

class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.sc = round(self.size / 6.5 + 0.5,2)
    def __str__(self):
        return f'Расход ткани на пальто составляет {self.sc}'

class Suit(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.ss = round(self.height * 2 + 0.3,2)
    def __str__(self):
        return f'Расход ткани на костюм составляет {self.ss}'

coat = Coat(1, 2)
suit = Suit(3, 4)
print(coat)
print(suit)
print(suit.get_full)
print(coat.get_full)
print(coat.get_coat())
print(suit.get_suit())
