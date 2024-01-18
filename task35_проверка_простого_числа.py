"""
Напишите функцию, которая принимает одно число и 
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое 
имеет 2 делителя: 1 и n(само число)

Input: 5
Output: yes
"""

def prime_number(number: int) -> bool:
    if number in range(3):
        return True
    if number % 2 == 0: #проверяем четные числа
        return False
    for i in range(3, number // 2 + 1, 2): #берем до половины, начинаем с 3 идем до половины с шагом 2
        if number % i == 0:
            return False
    return True

print(prime_number(int(input("Введите число: "))))