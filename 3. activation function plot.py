import numpy as np
import matplotlib.pyplot as plt
net=np.linspace(-10,10,101)

def bipolar_sigmoid(net,l):
    x=(2/(1+np.exp(-(l*net)))-1)
    return x
plt.subplot(4,2,1)
for l in range(1,11):
    x=bipolar_sigmoid(net,l)
    plt.plot(net,x,label=l)
    plt.legend(title='lambda')
    plt.title('Bipolar Sigmoid')
    plt.xlabel('net')
    plt.ylabel('f(net)')

def unipolar_sigmoid(net,l):
    x=(1/(1+np.exp((-l*net))))
    return x
plt.subplot(4,2,2)  
for l in range(1,11):
    x=unipolar_sigmoid(net,l)
    plt.plot(net,x,label=l)
    plt.legend(title='lambda')
    plt.title('Unipolar Sigmoid')
    plt.xlabel('net')
    plt.ylabel('f(net)')
    

def bipolar_signum(net):
    a=np.sign(net)
    return a
plt.subplot(4,2,3) 
x=bipolar_signum(net)
plt.plot(net,x)
plt.title('Bipolar Signum')
plt.xlabel('net')
plt.ylabel('f(net)')
    
def bipolar_signum(net):
    a=np.sign(net)
    return a
plt.subplot(4,2,3) 
x=bipolar_signum(net)
plt.plot(net,x,label=l)
plt.title('Bipolar Signum')
plt.xlabel('net')
plt.ylabel('f(net)')
    
def unipolar_signum(net):
    a=np.sign(net)+1
    return a/2
plt.subplot(4,2,4) 
x=unipolar_signum(net)
plt.plot(net,x,label=l)
plt.title('Unipolar Signum')
plt.xlabel('net')
plt.ylabel('f(net)')
    
def linear(net):
    a=net
    return a
plt.subplot(4,2,5) 
x=linear(net)
plt.plot(net,x)
plt.title('Linear')
plt.xlabel('net')
plt.ylabel('f(net)')

def relu_my(x):
    f=np.zeros(21)
    for i in range(1,21):
        if x[i]>0:
            f[i]=x[i]
        else:
            f[i]=0
    return f
net=np.linspace(-10,10,21)
plt.subplot(4,2,6) 
x=relu_my(net)
plt.plot(net,x)
plt.title('Relu')
plt.xlabel('net')
plt.ylabel('f(net)')

def relu_myl(x):
    f=np.zeros(21)
    for i in range(1,21):
        if x[i]>0:
            f[i]=x[i]
        else:
            f[i]=0.1*x[i]
    return f
net=np.linspace(-10,10,21)
plt.subplot(4,2,7) 
x=relu_myl(net)
plt.plot(net,x)
plt.title('Leaky Relu')
plt.xlabel('net')
plt.ylabel('f(net)')

