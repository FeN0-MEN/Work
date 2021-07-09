import module_calc
import module_time
import module_start
import module_write
from timeit import default_timer as timer

start = timer()

x, y, r = module_start.dots()
"""
r = int(input("r = "))
x, y = input('Введите координаты (x;y): ').split()
x = int(x)
y = int(y)
"""
count = module_calc.calc(x, y, r)

year, month, day, hour, minute = module_time.time()

end = timer()
timer = end - start

module_write.value(year, month, day, hour, minute, timer)
