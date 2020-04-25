import argparse as arg
parser = arg.ArgumentParser()
parser.add_argument("--way", type=str, help="Имя/Путь файла для сортировки", default=None)
args = parser.parse_args()

def MergeSort(text:list)->None:
    """This function sorted something"""
    if len(text) > 1:
        half = len(text)//2
        left_part = text[:half]
        right_part = text[half:]
        MergeSort(left_part)
        MergeSort(right_part)
        i = 0
        kley = text[:]
        while i < len(text):
            my_min = min(kley)
            text[i]=my_min
            del kley[kley.index(my_min)]
            i+=1

if not args.way:
    print("Введите путь к файлу ")
    way = input()
else:
    way = args.way
new_way = ''.join(way.split('\\')[:-1]) + "out_file"
file = open(way, 'r', encoding="utf-8")
new_file = open(new_way, 'w', encoding="utf-8")
for line in file:
    temp_line = line.split(' ')
    MergeSort(temp_line)
    new_file.write(' '.join(temp_line)+'\n')