def custom_write(file_name, strings: list):
    strings_positions = {}
    num_string = 0
    for text in strings:
        file = open(file_name, 'a', encoding='utf-8')
        num_string += 1
        tell = file.tell()
        file.write(f'{text}\n')
        file.close()
        strings_positions[num_string, tell] = text
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
