# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).

print('Введите координаты точки (Х,Y) через запятую: ')
coordinates = input().split(',')

if int(coordinates[0]) >= 0 and int(coordinates[1]) >= 0:
    print('Первая четверть')
elif int(coordinates[0]) <= 0 and int(coordinates[1]) >= 0:
    print('Вторая четверть')
elif int(coordinates[0]) <= 0 and int(coordinates[1]) <= 0:
    print('Третья четверть')
else:
    print('Четвертая четверть')