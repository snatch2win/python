# квадратное урaвнение: ax ** 2 + bx + c = 0
# Дискриминант квадратного  уравнения: D = b ** 2 - 4ac

import math

print("Введите первое число")
first_number = int(input())
print("Введите второе число")
second_number = int(input())
print("Введите третье число")
third_number = int(input())

opposite = -second_number

decision = second_number ** 2 - 4 * first_number * third_number
print("РЕШЕНИЕ:")
print("Находим дискриминант квадратного уравнения:")
print(decision)

if decision > 0:
    print("Дискриминант больше нуля, квадратное уравнение имеет два корня:")
    x1 = (opposite - math.sqrt(decision)) / (2 * first_number)
    print(x1)
    x2 = (opposite + math.sqrt(decision)) / (2 * first_number)
    print(x2)
else:
    print("Так как дискриминант меньше нуля, то уравнение не имеет действительных решений.")


