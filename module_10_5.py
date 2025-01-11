from multiprocessing import Pool
import time

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while line := file.readline():
            all_data.append(line)
    print(name, ' обработка завершена.')

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()

    for f_name in filenames:
        read_info(f_name)

    end_time = time.time()
    print(end_time - start_time, '(линейный)')

    # Многопроцессный
    start_time = time.time()

    with Pool(len(filenames)) as p:
        p.map(read_info, filenames)

    end_time = time.time()
    print(end_time - start_time, '(многопроцессный)')