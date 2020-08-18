import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)


def my_func(x):
    return slope * x + intercept


# Print first before plotting
testVal = 10

predict = my_func(testVal)
print("Summary Test")
print("testVal : ", testVal)
print("predict : ", predict)

myModel = list(map(my_func, x))
plt.scatter(x, y)
plt.plot(x, myModel)
plt.show()



