import random
import numpy as np
import matplotlib.pyplot as plt
import math

def randpath(tt):
    b=[]
    bb=[]
    b.append(0)
    bb.append(0)
    b2=[]
    for i in range(tt):
        c=random.random()
        bb.append(i+1)
        if c<=0.5:
           b.append(b[-1]+1)
        else:
           b.append(b[-1]-1)
    for j in range(len(b)):
        b2.append(b[j])
    return b,bb,b2
a,b,c=randpath(1000)
a1,b1,c1=randpath(1000)

def randpath(pp):
    y=[]
    yy=[]
    y.append(0)
    yy.append(0)
    y2=[]
    for i in range(pp):
        z=random.random()
        yy.append(i+1)
        if z<=0.5:
           y.append(y[-1]+1)
        else:
           y.append(y[-1]-1)
    for j in range(len(b)):
        y2.append(y[j])
    return y,yy,y2
x,y,z=randpath(1000)
x1,y1,z1=randpath(1000)

def randpath(pp):
    l=[]
    ll=[]
    l.append(0)
    ll.append(0)
    l2=[]
    for i in range(pp):
        m=random.random()
        ll.append(i+1)
        if m<=0.5:
           l.append(l[-1]+1)
        else:
           l.append(l[-1]-1)
    for j in range(len(b)):
        l2.append(l[j])
    return l,ll,l2
n,l,m=randpath(1000)
n1,l1,m1=randpath(1000)

def randpath(pp):
    s=[]
    ss=[]
    s.append(0)
    ss.append(0)
    s2=[]
    for i in range(pp):
        t=random.random()
        ss.append(i+1)
        if t<=0.5:
           s.append(s[-1]+1)
        else:
           s.append(s[-1]-1)
    for j in range(len(b)):
        s2.append(s[j])
    return s,ss,s2
r,s,t=randpath(1000)
r1,s1,t1=randpath(1000)

fig = plt.figure(figsize=[12,9])
plt.subplot(2,2,1)
for k in range(len(b)):
    plt.scatter([b[k]],[c[k]],1,color='blue')
    plt.scatter([b1[k]],[c1[k]],1,color='red')
plt.xlim(0,1000)
plt.ylim(-50,50)
plt.xlabel('step number')
plt.ylabel('X')

plt.subplot(2,2,2)
for k in range(len(b)):
    plt.scatter([y[k]],[z[k]],1,color='blue')
    plt.scatter([y1[k]],[z1[k]],1,color='red')
plt.xlim(0,1000)
plt.ylim(-50,50)
plt.xlabel('step number')
plt.ylabel('X')

plt.subplot(2,2,3)
for k in range(len(b)):
    plt.scatter([l[k]],[m[k]],1,color='blue')
    plt.scatter([l1[k]],[m1[k]],1,color='red')
plt.xlim(0,1000)
plt.ylim(-50,50)
plt.xlabel('step number')
plt.ylabel('X')

plt.subplot(2,2,4)
for k in range(len(b)):
    plt.scatter([s[k]],[r[k]],1,color='blue')
    plt.scatter([s1[k]],[r1[k]],1,color='red')
plt.xlim(0,1000)
plt.ylim(-50,50)
plt.xlabel('step number')
plt.ylabel('X')
plt.show()
