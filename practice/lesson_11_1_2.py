list_numbers = list(range(1, 101))
print(list_numbers)

result = [x for x in list_numbers if x % 3 ==0 or x % 5 == 0]
print(result)

result_2 = (x*x for x in range(1, 100) if x % 2 == 0)
print(result_2)
print(sum(result_2))

xs = range(10)
def print6(xs):
    for x, s in enumerate(xs):
        print(s)
        if x == 5:
            break

#print(print6(xs))

i = (x * x for x in range(10))
print(print6(i))
print(print6(i))

my_list = [1, 2, 3]
my_iter = iter(my_list)  # Преобразуем список в итератор
print(next(my_iter))  # Вывод: 1
print(next(my_iter))  # Вывод: 2
print(next(my_iter))  # Вывод: 3

print(*(x for x in "Hello World!" if x.isupper()))

squares = (x * x for x in range(5))
print(list(squares))
print(list(squares))

# Напишите генераторное выражение, которое возвращает кубы четных чисел от 0 до 10
cube = (x ** 3 for x in range(11) if x % 2 == 0)
print(*cube)
print(list(cube))
print(list(cube))

# Напишите функцию, которая принимает список чисел и возвращает сумму квадратов положительных
# чисел в этом списке. Используйте для этого генераторное выражение
def sum_square(list_numbers):
    return sum(x**2 for x in list_numbers if x > 0)

# Напишите генераторное выражение, которое возвращает буквы строки # "hello"#,
# но только если они являются гласными
classroom = (letter for letter in "hello" if letter in "AEIOUYaeiouy")
print(*classroom)

# Найдите среднее арифметическое всех чисел, кратных 3 или 5, в заданном диапазоне
numbers = range(1, 101)
filtered_numbers = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, numbers))
average = sum(filtered_numbers) / len(filtered_numbers)
print(average)

# Объедините несколько списков в один список, учитывая возможные дубликаты элементов
from itertools import chain

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [5, 6, 7, 8]
combined_list = list(set(chain(list1, list2, list3)))
print(combined_list)

# Дан список словарей. Отфильтруйте его по ключу age и значению 30
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 30},
    {"name": "Eve", "age": 25},
]
# мое решение
filter_people_age_30 = [age for age in people if age["age"] == 30]
print(filter_people_age_30)
# из лекции
filter_people = list(filter(lambda x: x["age"] == 30, people))
print(filter_people)

result_lambda = list(chain(*map(lambda x: [x, x], (filter(lambda x: x % 2 == 0, range(20))))))
print(result_lambda)

# Генераторная функция — это функция, использующая ключевое слово yield
def yield_start(start=1):
    while True:
        yield start
        start += 1

numb = yield_start()
print(next(numb))
print(next(numb))
print(next(numb))

