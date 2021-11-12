"""This is Part 1 of homework 4 for ITIN8000
This will take the iris data set and graph the data combinations
This work has been done by Kaitlyn Baysa"""

import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()
x = iris.data
y = iris.target
# import some data to play with
measurements = iris.data[:, :4]
targets = iris.target
target_names = iris.target_names
count = 0
for measurement in measurements:
    print(measurement, target_names[targets[count]])
    count = count + 1

# SL x SW
x_min, x_max = x[:, 0].min() - 0.5, x[:, 0].max() + 0.5
y_min, y_max = x[:, 1].min() - 0.5, x[:, 1].max() + 0.5

plt.figure(2, figsize=(8, 6))
plt.clf()

# Plot the training points
plt.scatter(x[:, 0], x[:, 1], c=y, cmap=plt.cm.Set1, edgecolor="k")
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())

plt.show()

# SL(0) x PL(2)

x_min, x_max = x[:, 0].min() - 0.5, x[:, 0].max() + 0.5
y_min, y_max = x[:, 2].min() - 0.5, x[:, 2].max() + 0.5

plt.figure(2, figsize=(8, 6))
plt.clf()

# Plot the training points
plt.scatter(x[:, 0], x[:, 2], c=y, cmap=plt.cm.Set1, edgecolor="k")
plt.xlabel("Sepal length")
plt.ylabel("Petal length")

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())

plt.show()

# SL(0) x PW(3)

x_min, x_max = x[:, 0].min() - 0.5, x[:, 0].max() + 0.5
y_min, y_max = x[:, 3].min() - 0.5, x[:, 3].max() + 0.5

plt.figure(2, figsize=(8, 6))
plt.clf()

plt.scatter(x[:, 0], x[:, 3], c=y, cmap=plt.cm.Set1, edgecolor="k")
plt.xlabel("Sepal length")
plt.ylabel("Petal width")

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())

plt.show()

# SW(1) x PL(2)
x_min, x_max = x[:, 1].min() - 0.5, x[:, 1].max() + 0.5
y_min, y_max = x[:, 2].min() - 0.5, x[:, 2].max() + 0.5

plt.figure(2, figsize=(8, 6))
plt.clf()

plt.scatter(x[:, 1], x[:, 2], c=y, cmap=plt.cm.Set1, edgecolor="k")
plt.xlabel("Sepal width")
plt.ylabel("Petal length")

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())

plt.show()

# SW(1) x PW(3)
x_min, x_max = x[:, 1].min() - 0.5, x[:, 1].max() + 0.5
y_min, y_max = x[:, 3].min() - 0.5, x[:, 3].max() + 0.5

plt.figure(2, figsize=(8, 6))
plt.clf()

plt.scatter(x[:, 1], x[:, 3], c=y, cmap=plt.cm.Set1, edgecolor="k")
plt.xlabel("Sepal width")
plt.ylabel("Petal width")

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())

plt.show()

# PL(2) x PW(3)
x_min, x_max = x[:, 2].min() - 0.5, x[:, 2].max() + 0.5
y_min, y_max = x[:, 3].min() - 0.5, x[:, 3].max() + 0.5

plt.figure(2, figsize=(8, 6))
plt.clf()

# Plot the training points
plt.scatter(x[:, 2], x[:, 3], c=y, cmap=plt.cm.Set1, edgecolor="k")
plt.xlabel("Petal length")
plt.ylabel("Petal width")

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())

plt.show()
