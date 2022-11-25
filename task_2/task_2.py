# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.
# ⋁ - "Или"
# ⋀ - "И"
# ¬ - "Не"

print('Введите значения предикат X,Y,Z')
x = bool(input())
y = bool(input())
z = bool(input())

if not(x or y or z) == (not x and not y and not z):
    print('True')
else:
    print('False')