"""
Требуется вычислить, сколько раз встречается 
некоторое число k в списке list_1.
Найдите количество и выведите его.
list_1 = [1, 2, 3, 4, 5]
k = 3
# 1

"""

list_1 = [1, 2, 3, 4, 5]
k = 3
count = 0 
for i in list_1: 
    if i == k: count += 1 
print(count)