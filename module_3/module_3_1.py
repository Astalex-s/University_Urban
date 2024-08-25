calls = 0


def count_calls():  # функция счетчик
    global calls
    calls += 1
    return calls


def string_info(string):  # Преобразуем строку в число знаков, верхний и нижний регистры, добавляем в кортеж
    string = (len(string), string.upper(), string.lower())
    count_calls()
    return string


print(string_info("capybara"))
print(string_info('Armageddon'))


def is_contains(string, list_to_search):  # Проверяем наличие строки в списке, предварительно преобразовав и строку и
                                          # список в нижний регистра
    i = 0
    while i < len(list_to_search):
        string_ = list_to_search[i]
        string_ = string_.lower()
        list_to_search[i] = string_
        i += 1
    result = string.lower() in list_to_search
    count_calls()
    return result


print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)
