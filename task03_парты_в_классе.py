"""
В школе 3 математических класса решили оборудовать
новыми партами. За каждой партой может сидеть 2 ученика.
Известно кол-во учеников в каждом из 3 классов. Выведите наименьшее число
парт, которые нужно приобрести для них.
"""

class1 = int(input("Количество учеников в первом классе: "))
class2 = int(input("Количество учеников во втором классе: "))
class3 = int(input("Количество учеников в третьем классе: "))

total1 = (class1 + 1)//2
total2 = (class2 + 1)//2
total3 = (class3 + 1)//2

print(f"Нам понадобится приобрести {total1 + total2 + total3} парты")