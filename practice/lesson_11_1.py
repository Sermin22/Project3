def is_even(x):
    return x % 2 == 0

result_filter = list(filter(is_even, range(20)))

print(result_filter)

def double(x):
    return [x, x]

map_double = list(map(double, result_filter))

print(map_double)

from itertools import chain

result_chain = list(chain(*map_double))

print(result_chain)

list_1 = [1, 4, 2, 4]
list_2 = [6, 6, 5, 8, 7]
result_list = list(chain(list_1, list_2))
print(result_list)