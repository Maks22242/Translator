#словарь операций
O = {
    '+':1,
    '-':2,
    '*':3,
    '/':4,
    '^':5,
    '<': 6,
    '>': 7,
    '==':8,
    '!=':9,
    '<=':10,
    '>=':11,
    '=': 12,
    '<-': 12
}
# Cужебные слова
W = {
    'print': 1,
    'cat': 2,
    'if': 3,
    'else':4,
    'while': 5,
    'length': 6,
    'sin': 7,
    'cos': 8,
    'tan': 9,
    'max': 10,
    'min': 11,
    'exp': 12,
    'log': 13,
    'range': 14,
    'round': 15,
    'break': 16,
    'function':17,
}
# Разделители
R = {
    ';':1,
    ')':2,
    "(":3,
    '\n':4, # Конец строки
    ' ': 5, # пробел
    '#': 6, # пробел
    '[': 7,
    ']':8
}
# Идентификаторы - динамическая
I = {

}
# Константы числа - динамическая
N = {

}
# Константы символы - динамическая
C = {

}


#Ключ по значению
def get_key(map, value):
    for k, v in map.items():
        if v == value:
            return k

def in_map_N(el):
    if (el in N.keys()):  # Проверяем есть ли наша цифра в словаре
        number = "N" + str(N[el])
    else:
        if (len(N) == 0):
            N[el] = 1
            number = "N1"
        else:
            new_val = max(N.values()) + 1
            N[el] = new_val
            number = "N" + str(new_val)
    return number

def in_map_I(el):
    if el in W.keys():
        number = "W" + str(W[el])
    elif el in I.keys():
        number = "I" + str(I[el])
    else:
        if(len(I) == 0):
            I[el] = 1
            number = "I1"
        else:
            new_val = max(I.values()) + 1
            I[el] = new_val
            number = "I" + str(new_val)
    return number

def loc_C(in_str,iter):
    el = in_str[iter]
    iter+=1
    while not(in_str[iter]=="\"" or in_str[iter]=="\'") :
        new_el = in_str[iter]
        el += str(new_el)
        iter += 1
    el += in_str[iter]
    iter+=1
    return el,iter

def in_map_C(el):
    if (el in C.keys()):  # Проверяем есть ли наша цифра в словаре
        number = "C" + str(C[el])
    else:
        if (len(C) == 0):
            C[el] = 1
            number = "C1"
        else:
            new_val = max(C.values()) + 1
            C[el] = new_val
            number = "C" + str(new_val)
    return number

