import numpy as np

array = np.arange(3,27)
print(array[:5])
print(array[-5:])
print(array[::4])

newarray = np.arange(1,50).reshape(7,7)
print("")
print(newarray)
print(newarray[2:5,2:5])
print(newarray[6])
print(newarray[:,6])

randarray = np.random.randint(1,50,20)
newrandarray = randarray[randarray<7]
oddrandarray = randarray[randarray%2 != 0]
print("")
print(randarray)
print(newrandarray)
print(oddrandarray)

array3 = np.arange(1,11)
add5array = array3+5
sub3array = array3-3
print("")
print(array3)
print(add5array)
print(sub3array)

array4 = np.random.randint(1,100,49).reshape(7,7)
array5 = np.random.randint(1,100,49).reshape(7,7)
print("")
print(array4)
print(array5)
print(array4*array5)
print(array4+array5)
print(array4@array5)