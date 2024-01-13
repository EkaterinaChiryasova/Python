"""
Требуется вывести все целые степени двойки (т.е. числа
вида 2k), не превосходящие числа N
10 -> 1 2 4 8
"""


n = 10
stepen = 0
result = 1
while result < n + 1:
    print(result)
    stepen += 1
    result = 2 ** stepen