import random
import pandas as pd
import matplotlib.pyplot as plt

def ary(n):
    """
    Задать массив
    """
    return [random.randint(0,100) for _ in range(n)]

def linearSearch(array, x):
    """
    Линейный поиск
    """
    
    time = 0
    i = 0
    
    # последовательно движемся по массиву, пока не найден нужный элемент
    while i < len(array) and array[i] != x:
        i += 1
        time += 3
    
    # если требуемого значения не существует, возвращаем -1
    if i == len(array):
        return [-1, time]
    
    # иначе возвращаем индекс требуемого значения
    return [i, time]

def barierSearch(a, x):
    """
    Поиск с барьером
    """
    
    # добавляем в конец списка требуемое значение
    array = [num for num in a]
    array.append(x)
    
    time = 0
    i = 0
    
    # двигаемся по массиву, пока требуемое значение не будет найдено
    while array[i] != x:
        i += 1
        time += 2
        
    # если уткнулись в барьер, возвращаем -1
    if i == len(array)-1:
        return [-1, time]
    # иначе возвращаем индекс требуемого значения 
    return [i, time]

def binarySearch(a, x):
    """
    Бинарный поиск
    """
    
    # сортируем массив
    array = sorted([num for num in a])
    
    # устанавливаем границы поиска
    L = 0
    R = len(array) - 1
    
    # первым элементом проверяем тот, что в середине
    m = L + (R - L)//2
    time = 0
    
    # пока левая граница не превысила правую и значение не найдено, двигаемся слева направо по массиву
    while L < R and array[m] != x: 
        
        # если требуемое значение меньше элемента посередине
        if x < array[m]:
            
            # то смещаем правую границу поиска до проверяемого элемента
            R = m - 1
            time += 1
            
        # если требуемое значение больше элемента посередине
        else:
            
            # то смещаем левую границу поиска до проверяемого элемента
            L = m + 1
            time +=1
            
        # обновляем центральный индекс
        m = L + (R - L)//2
        
        time += 3
    
    # если требуемое значение найдено, то возвращаем его индекс
    if array[m] == x:
        return [m, time]
    # иначе возвращаем -1
    return [-1, time]

def zadanie1():
    """
    Сравнить время выполнения линейного поиска в массиве случайных чисел a(n) при n = 100, 500, 1000, 3000, 10000
    """

    time = []
    nums = (100, 500, 1000, 3000, 10000)
    for num in nums:
        for i in range(3):
            time.append(linearSearch(ary(num), 19)[1])
    
    df = pd.DataFrame({'100 элементов': [time[0], time[1], time[2]],
                       '500 элементов': [time[3], time[4], time[5]],
                       '1000 элементов': [time[6], time[7], time[8]],
                       '3000 элементов': [time[9], time[10], time[11]],
                       '10000 элементов': [time[12], time[13], time[14]]
                      }, 
                      index = ['первый опыт', 'второй опыт', 'третий опыт'])
    return df

def zadanie2():
    """
    Сравнение времени поиска и количества повторений цикла при линейном и двоичном
    поиске в предварительно отсортированном массиве
    """
    
    
    value = 5000
    
    array = sorted(ary(value))
    array1 = array
    array2 = array
    
    time_linear = linearSearch(array1, 19)[1] # время поиска в линейном поиске
    time_binary = binarySearch(array2, 19)[1] # время поиска в бинарном поиске
    
    # рисуем столбчатую гистограмму
    index = ['time_linear', 'time_binary']
    values = [time_linear, time_binary]
    plt.bar(index, values)
    plt.show()
    print(f'Время линейного поиска: {time_linear}' + '\n' + f'Время бинарного поиска: {time_binary}')

def zadanie3():
    """
    Исследование эффективности введения «барьера» при линейном поиске
    """
    
    value = 5000
    
    array = ary(value)
    array1 = array
    array2 = array
    
    time_linear = linearSearch(ary(value), 19)[1]  # время поиска в линейном поиске
    time_barier = barierSearch(ary(value), 19)[1]  # время поиска с барьером
    
    # рисуем столбчатую диаграмму
    index = ['time_linear', 'time_barier']
    values = [time_linear, time_barier]
    plt.bar(index, values)
    plt.show()
    print(f'Время линейного поиска: {time_linear}' + '\n' + f'Время бинарного поиска: {time_barier}')

def main():
    print("1 - первое задание\n2 - второе задание\n3 - третье задание\n0 - выйти")
    while True:
        w = input()
        if w == '1':
            print(zadanie1())
        if w == '2':
            print(zadanie2())
        if w == '3':
            print(zadanie3())
        if w == '0':
            break

if __name__ == '__main__':
    main()