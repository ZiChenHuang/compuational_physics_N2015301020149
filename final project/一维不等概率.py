from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

steps = np.linspace(0, 100, 101)

x_ave = np.zeros(101)
y_ave = np.zeros(101)
z_ave = np.zeros(101)
x_now = np.zeros(200)
y_now = np.zeros(200)
z_now = np.zeros(200)

x2_ave = np.zeros(101)
y2_ave = np.zeros(101)
z2_ave = np.zeros(101)
x1_now = np.zeros(200)
y1_now = np.zeros(200)
z1_now = np.zeros(200)
x2_now = np.zeros(200)
y2_now = np.zeros(200)
z2_now = np.zeros(200)

for i in range(100):
    for j in range(200):
        ruler = np.random.rand()
        if ruler<=0.5:
            x_now[j] = x_now[j] + 1
        else:
            x_now[j] = x_now[j] - 1
    average = sum(x_now)/200
    x_ave[i+1] = average
    
for i in range(100):
    for j in range(200):
        ruler2 = np.random.rand()
        if ruler2<=0.75:
            y_now[j] = y_now[j] + 1
        else:
            y_now[j] = y_now[j] - 1
    average = sum(y_now)/200
    y_ave[i+1] = average
 
for i in range(100):
    for j in range(200):
        ruler3 = np.random.rand()
        if ruler3<=1:
            z_now[j] = z_now[j] + 1
        else:
            z_now[j] = z_now[j] - 1
    average = sum(z_now)/200
    z_ave[i+1] = average
     
for i in range(100):
    for j in range(200):
        ruler = np.random.rand()
        if ruler<=0.5:
            x1_now[j] = x1_now[j] + 1
        else:
            x1_now[j] = x1_now[j] - 1
        x2_now[j] = x1_now[j]**2
    average2 = sum(x2_now)/200
    x2_ave[i+1] = average2

for i in range(100):
    for j in range(200):
        ruler = np.random.rand()
        if ruler<=0.75:
            y1_now[j] = y1_now[j] + 1
        else:
            y1_now[j] = y1_now[j] - 1
        y2_now[j] = y1_now[j]**2
    average2 = sum(y2_now)/200
    y2_ave[i+1] = average2

for i in range(100):
    for j in range(200):
        ruler = np.random.rand()
        if ruler<=1:
            z1_now[j] = z1_now[j] + 1
        else:
            z1_now[j] = z1_now[j] - 1
        z2_now[j] = z1_now[j]**2
    average2 = sum(z2_now)/200
    z2_ave[i+1] = average2    
    
ay=[0];by=[0];cy=[0]    
ax=[0];bx=[0];cx=[0] 
end_time=40;dt=0.01      
for i in range(int(end_time/dt)):
    ay.append(0.25*(ax[i]**2)+0.75*ax[i])
    ax.append(ax[i]+dt)
    by.append(bx[i])
    bx.append(bx[i]+dt)
    cy.append(cx[i]**2)
    cx.append(cx[i]+dt)

fig = plt.figure(figsize=[20,9])  
plt.subplot(1,2,1)  
plt.scatter(steps, x_ave,label='$P_{x+1}=0.5$',s=13,color='royalblue')
plt.scatter(steps, y_ave,label='$P_{x+1}=0.75$',s=13,color='limegreen')
plt.scatter(steps, z_ave,label='$P_{x+1}=1$',s=13,color='r')
plt.legend(loc='upper left',fontsize=13)
plt.xlim(0,40)
plt.ylim(-1,40)
plt.xlabel('step number',fontsize=15)
plt.ylabel('$\overline{X}$',fontsize=15)
plt.title('$\overline{X}$ of 200 walkers',fontsize=18)
#plt.legend(loc='upper right',fontsize=15)
plt.subplot(1,2,2)
plt.scatter(steps, x2_ave,label='$P_{x+1}=0.5$',s=15,color='royalblue')
plt.scatter(steps, y2_ave,label='$P_{x+1}=0.75$',s=15,color='limegreen')
plt.scatter(steps, z2_ave,label='$P_{x+1}=1$',s=20,color='r')
plt.legend(loc='upper left',fontsize=13)
plt.plot(ax,ay,color='dimgray',linewidth=1)
plt.plot(bx,by,color='dimgray',linewidth=1)
plt.plot(cx,cy,color='dimgray',linewidth=1)
plt.xlim(0,40)
plt.ylim(0,200)
plt.xlabel('step number',fontsize=15)
plt.ylabel('$\overline{X^{2}}$',fontsize=15)
plt.title('$\overline{X^{2}}$ of 200 walkers (with theoretical curve)',fontsize=18)
plt.show()