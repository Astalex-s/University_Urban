def custom_write(file_name, strings: list):
    strings_positions = {}
    num_string = 0
    file = open(file_name, 'w', encoding='utf-8')
    for text in strings:
        num_string += 1
        tell = file.tell()
        file.write(f'{text}\n')
        strings_positions[num_string, tell] = text
    file.close()
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
