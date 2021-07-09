import datetime


def time():
    year = datetime.datetime.now().date().year
    month = datetime.datetime.now().date().month
    day = datetime.datetime.now().date().day
    hour = datetime.datetime.now().time().hour
    minute = datetime.datetime.now().time().minute

    return year, month, day, hour, minute
