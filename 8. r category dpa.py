import numpy as np

x1 = np.array([10, 2, -1])
x2 = np.array([2, -5, -1])
x3 = np.array([-5, 5, -1])

w1 = np.array([1, 1, 0])
w2 = np.array([-1, -1, -1])
w3 = np.array([2, 1, -1])
w=[]
w.append(w1)
w.append(w2)
w.append(w3)
x=np.array([0,0,0])
d1=np.array([1, -1, -1])
d2=np.array([-1, 1, -1])
d3=np.array([-1, -1, 1])
c=0.5

def signum(net):
    for i in range(len(net)):
        if net[i]>=0:
            x[i]=1
        else:
            x[i]=-1
    return x

for j in range(100):
    net1 = np.dot(w, x1)
    o1 = signum(net1)
    e1 = d1 - o1
    for i in range(len(e1)):
        if(e1[i]!=0):
            w[i]=w[i]+(c*e1[i]*x1)
    
    net2 = np.dot(w, x2)
    o2 = signum(net2)
    e2 = d2 - o2
    for i in range(len(e2)):
        if(e2[i]!=0):
            w[i]=w[i]+(c*e2[i]*x2)
            
    net3 = np.dot(w, x3)
    o3 = signum(net3)
    e3 = d3 - o3
    for i in range(len(e1)):
        if(e3[i]!=0):
            w[i]=w[i]+(c*e3[i]*x3)

    if(np.all(e1==0) and np.all(e2 == 0) and np.all(e3==0)):
        break
print('Final weights are', w)
print('Found zero error at '+str(j+1) +'th iteration')
