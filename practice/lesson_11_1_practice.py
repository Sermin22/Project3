# Напишите генератор, который принимает на вход последовательность чисел
# и генерирует квадраты этих чисел
def square_generator(nums):
    for num in nums:
        yield num ** 2

list_nums = list(range(1, 10))
i = square_generator(list_nums)
print(next(i))
print(next(i))
print(next(i))

# Напишите генератор, который генерирует случайные числа в заданном диапазоне
import random

def random_number_generator(start, stop):
    while True:
        yield random.randint(start, stop)

random_number = random_number_generator(2, 12)
print(next(random_number))
print(next(random_number))
print(next(random_number))

# Напишите генератор, который генерирует последовательность чисел по заданной формуле
def func(a):
    return a + 5

def sequence_generator(start, formula):
    num = start
    while True:
        yield num
        num = formula(num)

sequence = sequence_generator(2, func)
print(next(sequence))
print(next(sequence))

# Напишите генератор, который принимает на вход два списка и генерирует элементы,
# которые есть в обоих списках

list_1 = [1, 5, 4, 3, 8]
list_2 = [5, 2, 6, 3]
def intersection_generator(lst1, lst2):
    seen = set()
    for item in list_1:
        if item in list_2 and item not in seen:
            seen.add(item)
            yield item

items = intersection_generator(list_1, list_2)
print(next(items))
print(next(items))

# Напишите генератор, который принимает на вход размерность квадратной матрицы и
# генерирует числа по спирали, начиная с центрального элемента.
def spiral_generator(n):
    matrix = [[0] * n for i in range(n)]
    x, y = n//2, n//2
    matrix[y][x] = 1
    yield matrix[y][x]

    for i in range(2, n*n+1):
        if x == y or (x < y and x + y < n-1) or (x > y and x + y >= n):
            dx, dy = 0, -1
        else:
            dx, dy = -1, 0
        x, y = x+dx, y+dy
        matrix[y][x] = i
        yield matrix[y][x]
# Эта задача больше на логику построения шагов.
# # Чтобы понять функцию нужно изучить:
# 	• матрицы в программировании
# 	• генераторы
# после ситуация станет более ясна.

# изучить можно по ссылке https://sky.pro/wiki/python/rabota-s-matricami-v-python-rukovodstvo-dlya-nachinayushih/
