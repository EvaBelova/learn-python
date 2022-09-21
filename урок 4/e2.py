#Задайте натуральное число N.
# Напишите программу,
# которая составит список простых множителей числа N.

import math
def primefactors(n):
    while n % 2 == 0:
        print(2),
        n = n / 2

    for i in range(3, int(math.sqrt(n))+1,2):

        while (n % i == 0):
            print(i)
            n = n/i

n = int(input("Введите число n: \n"))
primefactors(n)

#    except:
       # print('Вы ввели не то')
   # else:
    #    break