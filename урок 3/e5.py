# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример: - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

fib1 = fib2 = fib1_negative = 1
fib2_negative = -1
n = int(input())

res = [fib2_negative, fib1_negative, 0, fib1, fib2]

for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    res.append(fib2)
    fib1_negative, fib2_negative = fib2_negative, fib1_negative - fib2_negative
    res = [fib2_negative] + res

print(res)
