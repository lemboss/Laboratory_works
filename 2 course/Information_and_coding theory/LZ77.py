import numpy as np

def encode(buffer_length, dictionary_length, string):
    """LZ77 coder"""

    ans = '' #строка, в которой будет закодированная часть
    buffer = string[:buffer_length] #буфер с размером buffer_length
    dictionary = np.zeros(dictionary_length, dtype=str) #словарь с размером dictionary_length
    pos = buffer_length #переменная, с которой начинается проход по входной строке
    start_fill = 0
    #пока не просмотрит всю входную строку или буфер не станет пустым
    while pos < len(string) or buffer != '':
        
        #если нет такого символа в словаре
        if buffer[0] not in dictionary:
            offset = 0  # смещение 0
            length = 0  # длина совпадения 0

            #формируем словарь
            for i in range(1, len(dictionary)):
                dictionary[i-1] = dictionary[i]
            dictionary[-1] = buffer[0]

            #формируем буфер
            if pos+1 >= len(string):
                buffer = buffer[1:]
            else:
                buffer = buffer[1:] + string[pos]

            pos += 1

            ans += str(offset)+str(length)+dictionary[-1]

        #если символ совпадает
        else:
            
            #рассчитываем смещение относительно начала словаря
            offset=np.nonzero(dictionary==buffer[0])[0][0]

            #находим количество совпадений (length)
            if len(dictionary) < len(buffer):
                for i in range(1, len(dictionary)):
                    if offset>=dictionary_length-1:
                        length = 1
                        break
                    if len(buffer) == 1:
                        length = 0
                        break
                    if dictionary[offset+i] != buffer[i]:
                        length = i
                        break
            else:
                for i in range(1, buffer_length):
                    if offset>=dictionary_length-1:
                        length = 1
                        break
                    if len(buffer) == 1:
                        length = 0
                        break
                    if dictionary[offset+i] != buffer[i]:
                        length = i
                        break
            
            #смещаем словарь
            for i in range(1, dictionary_length):
                if i+length >= dictionary_length:
                    if offset == 0 and length == 0:
                        start_fill=i
                    else:
                        start_fill=i-1
                    break
                dictionary[i-1] = dictionary[i+length]       
            for i in range(length+1):
                dictionary[i+start_fill] = buffer[i]


            ans += str(offset)+str(length)+buffer[length]

            #смещаем буфер
            if pos+length+1 >= len(string):
                buffer = buffer[length+1:] + string[pos:]
            else:
                buffer = buffer[length+1:buffer_length] + string[pos:pos+length+1] 

            pos += length+1
    
    return ans
        
def decode(dictionary_length, string):
    """LZ77 декодер"""

    ans = ''        #строка, в которой будет закодированная часть
    dictionary = np.zeros(dictionary_length, dtype=str) #словарь с размером dictionary_length
    syms=''
    start_fill=0
    #цикл по входной строке
    num=0
    while num<len(string):
        j=0
        while num<len(string) and string[num+j].isdigit():
            j+=1
        offset=int(string[num:num+j-1])  #смещение от начала словаря
        length=int(string[num+j-1])   #длина последовательности, которую нужно печатать
        sym=string[num+j]             #последний символ

        for i in range(offset, offset+length):
            syms+=dictionary[i]
        syms+=sym
        ans+=syms

        for i in range(1, dictionary_length+1):
            if i+length >= dictionary_length: 
                start_fill=i-1
                break
            dictionary[i-1]=dictionary[i+length]
        for i in range(length+1):
            dictionary[i+start_fill] = syms[i]
            
        syms=''
        num+=j+1
        
    return ans.replace('zero', '0').replace('one', '1').replace('two', '2').replace('three', '3').replace('four', '4').replace('five', '5').replace('six', '6').replace('seven', '7').replace('eight', '8').replace('nine', '9')

def to_code(file_name, code_file='coded.txt'):
    """
    file_name.txt - файл, который нужно закодировать
    code_file.txt - имя файла, в котором будет закодированный файл
    """
    with open(file_name, 'r', encoding ='utf8') as file:
        with open(code_file, 'w') as coder:
            for line in file:
                coder.write(encode(9, 100, line.replace('0', 'zero').replace('1', 'one').replace('2', 'two').replace('3', 'three').replace('4', 'four').replace('5', 'five').replace('6', 'six').replace('7', 'seven').replace('8', 'eight').replace('9', 'nine')[:-1]))
                coder.write(line[-1])
                
def to_decode(file_name):
    """"""
    with open(file_name, 'r') as coded:
        with open('decoded.txt', 'w', encoding = 'utf8') as decoded:
            
            for line in coded:
                
                if line == '\n':
                    decoded.write('\n')
                else:
                    decoded.write(decode(100, line[:-1]))
                    decoded.write('\n')
                    
def main():
    print("*** LZ77 CODER-DECODER ***") 
    while True:
        print('1 - закодировать файл\n2 - декодировать файл\n0 - выйти\n')
        button = input()
        if button == '1':
            print('Укажите название файла или его полный путь')
            name = input()
            try:
                to_code(name)
                print('Файл успешно закодирован (coded.txt)')
            except FileNotFoundError:
                print('Ошибка!\nФайл не найден. Попробуйте еще раз\n')
        elif button == '2':
            print('Укажите название файла или его полный путь')
            name = input()
            try:
                to_decode(name)
                print('Файл успешно декодирован (decoded.txt)')
            except FileNotFoundError:
                print('Ошибка!\nФайл не найден. Попробуйте еще раз\n')
        elif button == '0':
            print('\nЗавершение работы...')
            break

if __name__ == '__main__':
    main()