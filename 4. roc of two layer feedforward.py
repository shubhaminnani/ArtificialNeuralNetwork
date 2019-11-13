import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x1=np.linspace(0,6,100)
x2=np.linspace(0,6,100)
x1,x2=np.meshgrid(x1,x2)
net1=x1-1
net2=-x1+2
net3=x2
net4=-x2+3

def signum(net):
    a=np.sign(net)
    return a

o1 = signum(net1)
o2 = signum(net2)
o3 = signum(net3)
o4 = signum(net4)

net4=(o1+o2+o3+o4)-3.5
o5=signum(net4)

fig =plt.figure()
ax=plt.axes(projection='3d')
ax.plot_surface(x1,x2,o5)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('O5')
