"""
Дана последовательность из N целых чисел и число 
K. Необходимо сдвинуть всю последовательность 
(сдвиг - циклический) на K элементов вправо, K – 
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
"""

# list = [1, 2, 3, 4, 5]
# list2 = []
# shift = 3
# for i in range(len(list)):
#     list2.append(list[(i + shift) % len(list)])
# print(list2)

list = [1, 2, 3, 4, 5]
shift = 3
list2 = list[shift:] + list[:shift]
print(list2)