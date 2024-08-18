# Список (grades) содержит списки оценок для каждого ученика в алфавитном порядке:
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Множество (students) содержит неупорядоченную последовательность имён всех учеников в классе:
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

''' 
ЗАДАЧА: Необходимо составить словарь, используя grades и students,
где ключом будет имя ученика, а значением - его средний балл 
'''
# Создадим пустой словарь "Средний балл":
average_score = {}

# Преобразуем множество (students) в список и упорядочим список учеников в алфавитном порядке:
students = sorted(students)

''' 
Добавим в словарь (average_score) в виде ключа (key) студентов из списка, взяв их индексы
по порядку с 0 из списка студентов (students) и добавив к нему значения (value), взяв их
индексы по порядку с 0 из списка оценок учеников (grades), предварительно узнав количество
студентов в списке: 
'''
quantity_student = len(students)

''' 
Так как мы еще не проходили циклы))), воспроизведем добавление каждого клиента в словарь отдельной
строкой кода, округлив значение средней оценки до 2 знаков после запятой: 
'''
average_score[students[0]] = round(sum(grades[0]) / len(grades[0]), 2)
average_score[students[1]] = round(sum(grades[1]) / len(grades[1]), 2)
average_score[students[2]] = round(sum(grades[2]) / len(grades[2]), 2)
average_score[students[3]] = round(sum(grades[3]) / len(grades[3]), 2)
average_score[students[4]] = round(sum(grades[4]) / len(grades[4]), 2)

print("Всего учеников в списке:", quantity_student)
print(average_score)
