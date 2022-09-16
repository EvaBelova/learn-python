# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.


from random import randint

n = int(input('Введите N: '))
a = [randint(-n, n) for _ in range(n)]
positions = []
with open('file.txt') as f:
    for line in f:
        positions.append(int(line.strip()))

result = 1
for position in positions:
    result = result * a[position - 1]

print('Иcходный массив: ', a)
print('Позиции: ', positions)
print('Результат: ', result)
