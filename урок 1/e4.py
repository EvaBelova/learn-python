# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


while True:
    try:
        number = int(input('Введите номер четверти: '))
    except ValueError:
        print('Некорректный ввод')
    else:
        if number < 1 or number > 4:
            print('Введите номер четверти от 1 до 4')
        else:
            break

if number == 1:
    print('x > 0, y > 0')
elif number == 2:
    print('x < 0, y > 0')
elif number == 3:
    print('x < 0, y < 0')
else:
    print('x > 0, y < 0')