import argparse as arg
parser = arg.ArgumentParser()
parser.add_argument("--number", type=int, help="Является ли число точной степенью 2-ки?", default=None)
args = parser.parse_args()

def is_power_two(number:int)->bool:
    """This function check: number is power of two?"""
    if number > 1:
        while True:
            if number % 2 == 1:
                break
            number //= 2
        if number == 1:
            return True
    elif number < 0:
        print("Не той двойки мы степень проверять должны, ой не той")
    return False

print("Кусь!\nДля проверки напишите число или для выхода -q")
while True:
    request = input()
    if request == "-q":
        break
    if not args.number:
        args.number = eval(request)
    if is_power_two(args.number):
        print("Ваше число в какой-то степени двойка")
    else:
        print("Ваше число не является степенью двойка")
    args.number = None