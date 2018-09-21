# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 13:15:22 2018

@author: gyojh
"""


# arrays


import numpy as np
a = np.array([[1,2],[3,4]])
print(a)

#ask for the shape of the erray
print(np.shape(a))
#ask for the size of the erray
print(np.size(a))

#find the range of the erray
b = np.array(range(20))
#re size the erray shape
print(b.reshape(4,5))

# numpy arrays are mutable like lists
# numpy has aeange which is like range but for real numbers

print(np.arange(1.1,2.5,0.2))

#slicing as for lists but better

a = np.arange(0,15)
print(a[3-6])
#this below will print numbers 12 down to 6 with a diference of one
print(a[12:5:-1])
# 13-5 with a difference of 2
print(a[13:4:-2])




# control flow

x= 11
#if 
if x<10:
    print('yes')
 
    
    
    
# while
n = 10
tr = 0

while n>0:
    tr += n
    n -= 1
print (tr)


for i in range(10):
    print(i**2+i+1)
    
for _ in range(5):
    print('rob')
    
for a in [4,6,2,4,8]:
    for b in "rob":
        print(a,b)
        
        

        
        