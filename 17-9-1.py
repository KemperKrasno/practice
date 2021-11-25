array_of_numbers = input("Введите строку чисел, через пробел:")
number = input("Введите любое число:")
list_of_numbers = [int(i) for i in array_of_numbers.split(" ")]
number = int(number)
poz = None

def bubble(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle - 1] < element <= array[middle]:
        global poz
        poz = middle - 1
    if array[middle] == element:  # если элемент в середине,
        poz = middle
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

bubble(list_of_numbers)
array_right = len(list_of_numbers)-1
if number < list_of_numbers[0]:
    print("Число не находится внутри строки")
elif number > list_of_numbers[len(list_of_numbers)-1]:
    print("Число не находится внутри строки")
else:
    binary_search(list_of_numbers, number, 0, array_right)
print("Номер позиции элемента, который меньше введенного числа, а следующий за ним больше или равен этому числу(нумерация начинается с ноля):")
print(poz)
print("Отсортированная строка чисел:")
print(list_of_numbers)
print("Введеное число:")
print(number)

