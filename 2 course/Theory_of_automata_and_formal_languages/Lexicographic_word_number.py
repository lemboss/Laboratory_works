# Разработать программное средство, реализующее алгоритм получения лексикографического номера слова

Error = 'error'

def count_sym():
    """Возвращает целое число"""
    try:
        n = int(input('Введите целое число: '))
        return n
    except ValueError:
        return Error

#получаем количество букв в алфавите
while True:
    n = count_sym()
    if n != Error and n > 1:
        break

def sym_of_alph1():
    """Возвращает символы алфавита для номера"""
    new_sym = []
    sym = input(f'Введите {n} уникальных символов алфавита: ')
    
    # проверяем одинаковые буквы
    for s in sym:
        if s not in new_sym:
            new_sym.append(s)
    
    # формируем словарь, если длина введен символов совпадает с n
    if len(new_sym) == n:
        sym_alph = {}
        
        for num, value in enumerate(new_sym):
            sym_alph[value] = num+1
            
        return sym_alph
    
    else:
        return Error

#получаем словарь символов
while True:
    sym1 = sym_of_alph1()
    if sym1 != Error:
        break
print(sym1)

def read_word():
    """Возвращает слово"""
    
    word = input('Введите слово: ')
    
    for w in word:
        
        if w not in sym1.keys():
            return Error
        
    return word

#получаем слово
while True:
    
    word = read_word()
    
    if word != Error:
        break
print(word)

# количество букв в слове
k = len(word)

def num_of_word(word, n, k):
    """Возвращает лексико-графический номер слова"""
    
    num_word = []
    
    for w in word:
        k -= 1
        j = sym1[w]
        num_word.append(n**k * j)
        
    return sum(num_word)

#получаем лексико-графический номер слова
res = num_of_word(word, n, k)
print('Лексико-графический номер слова =', res)

def sym_of_alph2():
    """Возвращает символы алфавита для слова"""
    
    new_sym = []
    sym = sym1
    
    for s in sym:
        
        if s not in new_sym:
            new_sym.append(s)
            
    if len(new_sym) == n:
        return new_sym
    
    else:
        return Error

while True:
    sym2 = sym_of_alph2() 
    if sym2 != Error:
        break

def word():
    """Возвращает слово по номеру"""
    while True:
        N = count_sym()
        if N != Error:
            break
    if N == 0:
        return 'Пустое множество'
    
    list1 = sym2
    list3 = []
    list2 = sym2
    while len(list3) <= N:       
        list2 = [i + j for i in list2 for j in list1]
        list3 = list1 + list2
        list2 = list3      
        
    return list3[N-1]

# получаем слово по введенному с клавиатуры числу
res2 = word()
print('Слово, введенное пользователем, равняется числу', res2)