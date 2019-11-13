import numpy as np
np.random.seed(2)
def signum(net):
    shape = np.shape(net)
    z = np.zeros(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            if net[i][j] > 0:
                z[i][j] = 1
            else:
                z[i][j] = -1
    return z  

a1=np.array([[1,1,-1,-1,1]])
a2=np.array([[-1,1,1,-1,-1]])
b1=np.array([[-1,-1,1,1,-1,1,-1]])
b2=np.array([[-1,-1,-1,-1,-1,-1,-1]])
a3=np.array([[1,1,-1,1,-1]])
b3=np.array([[1,1,1,-1,-1,-1,-1]])
a4 = np.array([np.random.randint(-1,2,5)])
a4[a4<0.5]=-1
b4 = np.array([np.random.randint(-1,2,7)])
b4[b4<0.5]=-1

W=np.outer(a1,b1)+np.outer(a2,b2)+np.outer(a3,b3)+np.outer(a4,b4)
print('Final Weights are \n',str(W))
B1=np.dot(a1,W)
B1=signum(B1)
A1=np.dot(B1,W.T)
A1=signum(A1)

B2=np.dot(a2,W)
B2=signum(B2)
A2=np.dot(B2,W.T)
A2=signum(A2)

B3=np.dot(a3,W)
B3=signum(B3)
A3=signum(np.dot(B3,W.T))

B4=np.dot(a4,W)
B4=signum(B4)
A4=signum(np.dot(B4,W.T))

print('\n Error \n')
print(A1-a1)
print(A2-a2)
print(A3-a3)
print(A4-a4)