from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

steps = np.linspace(0, 1000, 1001)
x_ave = np.zeros(1001)
y_ave = np.zeros(1001)
z_ave = np.zeros(1001)
x_y0 = np.zeros(1001)
a=10000
b=1000
c=300
x_now = np.zeros(a)
y_now = np.zeros(a)
z_now = np.zeros(a)

for i in range(1000):
    for j in range(a):
        ruler = np.random.rand()
        if ruler<=0.5:
            x_now[j] = x_now[j] + 1
        else:
            x_now[j] = x_now[j] - 1
    average = sum(x_now)/a
    x_ave[i+1] = average
    
for i in range(1000):
    for j in range(b):
        ruler = np.random.rand()
        if ruler<=0.5:
            y_now[j] = y_now[j] + 1
        else:
            y_now[j] = y_now[j] - 1
    average = sum(y_now)/b
    y_ave[i+1] = average
    
for i in range(1000):
    for j in range(c):
        ruler = np.random.rand()
        if ruler<=0.5:
            z_now[j] = z_now[j] + 1
        else:
            z_now[j] = z_now[j] - 1
    average = sum(z_now)/c
    z_ave[i+1] = average
    
fig = plt.figure(figsize=[12,9])    
plt.plot(steps, x_ave,'orange',label='5000 walkers')
plt.plot(steps, y_ave,'green',label='1000 walkers')
plt.plot(steps, z_ave,'blue',label='500 walkers')
plt.plot(steps, x_y0,'black',linewidth=1)
plt.xlim(0,1000)
plt.ylim(-5,5)
plt.xlabel('step number',fontsize=15)
plt.ylabel('$\overline{X}$',fontsize=15)
plt.title('$\overline{X}$ of walkers',fontsize=18)
plt.legend(loc='upper right',fontsize=15)
plt.show()