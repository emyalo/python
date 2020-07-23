#from os import name, system
from random import choice, randint, sample

class GameCard: #создается карточка игры
    def __init__(self, user_name):
        self.user_name = user_name
        self._card = self._generate_card()
    def print_card(self): #вывод игровой карты
        headline = 2
        print(f'Имя игрока: {self.user_name}'.center(25, '-')) #Позиционирует по центру указанную строку, дополняя её справа и слева до указанной длины указанным символом
        for i, num in enumerate(self._card):
            num = str(num)
            if (i + 1) % 9 != 0:
                print(num.rjust(headline), end='|') #Позиционирует вправо указанную строку, дополняя её слева до указанной длины указанным символом.
            else:
                print(num.rjust(headline))
        print(''.center(25, '-'))

    def _generate_card(self): #генерирование карточки, сделает ее скрытой, чтобы не менять код
        gen = [num for num in range(1, 91)]
        card = []
        for _ in range(3):
            line = sorted(sample(gen, 5))
            for i in line:
                gen.remove(i)
            for _ in range(4):
                line.insert(randint(0, 9), ' ')
            card.extend(line)
        return card

    def player_move(self, move): #вычеркивание числа
        if move in self._card:
            self._card[self._card.index(move)] = '-'

    def is_win(self): #когда игра заканчивается победой
        a = True
        for num in self._card:
            if isinstance(num, int): #isinstance() проверяет принадлежность данных определенному классу (типу данных)
                a = False
        return a

class UserCard(GameCard): #карточка для игрока
    def player_move(self, move):
        answer = input('У вас есть выпавший бочонок? Введите "Y", если да, иначе "N" >>> ').lower()
        if answer == 'y':
            if move in self._card:
                super().player_move(move)
                a = True
            else:
                a = False
                print(f'Бочонка под номером {move} нет на карточке. К сожалению, игра завершена. Вы проиграли.')
        else:
            if move in self._card:
                a = False
                print(f'Бочонок под номером {move} есть на карточке. К сожалению, игра завершена. Вы проиграли.')
            else:
                a = True
        return a

class CompCard(GameCard):#карточка для компа
    pass

class GameLoto:  # сама игра
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer
        self._bag = [num for num in range(1, 91)]
        print('Это игра в "ЛОТО". Перед тобой две карточки, твоя и противника. Внимательно читай, что выпало. Удачи!')

    def start(self): #начало
        while True:
            #self._clear()
            self.player.print_card()
            self.computer.print_card()
            if self.player.is_win() and self.computer.is_win():
                print('Игра завершена. Ничья')
                break
            elif self.player.is_win():
                print(f'Поздравляем! Выиграл игрок {self.player.user_name}')
                break
            elif self.computer.is_win():
                print(f'Выиграл игрок {self.computer.user_name}')
                break
            else:
                new_move = self._number_taken_from_bag()
                print(f'Новый бочонок: {new_move: },', f'(осталось: {len(self._bag): } шт.)')
                user_a = self.player.player_move(new_move)
                self.computer.player_move(new_move)
                if user_a:
                    continue
                else:
                    break

    def _number_taken_from_bag(self):
        try:
            move = choice(self._bag)
            self._bag.remove(move)
        except IndexError:
            print('Игра завершена, бочонков больше нет')
            exit()
        return move

    # def _clear(self): #чистка экрана для os, работает с ошибкой
    #     if name == 'a':
    #         _ = system('clear')

USER_CARD = UserCard(input('Введи свое имя: '))
COMP_CARD = CompCard('AI')
GAME = GameLoto(USER_CARD, COMP_CARD)
GAME.start()