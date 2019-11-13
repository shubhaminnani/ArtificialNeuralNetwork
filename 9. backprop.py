import numpy as np

x1=np.array([0,0,1])
x2=np.array([0,1,1])
x3=np.array([1,0,1])
x4=np.array([1,1,1])
x=[x1,x2,x3,x4]
d1=0
d2=1
d3=1
d4=0
d=[d1,d2,d3,d4]
w=np.array([1,1,-1])
v=np.array([[1,-1,-1],[1,-2,1]])

def sigmoid(net):
    x=(2/(1+np.exp(-(net))))-1
    return x

n=0.05
for j in range(10000):
    E=0
    for i in range(4):
        net1 = np.dot(v, x[i])
        y1 = sigmoid(net1)
        y1 = np.append(y1,1)
        net2 = np.dot(w, y1)
        o1 = sigmoid(net2)
        e=0.5*(d[i]-o1)**2
        E=E+e
        do = (0.5)*(d[i]-o1)*(1-(o1**2)) 
        dy = (0.5)*w*do*(1-(y1**2))
        dy=dy[:2]
        w = w + n*do*y1
        v = v + n*(dy.reshape(2,1))*(x[i].reshape(1,3))
    if(E<0.01):
        break
print('Required iteration are '+str(j+1))
print('Updated weights of V are ' +str(v))
print('Updated weights of W are ' +str(w))
