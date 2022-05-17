#class_20220517

print("array:")
import numpy as np
x=np.array([1.0,2.0,3.0])
print(x)

y=np.array([2.0,4.0,6.0])

print(x+y)
print(x*y)
print(x/y)

print("行列:")
A=np.array([[1,2],[3,4]])
print(A)
print(A.shape)
print(A.dtype)

B=np.array([[3,0],[0,6]])
print(A+B)
print("A*B:",A*B)
#broadcast
print(A*10)

B=np.array([10,20])
print(A*B)


P=np.array([[51,55],[14,19],[0,4]])
print(P[0])
print(P[0][1])

P=P.flatten()
print(P[np.array([0,2,4])])
print(P[P>15])

import matplotlib.pyplot as plt
x=np.arange(0,6,0.1)
y=np.sin(x)

plt.plot(x,y)
plt.show()


print("basics:")
print(3*4)
print(7/5)
print(type(3.1415))

x=10
print(x)
x=100
y=3.14
print(x*y)
print(type(x*y))

a=[1,2,3,4,5]
print(a)
print(len(a))
print(a[0],a[0:2],a[:3],a[:-1])


for i in [1,2,3]:
    print(i)


def hello():
    print("HEllo World")

hello()