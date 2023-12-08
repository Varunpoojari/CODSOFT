import numpy as np

Arr1 = np.array([1,2,3,4,5])

print(Arr1)

print(type(Arr1))


NewArr = np.delete(Arr1,2)
print(NewArr)


Arr2 = np.array([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]])
print(Arr2)
print(type(Arr2))

NewArr = np.delete(Arr2,17)
print(NewArr)

