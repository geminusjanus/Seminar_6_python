# Напишите программу, которая принимает на 
# вход число N и выдает набор произведений 
# чисел от 1 до N.

from functools import reduce
number = int(input('Enter number N: '))
sum = reduce(lambda x, y: x*y, range(1, number+1))
print(sum)

# Старый код
# n = int(input("Enter: "))
# multiplication = 1
#
# for i in range (1, n+1):
#     multiplication*=i
#     print (multiplication)