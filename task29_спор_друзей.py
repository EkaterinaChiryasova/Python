"""
Ваня и Петя поспорили, кто быстрее решит 
следующую задачу: “Задана последовательность
неотрицательных целых чисел. Требуется определить
значение наибольшего элемента
последовательности, которая завершается первым
встретившимся нулем (число 0 не входит в
последовательность)”. Однако 2 друга оказались не 
такими смышлеными. Никто из ребят не смог до 
конца сделать это задание. Они решили так: у кого 
будет меньше ошибок в коде, тот и выиграл спор.
Ваня:                    
n = int(input())            верно
max_number = 1000           не верно, макс.число д.б. равно n или -1
while n != 0:               верно
 n = int(input())           
 if max_number > n:         не верно, здесь должны проверять макс < n
 max_number = n             верно
print(max_number)           Итого: 2 ошибки

Петя:
n = int(input())            верно
max_number = -1             верно
while n < 0:                не верно, д.б. пока n =! 0
 n = int(input())
 if max_number < n:         верно
 n = max_number             не верно, д.б. макс = n
print(n)                    не верно, должны выводить макс.
                            Итого: 3 ошибки
"""