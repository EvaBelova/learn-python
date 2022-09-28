#Дана последовательность чисел.
#Получить список уникальных элементов заданной последовательности
# [1, 5, 2, 3, 5, 1, 5, 5, 3, 10] => [2, 10]

num = [1, 5, 2, 3, 5, 1, 5, 5, 3, 10]
res = []
for i in num:
    if num.count(i) == 1:
        res.append(i)
print(res)


#переделка

numbers = [1, 5, 2, 3, 5, 1, 5, 5, 3, 10]
result = list(filter(lambda x: numbers.count(x) == 1, numbers))
print(result)