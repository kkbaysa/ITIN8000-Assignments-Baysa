import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets, metrics
from sklearn import model_selection
from sklearn import neighbors
from sklearn.decomposition import PCA
import Part1Plot
import Part2Accuracy

iris = datasets.load_iris()
x = iris.data
y = iris.target

# Print data correlations on graphs (x6)
# Part1.graph(iris)

# Run 5 test trials of iris data
Part2Accuracy.splitData(x, y)



# # To getter a better understanding of interaction of the dimensions
# # plot the first three PCA dimensions
# fig = plt.figure(1, figsize=(8, 6))
# ax = Axes3D(fig, elev=-150, azim=110)
# x_reduced = PCA(n_components=3).fit_transform(iris.data)
# ax.scatter(
#     x_reduced[:, 0],
#     x_reduced[:, 1],
#     x_reduced[:, 2],
#     c=y,
#     cmap=plt.cm.Set1,
#     edgecolor="k",
#     s=40,
# )
# ax.set_title("First three PCA directions")
# ax.set_xlabel("1st eigenvector")
# ax.w_xaxis.set_ticklabels([])
# ax.set_ylabel("2nd eigenvector")
# ax.w_yaxis.set_ticklabels([])
# ax.set_zlabel("3rd eigenvector")
# ax.w_zaxis.set_ticklabels([])
#
# plt.show()
