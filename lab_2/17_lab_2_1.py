list_of_keys = ["умм", "аксим", "иним"]
funcdict = {"умм": sum, "аксим": max, "иним": min}
print(r"""Здравствуйте!
Если вы хотите ввести данные с файла, то пропишите -f <путь>,
Например *-f e:\git-repository\labs_python\lab_2\test.txt*.
Рекомендация вводить запрос по типу:
*Действие в последовательности данных в диапазоне от до*.
Например, *Максимум в массиве (2, 6, 90, -1, -23, 324, -3124, 5) с 3 элемента по 7.*
В противном случае вы можете получить не то, что нужно.
Чтобы выйти из программы напишите *-q*.
Введите ваш запрос:)""")
while True:
    request = input()
    if request == "-q":
        break  
    if request[:2] == "-f":
        way = request[3:]
        request = open(way,"rb").read().decode("utf-8")
    request_into_char = list(request)
    if request_into_char[-1].isdigit():
        request_into_char.append('.')
        print("Фи, предложение без точки :(")
    list_of_numbers = []
    len_of_request, i = len(request_into_char), 0
    while i < len_of_request:
        if request_into_char[i] == '-':
            temp_str = '-'
            i += 1
        else:
            temp_str = ''
        while request_into_char[i].isdigit():
            temp_str = temp_str + request_into_char[i]
            i += 1
        if temp_str:
            list_of_numbers.append(''.join(temp_str))
        i += 1
    len_of_list = len(list_of_numbers)
    i = 0
    while i < len_of_list:
        list_of_numbers[i]=int(list_of_numbers[i])
        i += 1
    end, begin = list_of_numbers.pop(-1)-1, list_of_numbers.pop(-1)-1
    len_of_list = len(list_of_numbers) 
    correct_borders = end>begin and begin>0
    if correct_borders and len_of_list>end:
        usesfunc = None
        for key in list_of_keys:
            if request.find(key) + 1:
                usesfunc = funcdict[key]
        if usesfunc is None:
            print("Ваш запрос некорректный, попробуйте ещё.")
        else:
            len_of_realrange = end-begin+1
            if len_of_realrange % len_of_realrange**0.5 == 0:
                rangelen = int(len_of_realrange**0.5)
                sqrt_is_int = False
            else:
                rangelen = int(len_of_realrange**0.5) + 1
                sqrt_is_int = True
            realrange = []
            if sqrt_is_int:
                rangeend = end
                end -= rangelen
                while begin < end:
                    realrange.append(list_of_numbers[begin:begin+rangelen])
                    begin += rangelen
                realrange.append(list_of_numbers[begin:rangeend])    
            else:    
                while begin < end:
                    realrange.append(list_of_numbers[begin:begin+rangelen])
                    begin += rangelen
            list_of_temp_result = []
            for elem in realrange:
                list_of_temp_result.append(usesfunc(elem))
            print("Ваше число "+str(usesfunc(list_of_temp_result))+'.')
    else:
        print("Ваш запрос некорректный, попробуйте ещё.")
    print("Введите ваш запрос:")