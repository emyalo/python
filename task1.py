# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1=list_1
        self.list_2=list_2

    def __add__(self):
        m = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                m[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in m]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in m]))


list_1=[[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
list_2=[[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
print(f'матрица 1 равна\n{list_1}')
print(f'матрица 2 равна\n{list_1}')
my_matrix = Matrix(list_1, list_2)
print(f'Сумма двух матриц равна \n{my_matrix.__add__()}')