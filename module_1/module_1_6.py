# Словари
my_dict = {"Aleksey": 1980, "Mihail": 1987}

print(my_dict)
print(my_dict.get("Aleksey"))
print(my_dict.get("Anatoliy"))

my_dict.update({
                "Maksim": 1983,
                "Svetlana": 1976
                })
my_dict.pop("Aleksey")
print(my_dict)

# Множества
my_set = {2, 2, 2.0, "Aleksey", True, "Mihail", "Aleksey", False, False}
print(my_set)
my_set.add(3.0)
my_set.add("Sergey")
my_set.discard("Mihail")
print(my_set)
my_set.remove(True)
print(my_set)
