it_is_doing = True
print(r"""Введите запрос по образцу:\n"
<имя> <размер в Мб> <диапазон кол-ва строк в строке> <длина слова>\n"
Наппример, *testname.txt 512 (20, 50) (5, 9)*""")
request = input().split()
len_of_request = len(request)
if len_of_request == 6:
    K = (request[2][1], request[3][0])
    L = (request[4][1], request[5][0])
elif len_of_request == 4:
    K = (request[2][1], request[3][0])
    L = (3, 10)
elif len_of_request == 2:
    K = (10, 100)
    L = (3, 10)
else:
    print("Вы ввели данные неккоретно")
    it_is_doing = False
if it_is_doing:
    Mb = request[1]
    name = request[0]
    new_file = open(name, "wb")
    size = 0
    need_size = Mb*1024*8
    while size != need_size:
        pass
        size += 1
    new_file.close()