def analyzer(arr_str_in):
    str_out = []
    new_str = ""
    el = ""
    const = 0
    ind = 0
    con_str = 0
    for in_str in arr_str_in:
        iter = 0
        while (iter < len(in_str)):
            if in_str[iter].isdigit() and const == 0 and ind == 0 :  #Начинаем записывать циыру
                const = 1
                el += in_str[iter]
                iter += 1

            elif in_str[iter].isdigit() and const == 1 and ind == 0 :  # Продолжаем записывать цифру
                el += in_str[iter]
                iter += 1

            elif const == 1 and (in_str[iter:iter+2] == 'e-'or in_str[iter:iter+2] == 'e+'): # случай, когда встречаем е+ и у- записи числа
                el += in_str[iter:iter+2]
                iter += 2

                # Случай, когда встречаем е или "." при записи числа
            elif const == 1 and (in_str[iter] == '.' or in_str[iter] == 'e' ):
                el += in_str[iter]
                iter += 1

                # Встретив разделитетель при записи цифры заносим её в словарь
            elif not in_str[iter].isdigit() and const == 1 and in_str[iter] in R.keys():
                new_str += in_map_N(el)
                #Записав число, обнуляем значения и записываем разделитель
                el_R = R[in_str[iter]]
                new_str += "R"+str(el_R)
                el = ""
                const = 0
                ind = 0
                iter += 1

                # Встретив двухсимвольный оператор при записи цифры заносим её в словарь
            elif not in_str[iter].isdigit() and const == 1 and in_str[iter]+in_str[iter+1] in O.keys():
                new_str += in_map_N(el)
                #Записав число, обнуляем значения и записываем разделитель
                el_O = O[in_str[iter:iter+2]]
                new_str += "O"+str(el_O)
                el = ""
                const = 0
                ind = 0
                iter += 2

                # Встретив односимвольный оператор при записи цифры заносим её в словарь
            elif not in_str[iter].isdigit() and const == 1 and in_str[iter] in O.keys():
                new_str += in_map_N(el)
                #Записав число, обнуляем значения и записываем разделитель
                el_O = O[in_str[iter]]
                new_str += "O"+str(el_O)
                el = ""
                const = 0
                ind = 0
                iter += 1

            elif not in_str[iter].isdigit() and const == 1 and not (in_str[iter] in R.keys()) and not (in_str[iter] in O.keys()) and not in_str[iter:iter+2] in O.keys() : #если мы встретили букву, то выведим ошибку
                print("Лексический анализ  с цифрой")
                break

            #Индетефикатор
            # Если первый встретившийся нам символ являеься строковым, то начинаем запись индетефикатора
            elif in_str[iter].isalpha() and const == 0 and ind == 0 and not in_str[iter] in R.keys() and not (in_str[iter] in O.keys()) and not in_str[iter:iter+2] in O.keys():
                ind = 1
                el += in_str[iter]
                iter += 1

            elif ind == 1 and not in_str[iter] in R.keys() and not (in_str[iter] in O.keys()) and not in_str[iter:iter+2] in O.keys():
                el += in_str[iter]
                iter += 1

                # При записи индетефикатора и встрече разделителя запоминаем элемент
            elif ind == 1 and in_str[iter] in R.keys():
                new_str += in_map_I(el)
                el_R = R[in_str[iter]]
                new_str += "R" + str(el_R)                              
                el = ""
                const = 0
                ind = 0
                iter += 1

                # При записи индетефикатора и встрече двухсимвольного оператора и запоминаем элемент
            elif ind == 1 and in_str[iter:iter + 2] in O.keys():
                new_str += in_map_I(el)
                el_O = O[in_str[iter:iter + 2]]
                new_str += "O" + str(el_O)
                el = ""
                const = 0
                ind = 0
                iter += 2

                # При записи индетефикатора и встрече одиночного оператора и запоминаем элемент
            elif ind == 1 and in_str[iter] in O.keys():
                new_str += in_map_I(el)
                el_O = O[in_str[iter]]
                new_str += "O" + str(el_O)
                el = ""
                const = 0
                ind = 0
                iter += 1

                #Коммит
            elif in_str[iter] == '#':
                el_R = R[in_str[iter]]
                new_str += "R" + str(el_R)
                iter = len(in_str)-1
                el_R = R[in_str[iter]]
                new_str += "R" + str(el_R)
                iter+=1

            #Символьная константа
            elif in_str[iter]=="\"" or in_str[iter] == "\'" : #если мы встеритили ковычки, запишим символьну константу
                el, iter = loc_C(in_str,iter)
                new_str += in_map_C(el)
                el = ''
                iter+=1
             # Встретили двойную операцию типа ==
            elif in_str[iter:iter + 2] in O.keys():
                el_O = O[in_str[iter:iter + 2]]
                new_str += "O" + str(el_O)
                iter+=2

            # Встретили одиночную операцию
            elif in_str[iter] in O.keys():
                el_O = O[in_str[iter]]
                new_str += "O"+str(el_O)
                iter+=1

                # Запишим разделитель
            elif in_str[iter] in R.keys():
                el_R = R[in_str[iter]]
                new_str += "R" + str(el_R)
                iter+=1

        str_out.append(new_str)
        new_str = ""
        print("Proverka")

    return str_out

def prog():
    f_in = open('input.txt', 'r')
    str_in = f_in.readlines()
    print(str_in)
    str_out = analyzer(str_in)
    print("N: ",N,"\nI: ",I,"\nC: ",C )
    print(str_out)
    f_in.close()

prog()
