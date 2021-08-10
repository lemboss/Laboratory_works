# Разработать программное средство, реализующее алгоритм детерминизации автомата-распознавателя

import pandas as pd

# входные данные 
S = pd.DataFrame({
                    'vertex' : ['s0', 's1', 's2'],
                    '0' : [['s1', 's2'], ['s1', 's2'], ['s1', 's2']], 
                    '1' : [[None], ['s0', 's2'], ['s2']]
                })
print(S)

# s0 - начальное состояние
# s1, s2 - заключительные состояния

def fill_vertex(S):
    """Найти состояния детерминированного автомата"""
    
    vertex = dict()
    
    # первое состояние равно множеству начальных состояний исходного автомата
    vertex[f'p{len(vertex)}'] = [S['vertex'][0]] 
    
    # создаем 3 служебные перменные
    i = 0
    flag = True
    temp = list()

    # добавляем маршруты в список, чтобы определить: из каких состояний s состоит p
    while i < len(S['vertex']):
        
        # проверка на пустой маршрут
        if S['0'][i] != [None]:

            # условие на проверку длины маршрута
            if len(S['0'][i]) == 1:
                temp.append(S['0'][i])
            # проходим по путям 0
            else:
                for v in S['0'][i]:
                    if v not in temp:
                        temp.append(v)
            
            # проверка на уникальность состояний
            for value in vertex.values():
                if value == temp:
                    flag = False
                    break
            if flag == True:
                vertex[f'p{len(vertex)}'] = temp
        
        flag = True
        temp = []
        
        if S['1'][i] != [None]:
            if len(S['0'][i]) == 1:
                temp.append(S['0'][i])
            else:
                for v in S['1'][i]:
                    if v not in temp:
                        temp.append(v)
        
            for value in vertex.values():
                if value == temp:
                    flag = False
                    break
            if flag == True:
                vertex[f'p{len(vertex)}'] = temp
        
        flag = True
        temp = []
        
        i += 1
    return vertex

vertex = fill_vertex(S)
print(vertex)

print(S)

def fill_0(vertex_p, S):
    """"""
    temp = list()
    vertexes_p_0 = list()
    # берем состояния s, которые составляют p
    # берем по одному состояния из множества
    for values in vertex_p.values():      
        for value in values:              
            
            # находим индекс этого состояния из исходного автомата
            i = 0
            # проходим по множеству состояний исходного автомата
            # (1 колонка)
            for vertex_s in S['vertex']: 
                if vertex_s == value:
                    break
                i += 1
            
            # составляем список, который состоит из состояний, в которые попадает состояние
            # (2 колонка)
            for vertexes_s in S['0'][i]:
                if vertexes_s not in temp and vertexes_s != None: 
                    temp.append(vertexes_s)
            
            # если просмотрели все состояния, которые составляют p, то ищем совпадение в 1 колонке 
            # и записываем во 2 колонку
            # иначе просматриваем остальные
            if value == values[-1]:
                for key in vertex_p.keys():
                    if len(temp) == 0:
                        vertexes_p_0.append(None)
                        break
                    if vertex_p[key] == temp:
                        vertexes_p_0.append(key)
                        break
            else:
                continue
                
            temp = []
    return vertexes_p_0

def fill_1(vertex_p, S):
    """"""
    temp = list()
    vertexes_p_1 = list()
    # берем состояния s, которые составляют p
    # берем по одному состояния из множества
    for values in vertex_p.values():      
        for value in values:              
   
            # находим индекс этого состояния из исходного автомата
            i = 0
            # проходим по множеству состояний исходного автомата
            # (1 колонка)
            for vertex_s in S['vertex']: 
                if vertex_s == value:
                    break
                i += 1
            
            # составляем список, который состоит из состояний, в которые попадает состояние
            # (2 колонка)
            for vertexes_s in S['1'][i]:
                if vertexes_s not in temp and vertexes_s != None: 
                    temp.append(vertexes_s)
            
            # если просмотрели все состояния, которые составляют p, то ищем совпадение в 1 колонке 
            # и записываем во 2 колонку
            # иначе просматриваем остальные
            if value == values[-1]:
                for key in vertex_p.keys():
                    if len(temp) == 0:
                        vertexes_p_1.append(None)
                        break
                    if vertex_p[key] == temp:
                        vertexes_p_1.append(key)
                        break
            else:
                continue
                
            temp = []
    return vertexes_p_1

def to_determine(S):
    """"""
    vertex = fill_vertex(S)
    zeros = fill_0(vertex, S)
    ones = fill_1(vertex, S)
    vertex_p = list()
    for p in vertex.keys():
        vertex_p.append(p)
    return pd.DataFrame({'vertex' : vertex_p,
                         '0' : zeros,
                         '1' : ones
                        })

P = to_determine(S)
print(P)

vertex_p = list()
for p in vertex.keys():
    vertex_p.append(p)
print(vertex_p)

def character_string(P):
    """Проверить, допускает ли автомат цепочку символов"""
    num = input('Введите цепочку:\n')
    i = 0
    for sym in num:
        if P[sym][i] not in vertex_p or P[sym][i] == None:
            return 'Автомат цепочку не допускает'
        for j in range(len(vertex_p)):
            if P[sym][i] == vertex_p[j]:
                i = j
                break
    return 'Автомат цепочку допускает'

print(character_string(P))