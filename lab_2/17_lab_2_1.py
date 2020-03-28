keyslist = [
    ["Сумм", "сумм"],
    ["Максим", "максим"],
    ["Миним", "миним"]]
funclist = [sum, max, min]
print("""Здравствуйте
Рекомендация вводить запрос по типу:
*Действие в последовательности данных в диапазоне*
Например:
Максимум в массиве (2, 6, 90, -1, -23, 324, -3124, 5) с 3 элемента по 7.
В противном случае вы можете получить не то, что нужно.
Чтобы выйти из программы напишите 'q'
Введите ваш запрос:)""")
request = ''
while True:
    request = input()  
    if request == 'q':
        break
    A = list(request)
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
    counter = len(b)
    print(b, counter)        