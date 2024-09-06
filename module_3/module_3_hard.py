

def calculate_structure_sum(data_structure):
    counter = 0
    if isinstance(data_structure, (list, set, tuple)):
        for i in data_structure:
            counter += calculate_structure_sum(i)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            counter += calculate_structure_sum(key)
            counter += calculate_structure_sum(value)
    elif isinstance(data_structure, str):
        counter += calculate_structure_sum(len(data_structure))
    elif isinstance(data_structure, int):
        counter += data_structure

    return counter


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate_structure_sum(data_structure)
print(result)
