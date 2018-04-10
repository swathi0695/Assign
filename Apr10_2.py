import numpy as np
array_2d=np.ndarray((3,3),dtype=int)
print("Dimension : ", array_2d.shape)
array_2d.fill(7)
print(array_2d)
array_3d = array_2d.reshape(1,1,1)
print(array_3d)
array_3d+=5
print("After adding 5 :", array_3d)
print(array_3d)

array_3d -= 2
print("After subtracting 5 :", array_3d)
print(array_3d)

array_3d *= 2
print("After multiplying 5 :", array_3d)
print(array_3d)

