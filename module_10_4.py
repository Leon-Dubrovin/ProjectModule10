import threading
from random import randint
from time import sleep
from queue import Queue
class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        sleep(randint(3, 10))

class Cafe:
    def __init__(self, *tables:Table):
        self.queue = Queue()
        self.tables = tables
        self.count_occupied_tables = 0
    def guest_arrival(self, *guests:Guest):
        for gst in guests:
            guest_at_table = False
            for tbl in self.tables:
                if tbl.guest is None:
                    tbl.guest = gst
                    guest_at_table = True
                    self.count_occupied_tables += 1
                    gst.start()
                    print(f'{gst.name} сел(-а) за стол номер {tbl.number}')
                    break
            if not guest_at_table:
                self.queue.put(gst)
                print(f'{gst.name} в очереди')
    def discuss_guests(self):
        while not self.queue.empty() or self.count_occupied_tables > 0:
            for tbl in self.tables:
                if tbl.guest is not None:
                    if not tbl.guest.is_alive():
                        print(f'{tbl.guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {tbl.number} свободен')
                        if not self.queue.empty():
                            tbl.guest = self.queue.get()
                            print(f'{tbl.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {tbl.number}')
                            tbl.guest.start()
                        else:
                            tbl.guest = None
                            self.count_occupied_tables -= 1

if __name__ == '__main__':
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()