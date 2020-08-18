from csv import reader
import numpy
import matplotlib.pyplot as plt

# read csv file as a list of lists
with open('data.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)
    print(list_of_rows)
x = []
y = []
for item in list_of_rows[0]:
    x.append(int(item))

for item in list_of_rows[1]:
    y.append(int(item))

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(1, 22, 100)

testVal = 17
speed = mymodel(testVal)

print("Summary Test")
print ("x : ", x)
print ("y : ", y)
print("mymodel : ", mymodel)
print("testVal : ", testVal)
print("speed : ", speed)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()
