import numpy as np

information = [1,4,6,22,85,37]

#creating an array
myarray = np.array(information)
print(information)
print(myarray)

print(information*3) #repeating list
print(myarray*3) #element multiplication
print(information + information)
print(myarray + myarray)

#additional array features + functionalities
array1 = np.zeros((6,5))
array2 = np.ones((4,5))
array3 = np.arange(20).reshape(4,5)
arrays = [array1,array2,array3]
for array in arrays:
    print(array)
    print("dimensions-",array.ndim)
    print("shape-",array.shape)
    print("size-",array.size)
    print("memory (bytes)-",array.nbytes)
    print("-"*100)

newarray = np.arange(1,25)
for i in range(len(newarray)):
    if len(newarray) // 2
