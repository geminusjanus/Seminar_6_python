#Задайте список из нескольких чисел.
# Напишите программу которая найдет сумму элементов
# списка стоящих на нечетной позиции
# Старый код:
# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list_length = len(myList)
# sumOfElements = 0
# for i in range(list_length):
#     if i%2 !=0:
#         sumOfElements += myList[i]
# print('Сумма чисел на нечетных позициях:', sumOfElements)


myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newList = list(filter(lambda x: x%2 == 0, myList))
sum = 0
length = len(newList)
for i in range(length):
    sum += newList[i]
print('Сумма чисел на нечетных позициях:', sum)
