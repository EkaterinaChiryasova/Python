"""
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1

"""

n = int(input("Введите число оценок: "))
my_list = list()

for i in range(n):
    x = int(input("Введите оценки: "))
    my_list.append(x)

max_n = max(my_list)
min_n = min(my_list)

for i in range(len(my_list)):
    if my_list[i] == max_n:
        my_list[i] == min_n
print(my_list)