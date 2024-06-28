#игрок и компьютер управляют героями с различными характеристиками.
# Игра состоит из раундов, в каждом раунде игроки по очереди наносят урон друг другу,
# пока у одного из героев не закончится здоровье.
#Требования:
#1. Используйте ООП (Объектно-Ориентированное Программирование) для создания классов героев.
#2. Игра должна быть реализована как консольное приложение.
#Классы:
#Класс `Hero`:
# Атрибуты:
#- Имя (`name`)
#- Здоровье (`health`), начальное значение 100
#- Сила удара (`attack_power`), начальное значение 20
#- Методы:
#- `attack(other)`: атакует другого героя (`other`), отнимая здоровье в размере своей силы удара
#- `is_alive()`: возвращает `True`, если здоровье героя больше 0, иначе `False`
#Класс `Game`:
#- Атрибуты:
#- Игрок (`player`), экземпляр класса `Hero`
#- Компьютер (`computer`), экземпляр класса `Hero`
#- Методы:
#- `start()`: начинает игру, чередует ходы игрока и компьютера,
#пока один из героев не умрет. Выводит информацию о каждом ходе
#(кто атаковал и сколько здоровья осталось у противника) и объявляет победителя.

import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self):
        self.player = Hero('Боец')
        self.computer = Hero('Противник')

    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            # Player's turn
            self.player.attack(self.computer)
            print(f"{self.player.name} атака {self.computer.name}. {self.computer.name}'здоровье: {self.computer.health}")
            if not self.computer.is_alive():
                print(f"{self.computer.name} побежден! {self.player.name} Победил!")
                break

            # Computer's turn
            self.computer.attack(self.player)
            print(f"{self.computer.name} атака {self.player.name}. {self.player.name}'здоровье: {self.player.health}")
            if not self.player.is_alive():
                print(f"{self.player.name} побежден! {self.computer.name} победил!")
                break

if __name__ == "__main__":
    game = Game()
    game.start()