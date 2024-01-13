"""
Найдите сумму цифр трехзначного числа n.
n = 123 -> res = 6 (1 + 2 + 3)
n = 100 -> res = 1 (1 + 0 + 0)
"""

number = int(input("Введите трехзначное число: "))
result = number // 100 + number // 10 % 10 + number % 10

print(result)