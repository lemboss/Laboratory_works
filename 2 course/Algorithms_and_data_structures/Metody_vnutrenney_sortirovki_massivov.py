import numpy as np
import random
import pandas as pd

def start(a):
    print('0 - не использовать начальную сортировку\n1 - полность отсортировать массив\n2 - отсортировать массив в обратном порядке\n3 - отсортировать частично')
    word = input()
    if word == '0':
        return a
    elif word == '1':
        return sorted(a)
    elif word == '2':
        return a[::-1]
    elif word == '3':
        print('1 - отсортировать 25%\n2 - отсортировать 50%\n3 - отсортировать 75%')
        word = input()
        if word == '1':
            return sorted(a[:int(len(a)*0.25)])
        elif word == '2':
            return sorted(a[:int(len(a)*0.5)])
        elif word == '3':
            return sorted(a[:int(len(a)*0.75)])


def inclusion_sort(a):
    """
    Сортировка с помощью прямого включения
    """
    ar = start(a)

    iteration, swap, compare = 0, 0, 0

    # Для всех элементов кроме начального
    for i in range(1, len(ar)):
        x = ar[i]  # запоминаем значение элемента
        j = i - 1  # и его индекс
        # смещаем другие элементы к концу массива пока они меньше индекса
        while x < ar[j - 1] and j > 0:
            ar[j] = ar[j - 1]
            swap += 1
            j -= 1  # смещаем просмотр к началу массива
            iteration += 1
            compare += 1
        ar[j] = x  # рассматриваемый элемент помещаем на освободившееся место
        iteration += 1
    return [ar, iteration, swap, compare, iteration + swap + compare]


def selection_sort(a):
    """
    Сортировка с помощью прямого выбора
    """
    ar = start(a)

    iteration, swap, compare = 0, 0, 0

    # для всех элементов
    for i in range(len(ar) - 1):
        min_ = i  # запоминаем индекс текущего элемента

        # ищем минимальный элемент чтобы поместить на место i-ого
        # для остальных элементов после i-ого
        for j in range(i + 1, len(ar)):
            if ar[j] < ar[min_]:  # если элемент меньше минимального,
                min_ = j  # запоминаем его индекс в min_
                compare += 1
            iteration += 1
        ar[i], ar[min_] = ar[min_], ar[i]  # меняем местами i-ый и минимальный элементы
        swap += 1
        iteration += 1
    return [ar, iteration, swap, compare, iteration + swap + compare]


def bubble_sort(a):
    """
    Сортировка с помощью прямого обмена
    """
    ar = start(a)

    iteration, swap, compare = 0, 0, 0

    # для всех элементов
    for i in range(len(ar) - 1):

        # для всех элементов после i-ого
        for j in range(len(ar) - 1, i, -1):

            # если текущий элемент меньше предыдущего
            if ar[j - 1] > ar[j]:
                compare += 1

                # меняем их местами
                ar[j - 1], ar[j] = ar[j], ar[j - 1]
                swap += 1

            iteration += 1
    return [ar, iteration, swap, compare, iteration + swap + compare]


