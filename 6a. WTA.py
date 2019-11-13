# Program for WTA learning rule
import numpy as np

w1 = np.transpose(np.array([1, 0]))
w2 = np.transpose(np.array([0, -1]))
x1 = np.array([0.8, 0.6])
x2 = np.array([0.17, -0.98])
x3 = np.array([0.707, 0.707])
x4 = np.array([0.34, -0.93])
x5 = np.array([0.6, 0.8])

c= 0.1
xi = [x1, x2, x3, x4, x5]

k = np.ones([1,5])
k = np.append(k,np.zeros([99,5]),axis=0)

def weights(x, w):
    dw = c* (x -w)
    w = w + dw
    return w
i=0

while(not(np.all(k[i]==k[i-1]))):
    i= i+1         
    for j in range(5):
        net1 = np.dot(xi[j], w1)
        net2 = np.dot(xi[j], w2)
        if(net1>net2):
            weights(xi[j], w1)
            k[i][j]=0
        else:
            weights(xi[j], w2)
            k[i][j]=1  
    
print('Found same cluster after iterating '+str(i)+' times')