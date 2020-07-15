# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self,speed,color,name, is_police):
        self.speed=speed
        self.color=color
        self.name=name
        self.is_police=is_police

    def go(self):
        return(f'{self.name} поехала.')

    def stop(self):
        return(f'{self.name}  остановилась.')

    def turn_right(self):
        return(f'{self.name} повернул/а направо.')

    def turn_left(self):
        return(f'{self.name} повернул/а налево.')

    def show_speed(self):
        return(f'{self.name} едет со скоростью {self.speed}.')

class TownCar(Car):
    def __init__(self,speed,color,name, is_police):
        super(TownCar, self).__init__(speed,color,name, is_police)

    def show_speed(self):
        if self.speed>60:
            return(f'Скорость превышена. {self.name} едет со скоростью {self.speed}.')
        else:
            return(f'{self.name} едет со скоростью {self.speed}.')

class SportCar(Car):
    def __init__(self,speed,color,name, is_police):
        super(SportCar, self).__init__(speed,color,name, is_police)

class WorkCar(Car):
    def __init__(self,speed,color,name, is_police):
        super(WorkCar, self).__init__(speed,color,name, is_police)

    def show_speed(self):
        if self.speed>40:
            return(f'Скорость превышена. {self.name} едет со скоростью {self.speed}.')
        else:
            return(f'{self.name} едет со скоростью {self.speed}.')

class PoliceCar(Car):
    def __init__(self,speed,color,name, is_police):
        super(PoliceCar, self).__init__(speed,color,name, is_police)


a = SportCar(100, 'красная', 'спортивная машина', False)
b = TownCar(70, 'оранжевая', 'городская машина', False)
c = WorkCar(60, 'желтая', 'рабочая машина', False)
d = PoliceCar(40, 'зеленая',  'полицейская машина', True)


print(a.turn_left())
print(c.go())
print(f'{b.name}  {b.color}')
print(f'{d.name} это машина полиции? {d.is_police}')
print(f'{c.name}  это машина полиции?  {c.is_police}')
print(a.show_speed())
print(b.show_speed())
print(c.show_speed())
