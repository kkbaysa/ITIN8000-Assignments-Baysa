from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


iris = load_iris()
X = iris.data
y = iris.target

for i in range(1, 6):
    # Split up data into training and testing sets
    XTrainSet, XTestingSet, yTrainSet, yTestingSet = train_test_split(X, y, test_size=0.2, shuffle=True)
    # implement Gaussian Naive Bayes
    gnb = GaussianNB()
    # look at frequencies
    gnb.fit(XTrainSet, yTrainSet)
    #predict classification
    y_pred = gnb.predict(XTestingSet)
    print("Number of mislabeled points out of a total %d points : %d"
          % (XTestingSet.shape[0], (yTestingSet != y_pred).sum()))
