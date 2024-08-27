def print_params(a=1, b="strings", c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1,2,3])


values_list = [2, 'string', True]
values_dict = {'a': 5, 'b': True, 'c': 'string'}


print_params(*values_list)
print_params(**values_dict)


values_list_2 = [3.3, False]
print_params(*values_list_2, 42)
