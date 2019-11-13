##Program for Delta Learning Rule
import numpy as np

w = np.transpose(np.array([1, -1, 0, 0.5]))
x1 = np.array([1, -2, 0, -1])
x2 = np.array([0, 1.5, -0.5, -1])
x3 = np.array([-1, 1, -0.5, -1])


def bipolar_sigmoid(net):
    x = (2/(1+np.exp(-net))-1)
    return x

c = 0.1
d1 = -1
d2 = -1
d3 =1
count =1 


for i in range(5000):
    net1 = np.dot(w,x1)
    o1 = bipolar_sigmoid(net1)
    e1 =  (1/2)*(d1 - o1)**2
    dw = c*(d1 - o1)*(1/2)*(1 - o1*o1)*x1
    w =w + dw
    
    net2 = np.dot(w,x2)
    o2 = bipolar_sigmoid(net2)
    e2 =  (1/2)*(d2 - o2)**2
    dw = c*(d2 - o2)*(1/2)*(1 - o2*o2)*x2
    w = w + dw
    
    net3 = np.dot(w,x3)
    o3 = bipolar_sigmoid(net3)
    e3 =  (1/2)*(d2 - o2)**2
    dw = c*(d3 - o3)*(1/2)*(1 - o3*o3)*x3
    w = w+dw 
    
    if(abs(e1)<= 0.1 and abs(e2)<=0.1 and abs(e3)<=0.1):
        break

print('Found error minimum at interation',i+1)
print('Weights after interating are' ,w)



