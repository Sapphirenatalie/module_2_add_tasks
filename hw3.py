# Дан список, состоящий из 50 элементов, определить сколько из них кратны 41
# и больше среднего арифметического наибольшего и наименьшего значений списка.
# Для поиска максимального и минимальных значений использовать сортировку и индексы

import random

list_of_numbers = random.sample(range(40, 300000), 50)


def func_():
    lst0 = sorted(list_of_numbers)
    min_ = lst0[0]
    max_ = lst0[-1]
    sum_min_max = min_ + max_
    avg_ = sum_min_max / len(list_of_numbers)

    lst1 = []
    for i in list_of_numbers:
        if i % 41 == 0:
            lst1.append(i)

    lst2 = []
    for j in lst1:
        if j > avg_ and j != 0:
            lst2.append(j)
    print("числа, кратные 41 и больше среднего арифметического наибольшего "
          "и наименьшего значений в сгенерированном списке : ", *sorted(lst2))
    print("всего чисел: ", len(lst2))


func_()
