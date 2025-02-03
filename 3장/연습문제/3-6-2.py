import numpy as np
import matplotlib.pyplot as plt

sigma=1

fig=plt.figure()
ax = plt.axes(projection='3d')

def g(y,x):
    return (1/((sigma**2)*(2*3.14)))*(np.exp((-(y*y+x*x)/(2*sigma**2))))

x= np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)
X,Y=np.meshgrid(x,y)

z=g(y,x)
Z=g(Y,X)


ax.plot_surface(X, Y, Z, cmap='viridis')

plt.show()