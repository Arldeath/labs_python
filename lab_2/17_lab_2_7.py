def leo_numbers(countt:int, templist=[1,1])->int:
    """This function work with list of leonardo numrers"""
    if countt < 0:
        print("Первый аргумент этой функции - натуральное число")
    elif not (countt or countt-1):
        return 1
    elif countt < len(L):
        return L[countt]
    else:
        while len(L) <= countt:
            L.append(L[-1]+L[-2]+1)
        return L[-1]

L = [1, 1]
while True:
    print("Введите номер числа Леонардо или -q:")
    request = input()
    if request == "-q":
        break
    number = leo_numbers(int(request), L)
    print(number)