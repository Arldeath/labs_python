it_is_doing = True
print(r"""Введите запрос по образцу:\n"
<имя> <размер в Мб> <диапазон кол-ва строк в строке> <длина слова>\n"
Наппример, *testname.txt 512 (20, 50) (5, 9)*""")
request = input().split()
len_of_request = len(request)
if len_of_request == 6:
    K = (int(request[2][1]), int(request[3][0]))
    L = (int(request[4][1]), int(request[5][0]))
elif len_of_request == 4:
    K = (int(request[2][1]), int(request[3][0]))
    L = (3, 10)
elif len_of_request == 2:
    K = (10, 100)
    L = (3, 10)
else:
    print("Вы ввели данные неккоретно")
    it_is_doing = False
if it_is_doing:
    import random as rand
    Mb = int(request[1])
    begin_K, end_K = K[0], K[1]
    begin_L, end_L = L[0], L[1]
    name = request[0]
    new_file = open(name, "w")
    size = 0
    need_size = Mb*1024*8
    counter_for_description = 0
    while size < need_size:
        counter_of_words = 0
        number_of_words = rand.randint(begin_K, end_K)
        while counter_of_words < number_of_words:
            counter_of_chars = 0
            number_of_chars = rand.randint(begin_L, end_L)
            while counter_of_chars < number_of_chars:
                new_file.write(chr(rand.randint(33, 127)))
                size += 1
                counter_of_chars += 1
            new_file.write(' ')
            counter_of_words += 1
            size += 1
        new_file.write('\n')
        size += 1
        if (size/need_size)*100 > counter_for_description:
            #print(counter_for_description, end='\r')
            print(counter_for_description, end='\r')
            counter_for_description += 1
    new_file.close()