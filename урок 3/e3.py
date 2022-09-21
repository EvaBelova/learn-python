#Задайте список из вещественных чисел.
#Напишите программу,которая найдёт разницу между
#максимальным и минимальным значением дробной части элементов.
#Пример:- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

l = [1.1, 1.2, 3.1, 5, 10.01]
new_l = []

for num in l:
    if not isinstance(num, int):
        new_l.append(num - int(num))

min_num = min(new_l)
max_num = max(new_l)

print("min", min_num)
print("max", max_num)
print("difference", round(max_num - min_num, 10))
