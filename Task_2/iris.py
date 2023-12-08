from sklearn.datasets import load_iris

iris = load_iris()

print("Features names of iris dataset")
print(iris.feature_names)

print("Target names of iris dataset")
print(iris.target_names)

print("")

for i in range (len(iris.target)):
    print("ID: %d, Label %s, Feature : %s"% (i,iris.data[i], iris.target[i]))
