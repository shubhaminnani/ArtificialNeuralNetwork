import numpy as np
def and_gate(x1,x2):
    x=[x1,x2]
    w=[1,1]
    net = np.sum(np.multiply(x,w))
    if net >=2:
        op=1
    else:
        op=0
    print('x1 =',x[0], 'x2 =',x[1], 'w1= ',w[0],'w2 = ',w[1], 'op =',op)          
for i1 in range(2):
    for i2 in range(2):
        and_gate(i1,i2)


def or_gate(x1,x2):
    x=[x1,x2]
    w=[1,1]
    net = np.sum(np.multiply(x,w))
    if net >=1:
        op=1
    else:
        op=0
    print('x1 =',x[0], 'x2 =',x[1], 'w1= ',w[0],'w2 = ',w[1], 'op =',op)
    
for i1 in range(2): 
    for i2 in range(2):
        or_gate(i1,i2)  

def not_gate(x1):
    x=[x1]
    w=[1]
    net = np.sum(np.multiply(x,w))
    if net >=1:
        op=0
    else:
        op=1
    print('x1 =',x[0], 'w1= ',w[0], 'op =',op)        
 
for i1 in range(2): 
    not_gate(i1)   


def nand_gate(x1,x2):
    x=[x1,x2]
    w=[1,1]
    net = np.sum(np.multiply(x,w))
    if net >=2:
        op=0
    else:
        op=1
    print('x1 =',x[0], 'x2 =',x[1], 'w1= ',w[0],'w2 = ',w[1], 'op =',op)
for i1 in range(2): 
    for i2 in range(2):
        nand_gate(i1,i2)  

def or_gate(x1,x2):
    x=[x1,x2]
    w=[1,1]
    net = np.sum(np.multiply(x,w))
    if net >=1:
        op=1
    else:
        op=0
    print('x1 =',x[0], 'x2 =',x[1], 'w1= ',w[0],'w2 = ',w[1], 'op =',op)        

for i1 in range(2): 
    for i2 in range(2):
        or_gate(i1,i2) 


def exor_gate(x1,x2):
    x=[x1,x2]
    w1=[1,-1]
    w2=[-1,1]
    w5=[1,1]

    t1=np.sum(np.multiply(x,w1))
    if t1>=1:
        net1=1
    else:
        net1=0
    t2=np.sum(np.multiply(x,w2))
    if t2>=1:
        net2=1
    else:
        net2=0
    net12=[net1,net2]
    net3=np.sum(np.multiply(net12,w5))
    
    if net3>=1:
        op=1
    else:
        op=0
    print('x1 =',x[0], 'x2 =',x[1], 'w1= ',w1[0],'w2= ',w1[1],'w3 = ',w2[0],'w4 =', w2[1],'w5 =',w5[0],'w5 =',w5[1], 'op =',op)

for i1 in range(2):
    for i2 in range(2):
        exor_gate(i1,i2)
