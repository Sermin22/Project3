# Напишите генератор, который принимает на вход два списка и генерирует элементы,
# которые есть в обоих списках
def intersection_generator(list_1, list_2):
    seen = set()
    for item in list_1:
        if item in list_2 and item not in seen:
            seen.add(item)
            yield item
