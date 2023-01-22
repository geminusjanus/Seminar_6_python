# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр

num = float(input('Enter floating point number: '))
number = sum(int(i) for i in str(num) if i.isdigit())
print(number)