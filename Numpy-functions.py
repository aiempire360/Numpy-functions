import numpy as np

arr = np.zeros((2,3,4))
print(arr)

arr2 = np.ones((2,3,4))
print(arr2)

arr3 = np.full((2,3,4), 7)
print(arr3)

arr4 = np.eye((4))
print(arr4)

# start , stop , step
arr5 = np.arange(1, 100 )
print(arr5)

arr6 = np.linspace(2,30,10)
print(arr6)

# Aggregate functions : summarize data and return a single value

arr7 = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
print(np.sum(arr7))
print(np.mean(arr7))
print(np.min(arr7))
print(np.max(arr7))
print(np.argmin(arr7))
print(np.argmax(arr7))

print(np.sum(arr7, axis=1))

