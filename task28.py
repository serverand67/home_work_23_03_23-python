
"""
Задача 28: Напишите рекурсивную функцию sum(a, b), 
возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются 
только +1 и -1. Также нельзя использовать циклы. 
*Пример:*

2 2
    4 
"""
# вариант 1

# функция нахождения суммы двух чисел
def NumbersSum(numberA, numberB): # функция принимает два числа
    if (numberA == 0):                   # проверка если = 0
        return numberB                   # возвращаем число В
    if (numberB == 0):                   # проверка если = 0
        return numberA                   # возвращаем число А
    if (numberA != 0 and numberB != 0):  # проверка если числа не = 0                               
        return NumbersSum(numberA-1, numberB+1)
    
    
numberA = int(input("Введите число A: "))
numberB = int(input("Введите число B: "))
result = NumbersSum(numberA, numberB) # вызываем функцию
print(f"Сумма чила {numberA} и {numberB} равна: {result}")