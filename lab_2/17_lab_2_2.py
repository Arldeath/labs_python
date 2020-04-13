alphabet_keys = list(range(65, 91)) + list(range(97, 123))
import argparse as arg
parser = arg.ArgumentParser()
parser.add_argument("name", type=str, help="Имя мусорного файла")
parser.add_argument("Mb", type=int, help="Его размер в Мб")
parser.add_argument('K', nargs=2, type=int, default=[10, 100])
parser.add_argument('L', nargs=2, type=int, default=[3, 10])
args = parser.parse_args()
map(tuple, [args.K, args.L])
import random as rand

def junk_file(name:"str", Mb:"int", K:"tuple"=(10,100), L:"tuple"=(3,10))->None:
    size, need_size = 0, 1024*1024*Mb
    new_file = open(name, 'w')
    counter_for_description = 0
    begin_K, end_K = K[0], K[1]
    begin_L, end_L = L[0], L[1]
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

junk_file(args.name, args.Mb, args.K, args.L)