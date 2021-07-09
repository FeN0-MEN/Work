import math


def dis():
    print("(%.5f)*X^2+(%.5f)*X+(%.5f)=0" % (a, b, c))
    print('Количество корней: 2')
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("x1 = %.5f \nx2 = %.5f" % (x2, x1))


def dis0():
    print("(%.5f)*X^2+(%.5f)*X+(%.5f)=0" % (a, b, c))
    print('Количество корней: 1')
    x = -b / (2 * a)
    print("x1 = %.5f" % x)
    print("x2 = %.5f" % x)


def disminus():
    print("(%.5f)*X^2+(%.5f)*X+(%.5f)=0" % (a, b, c))
    print("Количество корней: 0")


# Ввод коэфицентов
print("Введите коэффициенты для уравнения")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

# Подсчёт дискриминанта
D = b ** 2 - 4 * a * c

# Если дискриминант положительный
if D > 0:
    dis()
# Если дискриминант равен нулю
elif D == 0:
    dis0()
# Если дискриминант отрицательный
else:
    disminus()
