keyslist = ["умм", "аксим", "иним"]
funclist = [sum, max, min]
funcdict = dict(map(lambda *args: args, keyslist, funclist)) 
print("""Здравствуйте!
Рекомендация вводить запрос по типу:
*Действие в последовательности данных в диапазоне.*
Например:
Максимум в массиве (2, 6, 90, -1, -23, 324, -3124, 5) с 3 элемента по 7.
В противном случае вы можете получить не то, что нужно.
Чтобы выйти из программы напишите 'q.'
Введите ваш запрос:)""")
request = ''
while True:
    request = input()  
    if request == 'q':
        break
    A = list(request)
    if A[-1].isdigit():
        A.append('.')
        print("Фи, предложение без точки :(")
    b, counter = [], 0
    mylen, i = len(A), 0
    while i < mylen:
        if A[i] == '-':
            temp = "-"
            i += 1
        else:
            temp = ""
        while A[i].isdigit():
            temp = temp + A[i]
            i += 1
        if temp:
            b.append(''.join(temp))
        i += 1
    mylen = len(b)
    i = 0
    while i < mylen:
        b[i]=int(b[i])
        i += 1
    begin, end, counter = b.pop(-2)-1, b.pop(-1)-1, len(b)
    bool1 = end>begin and begin>0
    if bool1 and counter>end:
        usesfunc = None
        for key in keyslist:
            if request.find(key) + 1:
                usesfunc = funcdict[key]
        if usesfunc is None:
            print("Ваш запрос некорректный, попробуйте ещё.")
        else:
            counter = end-begin+1
            if counter % counter**0.5 == 0:
                mylen = int(counter**0.5)
                bool2 = False
            else:
                mylen = int(counter**0.5) + 1
                bool2 = True
            mylist = []
            if bool2:
                temp2 = end
                end -= mylen
                while begin < end:
                    mylist.append(b[begin:begin+mylen])
                    begin += mylen
                mylist.append(b[begin:temp2])    
            else:    
                while begin < end:
                    mylist.append(b[begin:begin+mylen])
                    begin += mylen
            temp = []
            for elem in mylist:
                temp.append(usesfunc(elem))
            print(usesfunc(temp))
    else:
        print("Ваш запрос некорректный, попробуйте ещё.")