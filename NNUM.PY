import numpy as np

arr1=np.arange(2,11).reshape(3,3)
arr2=np.arange(1,10).reshape(3,3)
arr3=arr1.dot(arr2)
print(arr1)
print(arr2)
print(arr3)

x=np.array([[1,2,3],[1,2,3]])
y=np.array([[1,2,3],[1,2,3]])
print(x*y)