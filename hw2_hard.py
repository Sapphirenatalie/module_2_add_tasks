# Дан несортированный список, заполненный случайными положительными числами,
# выводить корни тех элементов, которые больше среднего арифметического чисел кратных 5.
# Список должен состоять из 10 000 элементов, поэтому придумать оптимизацию,
# чтобы не проходить весь список, если возможно.
#
# *Подсказка: может понадобиться random.randint(), continue, break

from math import sqrt
import random
import time

start = time.time()

list_of_numbers = [random.randint(5, 500) for i in range(10000)]
sort_list_of_numbers = sorted(list_of_numbers)
rev_list_of_numbers = sort_list_of_numbers[::-1]


def special_func():
    list_1 = []

    for i in rev_list_of_numbers:
        if i % 5 == 0 and i not in list_1:
            list_1.append(i)

    list_2 = []
    for j in list_1:
        avg = sum(list_1) / len(list_1)
        if j > avg:
            list_2.append(j)
        else:
            break

    n = 0
    for k in list_2:
        n += 1

        print(f'{n} √ {k} -->> {round(sqrt(k), 2)}')

    print('всего ', n)


special_func()

finish = time.time()
res = (finish - start) * 1000

print('Время работы в миллисекундах: ', res)
