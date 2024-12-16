# Исходные данные:
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

# Нужно выписывать из этого списка только положительные числа до тех пор, пока не встретите отрицательное
# или не закончится список (выход за границу).

# Чтобы перебрать список вам понадобиться обращение по индексу, запишите в отдельную переменную начальное значение - 0.
index = 0

# Чтобы не выйти за границу списка, в условии цикла while сравниваем текущий индекс и длину списка (функция len()).
while index < len(my_list):  # индексов всего 0-11, длина(len) 12.
    number = my_list[index]  # число из списка (первое число 42 по индексу 0)

    if number > 0:
        print(number)  # печатаем положительные цифры

    elif number < 0:
        break  # прерываем цикл как только встерим отрицательное число

    index = index + 1  # следующее число (69) - индекс 0+1 в списке
