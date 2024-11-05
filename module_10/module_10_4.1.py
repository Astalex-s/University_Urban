import time
from threading import Thread, Event


def first_worker():
    print('Первый рабочиц приступил к своей задаче')
    event.wait(timeout=5)  # Будем ожидать, пока событие не произойдёт. Для этого мы вызываем метод «wait(5 секунд)»
    print('Первый рабочий продолжил выполнение задачи')
    time.sleep(5)
    print('Первый рабочий закончил выполнять свою задачу')


def second_worker():
    print('Второй рабочий приступил к своей задаче')
    time.sleep(10)
    print('Второй рабочий закончил выполнение своей задачи')
    event.set()  # Когда нам необходимо поменять флаг, мы вызываем метод «set()»


event = Event()
thread1 = Thread(target=first_worker)
thread2 = Thread(target=second_worker)
thread1.start()
thread2.start()

# print(event.is_set()) - Проверить состояние этого флага мы можем, вызвав метод «is_set()»
