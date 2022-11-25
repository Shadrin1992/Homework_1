# Напишите программу, которая по заданному номеру четверти, показывает диапазон 
# возможных координат точек в этой четверти (x и y).

print('Введите номер четверти: ')
quarter_num = int(input())

if quarter_num == 1:
    print('x>0 y>0')
elif quarter_num == 2:
    print('x<0 y>0')
elif quarter_num == 3:
    print('x<0 y<0')
else:
    print('x>0 y<0')