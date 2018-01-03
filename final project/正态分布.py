import random
import numpy as np
import matplotlib.pyplot as plt
import math
N=1000
def randpath(n,tt):
    b=[]
    bb=[]
    bb1=[]
    for i in range(1,2*n):
        b.append(-n+i)
        bb.append(0)
        if i==n:
           bb1.append(n)
        else:
           bb1.append(0)
    for j in range(n):
        x=[]
        x.append(0) 
        for k in range(tt):   
            c=random.random()
            if c<=0.5:
               x.append(x[-1]+1)
            if c>0.5:
               x.append(x[-1]-1)
        ct=b.index(x[-1])
        bb[ct]=bb[ct]+1/n
    if tt==0:
       return b,bb1
    else:
       return b,bb    
   
x1=[-100];y1=[-100]
x2=[-100];y2=[-100]
x3=[-100];y3=[-100]
x4=[-100];y4=[-100]
end_time=200;dt=0.01
for i in range(int(end_time/dt)):
    y1.append(2*0.0398942*(math.exp(-(1/200)*(x1[i]**2))))
    x1.append(x1[i]+dt)
for i in range(int(end_time/dt)):
    y2.append(2*0.0230329*(math.exp(-(1/600)*(x2[i]**2))))
    x2.append(x2[i]+dt)
for i in range(int(end_time/dt)):
    y3.append(2*0.01261566*(math.exp(-(1/2000)*(x3[i]**2))))
    x3.append(x3[i]+dt)
for i in range(int(end_time/dt)):
    y4.append(2*0.0089206*(math.exp(-(1/4000)*(x4[i]**2))))
    x4.append(x4[i]+dt)
    
fig = plt.figure(figsize=[15,10]) 

plt.subplot(221)      
a,b=randpath(5000,100)
plt.plot(a,b)
plt.plot(x1,y1,color='red',label='S=100',linewidth=1.5)
plt.xlim(-100,100)
plt.ylim(0,0.08)
plt.xlabel('X',fontsize=15)
plt.ylabel('Probability density',fontsize=15)
plt.legend(loc='upper right',fontsize=16)

plt.subplot(222) 
a,b=randpath(10000,300)
plt.plot(a,b)
plt.plot(x2,y2,color='red',label='S=300',linewidth=1.5)
plt.xlim(-100,100)
plt.ylim(0,0.08)
plt.xlabel('X',fontsize=15)
plt.ylabel('Probability density',fontsize=15)
plt.legend(loc='upper right',fontsize=16)

plt.subplot(223) 
a,b=randpath(5000,1000)
plt.plot(a,b)
plt.plot(x3,y3,color='red',label='S=1000',linewidth=1.5)
plt.xlim(-100,100)
plt.ylim(0,0.08)
plt.xlabel('X',fontsize=15)
plt.ylabel('Probability density',fontsize=15)
plt.legend(loc='upper right',fontsize=16)

plt.subplot(224) 
a,b=randpath(5000,2000)
plt.plot(a,b)
plt.plot(x4,y4,color='red',label='S=2000',linewidth=1.5)
plt.xlim(-100,100)
plt.ylim(0,0.08)
plt.xlabel('X',fontsize=15)
plt.ylabel('Probability density',fontsize=15)
plt.legend(loc='upper right',fontsize=16)

plt.show()