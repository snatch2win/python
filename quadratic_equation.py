# квадратное урaвнение: ax ** 2 + bx + c = 0
# Дискриминант квадратного  уравнения: D = b ** 2 - 4ac

import math

print("Введите первое число")
a = int(input())
print("Введите второе число")
b = int(input())
print("Введите третье число")
c = int(input())

opposite = -b

decision = b ** 2 - 4 * a * c
print("РЕШЕНИЕ:")
print("Находим дискриминант квадратного уравнения:")
print("дискриминант равен: ")
print(decision)

if decision > 0:
    print("Дискриминант больше нуля, квадратное уравнение имеет два корня:")
    x1 = (opposite - math.sqrt(decision)) / (2 * a)
    print(x1)
    x2 = (opposite + math.sqrt(decision)) / (2 * a)
    print(x2)
elif decision == 0:
    print("ERROR!!!")
    print("Дискриминант не может равняться нулю!!")
else:
    print("Так как дискриминант меньше нуля, то уравнение не имеет действительных решений.")


