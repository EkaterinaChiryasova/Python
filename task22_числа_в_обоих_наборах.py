"""
Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12
"""

var1 = '11 6' 
var2 = '2 4 6 8 10 12 10 8 6 4 2' 
var3 = '3 6 9 12 15 18' 

new_var = set(map(int, var2.split()))
new_var2 = set(map(int, var3.split()))
new_var3 = sorted(new_var.intersection(new_var2))
for i in new_var3:
    print(i, end=' ')