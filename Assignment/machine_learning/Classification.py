import matplotlib.pyplot as plt


dach_length = [55, 57, 64, 63, 58, 49, 54, 61]
dach_height = [30, 31, 36, 30, 33, 25, 37, 34]

jin_length = [56, 47, 56, 46, 49, 53, 52, 48]
jin_height = [52, 52, 50, 53, 50, 53, 49, 54]

plt.legend(loc='upper right')

plt.scatter(dach_length, dach_height, c='r', label='Dachshund')
plt.scatter(jin_length, jin_height,c='b',marker='^', label='Jindo dog')

plt.xlabel('Length')
plt.ylabel('Height')
plt.title("Dog size")

newdata_length = [60]
newdata_height = [30]

plt.scatter(newdata_length, newdata_height, s=100, marker='p',c='g', label='new Data')
plt.legend(loc='upper right')

plt.show()
