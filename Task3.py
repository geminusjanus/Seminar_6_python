# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
# Старый код
# num = float(input("Enter floating point number: "))

# def sumDigits(num):
#     sum = 0
#     for i in str(num):
#         if i != ".":
#             sum += int(i)
#     return sum

# print(f"Сумма цифр = {sumDigits(num)}")

num = float(input('Enter floating point number: '))
number = sum(int(i) for i in str(num) if i.isdigit())
print(number)