import math


def calc(x, y, r):
    top_dot = y + r
    bot_dot = y - r
    left_dot = x - r
    right_dot = x + r
    count = 0

    for horizontal in range(left_dot, right_dot + 1):

        for vertical in range(bot_dot, top_dot + 1):

            if math.sqrt((horizontal - x) ** 2 + (vertical - y) ** 2) <= (r):
                count += 1

    return count
