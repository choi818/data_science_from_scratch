from matplotlib import pyplot as plt
from collections import Counter

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

plt.bar([x for x in histogram.keys()],  # move bar to the 4 times left
        histogram.values(),                 # set the height of the bar
        8)                                  # width = 8

plt.axis([-5, 105, 0, 5])                   # -5 <= x.axis <= 105, 0 <= y.axis <= 5
plt.xticks([10 * i for i in range(11)])     # labels of x.axis = 0, 10, 20, ..., 100
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")

plt.show()
