import module_calc
import module_start
import module_time
import main_program


def value(year, month, day, hour, minute, time):
    f = open('output.txt', 'w', encoding='UTF-8')
    f.write("%s.%s.%s %s:%s \n" % (year, month, day, hour, minute))
    f.write("%s \n" % count)
    f.write("%0.2f \n" % time)
    f.close()


time = main_program.timer
year, month, day, hour, minute = module_time.time()
x, y, r = module_start.dots()
count = module_calc.calc(x, y, r)
