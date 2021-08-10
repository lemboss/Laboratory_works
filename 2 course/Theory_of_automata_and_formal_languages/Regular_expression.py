# Разработать регулярное выражение для указанной цепочки символов
# Произвольная цепочка символов a, b и с, заканчивающаяся символом "!" или "сс"
# (a + b + c)*   !/cc

# создадим алфавит
syms = list('abc')
print('Алфавит:', syms)

syms1 = syms
syms2 = syms
syms3 = []
# создадим (a + b + c)* до 20 элемента 
while len(syms3) <= 20:       
        syms2 = [i + j for i in syms2 for j in syms1]
        syms3 = syms1 + syms2
        syms2 = syms3
        
# добавим к итерации завершающий символ
end = input('Введите последний символ ')
for i in range(len(syms3)):
    syms3[i] = syms3[i] + end
    
print(*syms3)