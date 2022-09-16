# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


while True:
    try:
        x = float(input("Введите x: "))
        y = float(input("Введите y: "))
        z = float(input("Введите z: "))
    except:
        print('Вы ввели не то')
    else:
        break

left = not (x or y or z)
right = (not x) and (not y) and (not z)

if left == right:
    print("Истина")
else:
    print("Ложь")