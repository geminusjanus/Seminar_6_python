# Задайте натуральное число N. Напишите
# программу которая составит список простых множителей числа N


n = int(input('Enter simple number: '))

list = list(filter(lambda x:all(x % y != 0 for y in range(2, x)), range(2, 13)))

print(list)