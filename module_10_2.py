import threading
from time import sleep


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
    def run(self):
        days_cnt = 0
        enemies_cnt = 100
        print(f'{self.name}, на нас напали!')
        while enemies_cnt > 0:
            sleep(1)
            days_cnt += 1
            enemies_cnt -= self.power
            print(f'{self.name} сражается {days_cnt} день(дня)..., осталось {enemies_cnt} воинов.')
        print(f'{self.name} одержал победу спустя {days_cnt} дней(дня)!')

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print('Все битвы закончились!')