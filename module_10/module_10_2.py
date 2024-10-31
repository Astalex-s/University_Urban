import threading
from time import sleep


class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.number_of_enemies = 100
        self.number_of_days = 0

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.number_of_enemies:
            self.number_of_days += 1
            if self.number_of_enemies > 0:
                self.number_of_enemies -= self.power
                print(f'{self.name} сражается {self.number_of_days} день(дня)..., '
                      f'осталось {self.number_of_enemies} воинов.')
                sleep(1)
        print(f'{self.name} одержал победу спустя {self.number_of_days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
