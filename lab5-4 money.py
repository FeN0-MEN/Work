def rubel(price):
    rub = price // 100
    return rub


def cents(penny):
    penny = penny % 100
    return penny


def check1(rubel):
    if rubel(penny) % 10 == 1 and rubel(penny) % 100 not in range(11, 15):
        ending1 = "ь"
    elif 4 >= rubel(penny) % 10 >= 2 and rubel(penny) not in range(11, 15):
        ending1 = "я"
    else:
        ending1 = "ей"
    return ending1


def check2(penny):
    if cents(penny) % 10 == 1 and cents(penny) not in range(11, 15):
        ending2 = "йка"
    elif 4 >= cents(penny) % 10 >= 2 and cents(penny) not in range(11, 15):
        ending2 = "йки"
    else:
        ending2 = "ек"
    return ending2


# Это основная программа
# Ввод данных

penny = int(input('Введите цену покупки '))
ending1 = ""
ending2 = ""

# Вывод данных
print("%d рубл%s\n%d копе%s" % (rubel(penny), check1(rubel), cents(penny), check2(penny)))
