def print_params(a=2, b='string', c=True):
    print(a, b, c)


print_params()
print_params(False,7, [1, 2, 3])
print_params(b=25)
print_params(c=[1, 2, 3])

value_list = [True, 9, 'unknown']
value_dict = {'a': 1, 'b': False, 'c': (3, 2, 1)}
print_params(*value_list)
print_params(**value_dict)

value_list_2 = [1, 'end']
print_params(*value_list_2, 42)