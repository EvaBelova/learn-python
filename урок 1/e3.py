# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример: - x=34; y=-30 -> 4, - x=2; y=4-> 1, - x=-34; y=-30 -> 3


while True:
    try:
        x = float(input('Введите x: '))
        y = float(input('Введите y: '))
    except ValueError:
        print('Введен неверный символ')
    else:
        if x == 0 or y == 0:
            print('X и Y не могут быть равными 0')
        else:
            break

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)