def quick_sort(array, left, right, iteration=0, swap=0, compare=0, d=0):
    """
    Метод быстрой сортировки
    """

    if d == 0:
        ar = start(array)
    else:
        ar = array

    i, j = left, right  # левая и правая границы
    x = ar[(left + right) // 2]  # средний элемент

    # пока границы не сомкнутся
    while i < j:

        # сдвигаем левую границу пока элемент [i] меньше x
        while ar[i] < x:
            i += 1
            iteration += 1

        # сдвигаем правую границу пока элемент [j] больше x
        while ar[j] > x:
            j -= 1
            iteration += 1

        if i <= j:

            if ar[i] > ar[j]:
                ar[i], ar[j] = ar[j], ar[i]
                swap += 1
                compare += 1

            i += 1
            j -= 1
            compare += 1

        iteration += 1

    # рекурсивно вызываем сортировку для левой и правой части массива
    if (left < j):
        compare += 1
        quick_sort(ar, left, j, iteration, swap, compare, d + 1)
    if (i < right):
        compare += 1
        quick_sort(ar, i, right, iteration, swap, compare, d + 1)

    return [ar, iteration, swap, compare, iteration + swap + compare]


def zadanie1():
    """Сравнить эффективность прямых методов сортировки (число итераций, сравнений и обменов) для
числовых массивов, содержащих различное число элементов (20, 500, 1000, 3000, 5000, 10000), выбираемых
случайным образом. Для 20 элементов предусмотреть ввод с клавиатуры. Оценить время сортировки, построить
соответствующие таблицы."""
    size_ar = random.choice((20, 500, 1000, 3000, 5000, 10000))
    print(f"Массив состоит из {size_ar} элементов")
    if size_ar == 20:
        print('Если хотите заполнить массив самостоятельно, напишите "1", иначе Enter')
        elem = input()
        if elem == '1':
            ar = []
            for i in range(20):
                elem = int(input(f'Введите {i + 1} элемент: '))
                ar.append(elem)
        else:
            ar = [np.random.randint(-10, 10) for _ in range(size_ar)]
            print(f'Массив {ar}')
    else:
        ar = [np.random.randint(-10, 10) for _ in range(size_ar)]

    print('надо написать 0')
    i_sort = inclusion_sort(ar)
    print('надо написать 0')
    s_sort = selection_sort(ar)
    print('надо написать 0')
    b_sort = bubble_sort(ar)
    df = pd.DataFrame({'прямое включение': [i_sort[1], i_sort[2], i_sort[3], i_sort[4]],
                       'прямой выбор': [s_sort[1], s_sort[2], s_sort[3], s_sort[4]],
                       'прямой обмен': [b_sort[1], b_sort[2], b_sort[3], b_sort[4]]
                       },
                      index=['Итераций', 'Обменов', 'Сравнений', 'Операций всего'])
    return df


def zadanie2():
    """Исследовать влияние начальной упорядоченности массива (уже отсортированный, отсортированный в
обратном порядке, частично отсортированный – при разных размерах отсортированной части 25%, 50% и 75%)."""

    ar = [np.random.randint(-10, 10) for _ in range(1000)]

    print('надо написать 1')
    full_sorted = bubble_sort(ar)[4]

    print('надо написать 2')
    reversed_ = bubble_sort(ar)

    print('надо написать 3 потом 1')
    one_quarter_sorted = bubble_sort(ar)

    print('надо написать 3 потом 2')
    half_sorted = bubble_sort(ar)

    print('надо написать 3 потом 3')
    three_quarters_sorted = bubble_sort(ar)

    df = pd.DataFrame({'100% sorted': [full_sorted],
                       '25% sorted': [one_quarter_sorted[4]],
                       '50% sorted': [half_sorted[4]],
                       '75% sorted': [three_quarters_sorted[4]],
                       'Reversed': [reversed_[4]]
                       },
                      index=['Операций'])
    return df


def zadanie3():
    """Сравнить эффективность быстрой сортировки и прямых методов. Определить размеры массивов, когда
прямые методы эффективнее. Составить таблицы, иллюстрирующие сделанные выводы."""
    i_sort = []
    q_sort = []
    for size in (500, 10000):
        ar = [np.random.randint(-10, 10) for _ in range(size)]
        print("надо написать 0")
        i_sort.append(inclusion_sort(ar)[4])
        print("надо написать 0")
        q_sort.append(quick_sort(ar, 0, len(ar) - 1)[4])
    df = pd.DataFrame({
        'прямое включение': i_sort,
        'быстрая сортировка': q_sort
    },
        index=['500 элементов', '10000 элементов'])

    return df

def main():
    while True:
        print("Выберите номер задания:\n1 - сравнить эффективность прямых методов сортировки\n2 - Исследовать влияние начальной упорядоченности массива\n3 - сравнить эффективность быстрой сортировки и прямых методов\nend - чтобы закончить")
        param = input()
        if param == '1':
            print(zadanie1())
        elif param == '2':
            print(zadanie2())
        elif param == '3':
            print(zadanie3())
        elif param == 'end':
            break
        else:
            continue
            
if __name__ == '__main__':
    main()