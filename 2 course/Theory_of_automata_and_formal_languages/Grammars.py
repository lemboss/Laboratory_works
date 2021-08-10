# 1. Составить грамматику, порождающую формальный язык
# 2. Определить тип формальной грамматики и языка по классификации Хомского
# 3. Разработать программное средство, распознающее тип введенной пользователем грамматики по классификации Хомского

T=list(input('Введите терминалы:\n'))   
N=list(input('Введите нетерминалы\n'))
print("\nАлфавит терминалов:\n", T)
print("\nАлфавит нетерминалов:\n", N)

list1 = T
list2 = T
list3 = []
while len(list3) <= 10:
    list2 = [i + j for i in list2 for j in list1]
    list3 = list1 + list2
    list2 = list3   

list4 = N
list5 = N
list6 = []
while len(list5) <= 10:
    list5 = [i + j for i in list6 for j in list4]
    list6 = list4 + list5
    list5 = list6  
print("\nТерминалы:\n", list3)
print("\nНетерминалы:\n", list6)

R=[list3[i] + list6[j] for i in range(10) for j in range(10)]
for i in list3:
    R.append(i)
L=[list6[i] + list3[j] for i in range(10) for j in range(10)] 
for i in list3:
    L.append(i)
print(R)
print(L)

P=[]
n=int(input('Количество правил?\n'))
for i in range(n):
    a=[]
    l=input('\nЛевая часть правила:\n')  
    a.append(l)
    rn=int(input('\nСколько правых частей правила?\n'))
    for j in range(rn):
        r=input('\nПравая часть правила:\n')
        a.append(r)
    P.append(a)   
print(P)

def res(T,N,P,R,L):
    tip=''
    for i in range(len(P)):
        if P[i][0] not in T:
            break
        else:
            flag=False
            for i in range(len(P)):
                for j in range(len(P[i])):
                    if P[i][j] not in R or L:
                        flag=True
                        break
            if flag == False:
                tip='тип 3'
                return tip
    if tip!='':
        return tip
    else:
        flag=False
        for i in range(len(P)):
            if P[i][0] not in T:
                flag=True
                break
        if flag == False:
            tip = 'тип 2'
            return tip
    
    if tip!='':
        return tip
    else:
        for i in range(len(P)):
            for j in range(1,len(P[i])):
                if len(P[i][0])>len(P[i][j]):
                    tip = 'тип 0'
                    return tip
        tip = 'тип 1'
        return tip
    
    
    if tip!='':
        return tip
    
print(res(T,N,P,R,L))

