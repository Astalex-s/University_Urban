import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            else:
                all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Высчитываем время затраченное на при линейном вызове функции read_info():

# start_time = datetime.datetime.now()
# for filename in filenames:
#     read_info(filename)
# end_time = datetime.datetime.now()
# print(f'{end_time - start_time} (линейный)')

# Высчитываем время затраченное на при многопроцессорном вызове функции read_info():

if __name__ == '__main__':
    start_time = datetime.datetime.now()
    with Pool() as pool:
        result = pool.map(read_info, filenames)
    end_time = datetime.datetime.now()
    print(f'{end_time - start_time} (многопроцессный)')
