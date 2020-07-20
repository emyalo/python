# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class DivZero:
    def __init__(self, nom, denom):
        self.nom = nom
        self.denom = denom

    @staticmethod
    def div_zero(nom, denom):
        try:
            return (nom / denom)
        except:
            return (f'Нельзя делить на ноль! Это не предел')


print(DivZero.div_zero(1, 0))
print(DivZero.div_zero(1, 2))
