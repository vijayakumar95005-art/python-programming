a=[23,42,66]
b=[1,1,1]
c=[]
for i in range(len(a)):
    c.append(a[i]+b[i])
print(c)


import numpy as np
a=np.array(a)
b=np.array(b)
print(a+b)
