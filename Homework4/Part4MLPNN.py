from sklearn.datasets import load_iris
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


# convert accuracy to a decimal
def toPercent(decimal):
    return "{:.2%}".format(decimal)


iris = load_iris()
X = iris.data
y = iris.target

X, y = make_classification(n_samples=100, random_state=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

scaler = StandardScaler()
scaler.fit(X_train)

train_data = scaler.transform(X_train)
test_data = scaler.transform(X_test)

# creating the classifier
mlp = MLPClassifier(hidden_layer_sizes=(10, 5), max_iter=1000)
mlp.fit(X_train, y_train)

predictions_train = mlp.predict(train_data)
print("Accuracy of training data", toPercent(accuracy_score(predictions_train, y_train)))

predictions_test = mlp.predict(test_data)
print("Accuracy of testing data",  toPercent(accuracy_score(predictions_test, y_test)))


