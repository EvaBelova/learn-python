#Напишите программу вычисления арифметического выражения заданного строкой.
#Используйте операции +, -, /, *. приоритет операций стандартный

#2+2 => 4;


print(eval(input()))


#Переделка
n = input('Введите несколько чисел через пробел: ')
numbers = n.split(' ')
result = sum(map(int, filter(lambda x: numbers.index(x) % 2 == 0, numbers)))
print(result)
