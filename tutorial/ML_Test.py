import numpy
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

mean = numpy.mean(speed)
mode = stats.mode(speed)
median = numpy.median(speed)
std = numpy.std(speed)

print("Summary ")
print("Mean : ", mean)
print("Median : ", median)
print("Std. dev : ", std)
print("Mode : ", mode)
