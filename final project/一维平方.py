from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

steps = np.linspace(0, 100, 101)
x2_ave = np.zeros(101)
x_y0 = np.zeros(101)
x_now = np.zeros(5000)
x2_now = np.zeros(5000)
st=[0]
th=[0]
dt=0.01
end_time=100
for i in range(100):
    for j in range(5000):
        ruler = np.random.rand()
        if ruler<=0.5:
            x_now[j] = x_now[j] + 1
        else:
            x_now[j] = x_now[j] - 1
        x2_now[j] = x_now[j]**2
    average2 = sum(x2_now)/5000
    x2_ave[i+1] = average2
    
for i in range(int(end_time/dt)):
    th.append(st[i])
    st.append(st[i]+dt)
    
fig = plt.figure(figsize=[12,9])  
plt.plot(st,th,label='theoretical curve',color='red')
plt.scatter(steps, x2_ave,label='simulation point',color='black',s=8)
plt.legend(loc='upper left',fontsize=15)
plt.xlim(0,100)
plt.ylim(0,100)
plt.xlabel('step number',fontsize=15)
plt.ylabel('$\overline{X^{2}}$',fontsize=15)
plt.title('$\overline{X^{2}}$ of 1000 walkers',fontsize=15)

plt.show()