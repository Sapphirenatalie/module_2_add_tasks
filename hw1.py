# Вводится число с клавиатуры N,
# необходимо вывести квадраты всех четных чисел в промежутке от 1 до N включительно.

print('Без использования функции')
n = int(input('Введите число: '))
for i in range(1, n+1):
    if i % 2 == 0:
        print(f'{i}^{2} = {i ** 2}')
    continue

print('С функцией')
num_ = (int(input('Введите число: ')))


def func_sq(num_):

    for j in range(1, num_ + 1):
        if j % 2 == 0:
            print(f'{j}^{2} = {j ** 2}')
    return num_


func_sq(num_)
