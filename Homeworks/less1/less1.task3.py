"""
Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369
"""

number = int(input("Enter number"))
a = int(number * 11)
b = int(number * 111)
summa = number + a + b
print(summa)


