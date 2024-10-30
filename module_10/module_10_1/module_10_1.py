import datetime
import threading
from time import sleep


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')
    return write_words


# Получение текущего времени перед запуском потоков
start_time = datetime.datetime.now()
# Запуск функций
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
# Получение текущего времени окончания работы функций
end_time = datetime.datetime.now()
# Вывод результата времени работы функций
print(f'Работа потоков {(end_time - start_time)}')

# Получение текущего времени перед запуском потоков
start_time = datetime.datetime.now()

# Создание 4-х потоков
threads = list()
threads.append(threading.Thread(target=write_words, args=(10, 'example5.txt')))
threads.append(threading.Thread(target=write_words, args=(30, 'example6.txt')))
threads.append(threading.Thread(target=write_words, args=(200, 'example7.txt')))
threads.append(threading.Thread(target=write_words, args=(100, 'example8.txt')))

# Запуск потоков
for thread in threads:
    thread.start()

# Ожидание завершения потоков
for thread in threads:
    thread.join()
# Получение текущего времени после завершения потоков
end_time = datetime.datetime.now()

# Вывод результата времени работы потоков
print(f'Работа потоков {(end_time - start_time)}')
