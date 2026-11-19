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

#creating a random array
randomarray = np.random.randint(1,50,20)
print(randomarray)
print(randomarray.max())
print(randomarray.min())
print(np.sort(randomarray))
print(np.sort(randomarray)[::-1])
reshapearray = randomarray.reshape(5,4)
print(reshapearray)

#rowise sorting
print(np.sort(reshapearray,axis=1))

#collumnwise sorting
print(np.sort(reshapearray,axis=0))




"""newarray = np.arange(1,25)
for i in range(1,len(newarray)):
    for j in range(1,len(newarray)):
        if i // j == 0 and i*j == len(newarray):
            print(newarray.reshape(i,j))"""