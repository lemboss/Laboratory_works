# Минимизация автомата распознавателя
# Разработать программное средство, реализующее алгоритм минимизации

import pandas as pd

# Входные данные
status = ['q0','q1','s2','s3','q4','q5','s6','s7']
zero_way = ['q1','q5','q1','s2','q1','q5','q5','s3']
one_way = ['q4','s6','s6','s3','q5','s6','s2','s6']

def remove_odd_status(s, z, o):
    """Удалить недостижимые вершины"""
    for v in s:
        if v not in z and v not in o and v != 'q0':
            index = s.index(v)
            st = s[:index] + s[index+1:]
            ze = z[:index] + z[index+1:]
            on = o[:index] + o[index+1:]

    return pd.DataFrame({
                        'status':st,
                        '0':ze,
                        '1':on
                        })

input_data = remove_odd_status(status, zero_way, one_way)

def equals_0(data):
    """Определить группы для 0-эквивалентности"""
    q = []
    s = []
    for status in data['status']:
        if status[0] == 'q':
            q.append(status)
        elif status[0] == 's':
            s.append(status)
    return [q, s]

equal_0 = equals_0(input_data)

def to_minimize(dataframe, groups=equal_0, new_groups=[]):
    """Минимизировать автомат"""
    
    new_groups.append(groups)
    auph = []
    #цикл по группам 0 эквивалентности
    for group in groups:
        #цикл по каждому состоянию из этой группы
        for status in group:
            new_group=[status] #выделяю новую группу

            #ищу номер группы по 0, чтобы потом можно было понять, входят ли вершины в одну группу
            #нахожу саму вершину
            for num, s in enumerate(dataframe['0']):
                if int(status[-1]) == num:
                    stat_0=s
                    break
            #а тут нахожу группы, в которую она входит
            for num, gr in enumerate(groups):
                if stat_0 in gr:
                    number_of_group_by_0=num
                    break

            #ищу номер группы по 1, чтобы потом можно было понять, входят ли вершины в одну группу
            #нахожу саму вершину
            for num, s in enumerate(dataframe['1']):
                if int(status[-1]) == num:
                    stat_1=s
                    break
            #а тут нахожу группы, в которую она входит
            for num, gr in enumerate(groups):
                if stat_1 in gr:
                    number_of_group_by_1=num
                    break
            
            #найти первые соответствия
            temp_0={}
            for num, s in enumerate(dataframe['0']):
                if int(status[-1]) == num:
                    temp_0[f'{status[0]}{status[1]}']=s
                    break

            temp_1={}
            for num, s in enumerate(dataframe['1']):
                if int(status[-1]) == num:
                    temp_1[f'{status[0]}{status[1]}']=s
                    break

            #найти индекс для проверки следующих вершин
            for num in range(len(group)):
                if status[-1] == group[num][-1]:
                    i=num
                    break
            #проход по следуюшим состояниям
            for o_status in range(i+1, len(group)):
                
                #проход по столбцу "0"
                for num, s in enumerate(dataframe['0']):
                    if int(group[o_status][-1]) == num:
                        if s in groups[number_of_group_by_0]:
                            temp_0[f'{group[o_status][0]}{num}']=s
                        break

                #проход по столбцу "1"
                for num, s in enumerate(dataframe['1']):
                    if int(group[o_status][-1]) == num:
                        if s in groups[number_of_group_by_1]:
                            temp_1[f'{group[o_status][0]}{num}']=s
                        break
                
            #создаю группу
            for key in temp_0.keys():
                for key1 in temp_1.keys():
                    if key not in new_group and key == key1:
                        new_group.append(key)
            
            #все вместить в один список
            flag=True
            for gr in auph:
                for item in gr:
                    for aaa in new_group:
                        if aaa == item:
                            flag=False
                            break
            if flag == True:    
                auph.append(new_group)

    if len(new_groups) > 1 and new_groups[-1] == new_groups[-2]:
        new_status=[]
        for a in dataframe['status']:
            if len(a)<1: continue
            for b in new_groups[-1]:
                if a in b: new_status.append(b)
        new_0=[]
        for a in dataframe['0']:
            if len(a)<1: continue
            for b in new_groups[-1]:
                if a in b: new_0.append(b)
        new_1=[]
        for a in dataframe['1']:
            if len(a)<1: continue
            for b in new_groups[-1]:
                if a in b: new_1.append(b)

        print(pd.DataFrame({'status':new_status,'0':new_0,'1':new_1}))
        return [j for _ in new_groups for j in _]
    to_minimize(dataframe, auph, new_groups)

to_minimize(input_data)