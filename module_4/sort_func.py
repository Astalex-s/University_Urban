nums = [3, 1, 2, 5, 4, 6, 10, 7, 9, 8]


# Пузырьковая сортировка:
def bubble_sort(lst):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swapped = True
    return lst

# Сортировка выборкой:
def selection_sort(lst):
    for i in range(len(lst)):
        lowest = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[lowest]:
                lowest = j
        lst[i], lst[lowest] = lst[lowest], lst[i]
    return lst

# Перебор вставкой

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = i
        j = i -1
        while lst[j] > key and j >= 0:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j +1] = key
    return lst
