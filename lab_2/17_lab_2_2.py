def junk_file(name, Mb, K=(10,100), L=(3,10)):
    import random
    size, need_size = 0, 1024*1024*Mb
    new_file = open(name, 'w')
    counter_for_description = 0
    while size < need_size:
        counter_of_words = 0
        number_of_words = rand.randint(begin_K, end_K)
        while counter_of_words < number_of_words:
            counter_of_chars = 0
            number_of_chars = rand.randint(begin_L, end_L)
            while counter_of_chars < number_of_chars:
                new_file.write(chr(rand.choice(alphabet_keys)))
                size += 1
                counter_of_chars += 1
            new_file.write(' ')
            counter_of_words += 1
            size += 1
        new_file.write('\n')
        size += 1
        if (size/need_size)*100 > counter_for_description:
            print(counter_for_description, end='\r')
            counter_for_description += 1
    new_file.close()

it_is_doing = True
print("""Введите запрос по образцу:
<имя> <размер в Мб> <диапазон кол-ва строк в строке> <длина слова>
Наппример, *testname.txt 512 (20, 50) (5, 9)*""")
request = input().split()
len_of_request = len(request)
if len_of_request == 6:
    K = (int(request[2][1:-1]), int(request[3][0:-1]))
    L = (int(request[4][1:-1]), int(request[5][0:-1]))
elif len_of_request == 4:
    K = (int(request[2][1:-1]), int(request[3][0:-1]))
    L = (3, 10)
elif len_of_request == 2:
    K = (10, 100)
    L = (3, 10)
else:
    print("Вы ввели данные неккоретно")
    it_is_doing = False
if it_is_doing:
    alphabet_keys = list(range(65, 91)) + list(range(97, 123))
    import random as rand
    Mb = int(request[1])
    begin_K, end_K = K[0], K[1]
    begin_L, end_L = L[0], L[1]
    name = request[0]
    size, need_size = 0, Mb*1024*1024
    junk_file(name, Mb, (begin_K, end_K), (begin_L, end_L))