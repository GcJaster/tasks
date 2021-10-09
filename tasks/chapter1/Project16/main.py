""" Напишите программу, которая будет запрашивать у пользователя радиус и сохранять его в переменной r.
После этого она должна вычислить площадь круга с заданным радиусом и объем шара с тем же радиусом.
Используйте в своих вычислениях константу pi из модуля math. """

from math import pi

r = int(input("Введите радиус: "))

area = pi * r**2
volume = 4/3 * pi * r**3

print(f"Площадь круга равна: {area:.2f} см^2", f"Объём шара равен: {volume:.2f} см^3", sep='\n')