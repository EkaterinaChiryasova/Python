"""
Петя, Катя и Сережа делают из бумаги журавликов. Вместе
они сделали S журавликов. Сколько журавликов сделал каждый
ребенок, если известно, что Петя и Сережа сделали одинаковое
количество журавликов, а Катя сделала в два раза больше журавликов,
чем Петя и Сережа вместе?
6 -> 1 4 1
24 -> 4 16 4
60 -> 10 40 10
"""

s = int(input("Сколько сделано журавликов: "))
sergey = s / 6
petr = sergey
kat = (sergey + petr) * 2
print(f"Сергей сделал {sergey} журавликов, Катя {kat}, Петя {petr}")