""" Подпрограмы """


# -----------------------------------------------------------------------------------------------------------------------


def minutes(Mp, Motp):
    return int(Mp + Motp)


def hours(HH, Hp, Hotp):
    return int(HH + Hp + Hotp)


def endingH(HH):
    ending = "s"
    if HH == 1:
        ending = ""
    return ending


def endingM(MM):
    ending = "s"
    if MM == 1:
        ending = ""
    return ending


def endingD(days):
    ending = "s"
    if days == 1:
        ending = ""
    return ending


# -----------------------------------------------------------------------------------------------------------------------

"""" Это сновная программа """""

# Ввод данных

Hotp = int(input('Введите время отправления (Часы) '))
Motp = int(input('(Минуты) '))
Hp = int(input("Введите время в пути (часы) "))
Mp = int(input('(Минуты) '))
HH = 0
days = 0

# Проверка условия что часы<24 минуты<60

MM = minutes(Mp, Motp)
while MM > 59:
    MM = MM - 60
    HH = int(HH + 1)

HH = hours(HH, Hotp, Hp)
while HH > 23:
    HH = int(HH - 24)
    days = int(days + 1)

# Вывод данных

print("%.2d Hour%s : %.2d minute%s \n%d day%s" % (HH, endingH(HH), MM, endingM(MM), days, endingD(days)))
