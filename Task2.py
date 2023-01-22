# Задайте натуральное число N. Напишите
# программу которая составит список простых множителей числа N
# Старый код
# num = int(input('Enter number N= '))
# i = 2 
# list = []
# num2 = num
# while i <= num:
#     if num % i == 0:
#         list.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {num2} приведены в списке: {list}")


n = int(input('Enter simple number: '))

list = list(filter(lambda x:all(x % y != 0 for y in range(2, x)), range(2, 13)))

print(list)