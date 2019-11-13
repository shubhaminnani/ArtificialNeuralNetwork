import numpy as np

x = np.array([[1, 2, 3, 4, 5]])
print('Universe :' +str(x))

a = np.array([[1, 2, 3, 4, 5]])
print('Set A : '+str(a))
ua = np.array([[0, 1, 0.5, 0.3, 0.2]])
print('Membership of A :'+str(ua))

v = np.array([[1, 2, 3, 4, 5]])
print('Set V: ' +str(v))
uv = np.array([[0, 0.5, 0.7, 0.2, 0.4]])
print('Membership of V :'+str(uv))

print('Complement of Set A : '+str(a))
uab = 1 - ua
print('Membership of Complement of A' +str(uab))

print('Complement of Set V : '+str(v))
uav = 1 - uv
print('Membership of complement of V' +str(uav))

print('Union Set :' +str(a))
auv = np.maximum(ua, uv)
print('Membership of Union of A and V'+str(auv))

print('Intersection Set :' +str(a))
aiv = np.minimum(ua, uv)
print('Membership of Intersection of A and V' +str(aiv))

print('Set A :' +str(a) +' Set V: '+str(v))
dav1 = aiv
print('Membership of DeMorgan laws A U V(Bar) '+str(dav1))

print('Set A :' +str(a) +' Set V: '+str(v))
dav2 = auv
print('Membership of DeMorgan laws A I V(Bar) '+str(dav2))

print('Set A :' +str(a) +' Set V: '+str(v))
uabUuav = np.maximum(uab,uav)
davr1 = uabUuav
print('Membership of complement of a^ U v^' +str(davr1))

print('Set A :' +str(a) +' Set V: '+str(v))
uabIuav = np.minimum(uab,uav)
davr2 = uabIuav
print('Membership of complement of a^ I v^' +str(davr2))

print('Set A :' + str(a) +' Set V: '+str(v))
ubda = np.minimum(uv,uab)
print('Membership of difference of a and v' +str(ubda))

print('Set A :' +str(a) +' Set V: '+str(v))
uadb = np.minimum(ua,uav)
print('Membership of difference of v and a' +str(ubda))

print('Set A :' +str(a) +' Set V: '+str(v))
w = np.maximum(ua,uab)
print('Union of a U v ' +str(w))
x = np.minimum(ua,uab)
print('Set A :' +str(a) +' Set V: '+str(v))
print('Intersection of a I v ' +str(x))

y = np.maximum(ua,uv)
z = np.maximum(uv,ua)
print('Set A :' +str(a) +' Set V: '+str(v))
if np.all(y==z):
    print('Associative Property of Union holds')
else:
    print('Associative Property of Union does not hold')

m = np.minimum(ua, uv)
n = np.minimum(ua, uv)
print('Set A :' +str(a) +' Set V: '+str(v))
if np.all(m==n):
    print('Associative Property of Intersection holds')
else:
    print('Associative Property of Intersection does not hold')

uz = np.array([[0.4, 0.2, 0.7, 1, 0.5]])

i = np.maximum(ua,np.maximum(uv,uz))
j = np.maximum(np.maximum(ua,uv),uz)
if np.all(i==j):
    print('Commutative Property holds')
else:
    print('Commutative Property does not hold')
    
k = np.maximum(ua, np.minimum(uv,uz))
l = np.minimum(np.maximum(ua,uv),np.maximum(ua,uz))
if np.all(k==l):
    print('Distributive Property holds')
else:
    print('Distributive Property does not hold')