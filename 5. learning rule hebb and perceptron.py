import numpy as np
q=np.array([1,-1,0,0.5])
print('Intial weights', q)
w=np.transpose(q)
c=0.1
x1 = np.array([1, -2, 1.5, 0])
x2 = np.array([1, -0.5, -2, -1.5])
x3 = np.array([0, 1, -1, 1.5])
def signum(x):
    return np.sign(x)
for i in range(10):
    net1 = np.dot(w,x1)
    o1 = signum(net1)
    dw = c*o1*x1
    w=w+dw
    net2 = np.dot(w,x2)
    o2=signum(net2)
    dw = c*o2*x2
    w=w+dw
    net3 = np.dot(w,x3)
    o3=signum(net3)
    dw = c*o3*x3
    w=w+dw
print('Ater iterating 10 times updated weights are', w)
    
import numpy as np
q=np.array([1,-1,0,0.5])
x1 = np.array([1, -2, 0,-1])
x2 = np.array([0, 1.5, -0.5, -1])
x3 = np.array([-1, 1, 0.5, -1])
print('Intial weights', q)
w=np.transpose(q)
c=0.1
d1= -1
d2= -1
d3= 1
def signum(x):
    return np.sign(x)

for i in range(10):
    net1 = np.dot(w,x1)
    o1 = signum(net1)
    e1 = d1 - o1
    dw = c*e1*x1
    w=w+dw
    net2 = np.dot(w,x2)
    o2=signum(net2)
    e2=d2-o2
    dw = c*e2*x2
    w=w+dw
    net3 = np.dot(w,x3)
    o3=signum(net3)
    e3 = d3-o3
    dw = c*e3*x3
    w=w+dw
    if(e1==0 and e2 ==0 and e3==0):
        break
print('Found error zero at interation',i)
print('Weights after interating are' ,w)  