from sklearn import model_selection, neighbors, metrics, datasets


# Part 2 of the assignment will split the data into a
# testing and training set to measure the accuracy of the randomized data
iris = datasets.load_iris()
x = iris.data
y = iris.target

# run 5 trials of random data
for i in range(1, 6):
    # split data into training and testing sets
    # testing has 20% of data and trial has 80%
    xTrainSet, xTestSet, yTrainSet, yTestSet = model_selection.train_test_split(x, y, test_size=.2, shuffle=True)
    # print("Training set", i, "\b:\n", xTrainSet)
    # print("Training set", i, "\b:\n", xTestSet)
    # print("Testing set", i, "\b:\n", yTrainSet)
    # print("Testing set", i, "\b:\n", yTestSet)

    # set K value to 1
    neigh = neighbors.KNeighborsClassifier(n_neighbors=1)
    # look at the nearest neighbors
    neigh.fit(xTrainSet, yTrainSet)

    # predict the class labels for the data set
    yPredict = neigh.predict(xTestSet)

    # determine the accuracy between the test target values and the predicted values
    decimalResult = metrics.accuracy_score(yTestSet, yPredict)

    # convert accuracy to a decimal
    percentResult = "{:.2%}".format(decimalResult)
    print("Accuracy", i, "\b:", percentResult)
