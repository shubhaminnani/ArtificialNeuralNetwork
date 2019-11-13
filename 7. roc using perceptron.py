import numpy as np
import matplotlib.pyplot as plt

w = np.array([-2.5, 1.75])
x1 = np.array([1, 1])
x2 = np.array([-0.5, 1])
x3 = np.array([3, 1])
x4 = np.array([-2, 1])
d1 = 1
d2 = -1
d3 = 1
d4 = -1
c=0.5
v=[]
v.append(w)

def signum(net):
    return np.sign(net)

for i in range(10):
    net1 = np.dot(w, x1)
    o1 = signum(net1)
    e1 = d1 - o1
    dw = c*e1*x1
    w= w +dw
    v.append(w)
    
    net2 = np.dot(w, x2)
    o2 = signum(net2)
    e2 = d2 - o2
    dw = c*e2*x2
    w= w +dw
    v.append(w)
    
    net3 = np.dot(w, x3)
    o3 = signum(net3)
    e3 = d3 - o3
    dw = c*e3*x3
    w= w +dw
    v.append(w)
    
    net4 = np.dot(w, x4)
    o4 = signum(net4)
    e4 = d4 - o4
    dw = c*e4*x4
    w= w +dw
    v.append(w)
    
    if(e1==0 and e2 == 0 and e3==0 and e4==0):
        break
print('Found zero error at '+str(i) +' iteration')
c1 = np.zeros(17)
c2 = np.zeros(17)
for i in range(17):
    c1[i]=v[i][0]
    c2[i]=v[i][1]


x = np.linspace(-5, 5, 101)
y1 = -1*(x)
y2 = 2*(x)
y3 = -(1/3)*(x)
y4 = (1/2)*(x)
fig, ax = plt.subplots()
ax.plot(c1,c2,x,y1,x,y2,x,y3,x,y4)
plt.title('Region of Convergence')
plt.xlabel('x1')
plt.ylabel('x2')
ax.legend(('weight', 'y1', 'y2','y3', 'y4'))
ax.fill_between(x, y3, y4,where=x>=0,facecolor='yellow')
plt.show()



