immutable_var = (1, 2.0, 'String', True)

print('Immutable tuple:', immutable_var)

# Объект «кортеж» не поддерживает назначение элементов, он является неизменяемой коллекцией.
# Был закомментирован для возможности продолжения домашнего задания)
# immutable_var[0] = 2
# print(immutable_var)

mutable_list = [1, 2.0, 'String', True]

print('Mutable list:', mutable_list)

mutable_list[1] = 'Aleksey'
print('Mutable list is mutable:', mutable_list)
