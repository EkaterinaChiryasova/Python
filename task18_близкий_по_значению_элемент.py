"""
Требуется найти в массиве list_1 самый близкий по 
значению элемент к заданному числу k и вывести его.
Считать, что такой элемент может быть только один. 
Если значение k совпадает с этим элементом - выведите его.
list_1 = [1, 2, 3, 4, 5]
k = 6
# 5

"""

n = int(input('Введите количество элементов в массиве: '))
list = []

for i in range(n):
    list.append(int(input('Введите элемент массива: ')))
print(list)

x = int(input('Введите число: '))

k = 0 #сюда положим индекс элемента массива, с которым у Х наименьшая разница
minDiff = abs(x - list[0]) #сюда положим минимальную разницу между числом Х и элементом массива, предположим, что мин разница с первым элементом

for i in range(n):
    if abs(x - list[i]) <= minDiff:
        minDiff = abs(x - list[i])
        k = i
print(list[k])

i = 0
min_num = abs(list[0] - k)
index = 0
while i < len(list):
    if abs(list[i] - k) < min_num:
        min_num = abs(list[i] - k)
        index = i
    i += 1
print(list[index])