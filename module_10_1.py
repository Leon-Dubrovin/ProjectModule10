import time
from time import sleep
import threading
def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for n in range(word_count):
            file.write(f'Какое-то слово № {n + 1}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}.')

start_time = time.time()

args1 = ((10, 'example1.txt'),
        (30, 'example2.txt'),
        (200, 'example3.txt'),
        (100, 'example4.txt'),
        )

for argi in args1:
    wite_words(*argi)

end_time = time.time()
execution_time = end_time - start_time
print(f"Работа потоков: {execution_time}")

start_time = time.time()

args2 = ((10, 'example5.txt'),
        (30, 'example6.txt'),
        (200, 'example7.txt'),
        (100, 'example8.txt'),
        )
threads = [threading.Thread(target=wite_words, args=argi) for argi in args2]

for thr in threads:
    thr.start()
for thr in threads:
    thr.join()

end_time = time.time()
execution_time = end_time - start_time
print(f"Работа потоков: {execution_time}")