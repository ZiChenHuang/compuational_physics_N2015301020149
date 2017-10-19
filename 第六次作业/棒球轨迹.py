
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

x=[0]
y=[0]
z=[0]
vx=15
vy=15
vz=0
dt=0.01

a=[0]
b=[0]
c=[0]
va=15
vb=15
vc=0
dt=0.01
w=200*3.14159/3

i=0
while y[i]>=0:
    x.append(x[i]+vx*dt)
    y.append(y[i]+vy*dt)
    z.append(z[i]+vz*dt)
    v=(vx**2+vy**2+vz**2)**0.5
    ay=-9.8
    ax=-(0.0039+0.0058/(1+math.exp((v-35)/5)))*v*vx
    az=-4.1*10**(-4)*vx*w
    vx=vx+ax*dt
    vy=vy+ay*dt
    vz=vz+az*dt
    v=(vx**2+vy**2+vz**2)**0.5
    i=i+1

i=0
while b[i]>=0:
    a.append(a[i]+va*dt)
    b.append(b[i]+vb*dt)
    c.append(c[i]+vc*dt)
    v=(va**2+vb**2+vc**2)**0.5
    aa=-(0.0039+0.0058/(1+math.exp((v-35)/5)))*v*va
    ab=-9.8
    ac=0
    va=va+aa*dt
    vb=vb+ab*dt
    vc=vc+ac*dt
    v=(va**2+vb**2+vc**2)**0.5
    aa=-(0.0039+0.0058/(1+math.exp((v-35)/5)))*v*va
    ac=0
    i=i+1
    
fig = plt.figure(figsize=(14,9))
ax = Axes3D(fig)


plt.xlabel("x(m)",fontsize=18)
plt.ylabel("z(m)",fontsize=18)
ax.set_zlabel("y(m)",fontsize=18)
plt.title("trajectory of battedball",fontsize=18)
ax.set_zlim(0,10)
plt.ylim(-10,0.1)
plt.xlim(0,40)
ax.plot(x, z, y,label="trajectory with Magnusforce",color="green",linewidth=2)
ax.plot(a, c, b,label="trajectory without Magnusforce",color="red",linewidth=2)
ax.scatter(x[0],z[0],y[0],label="initial position",color="red")
ax.scatter(x[-1],z[-1],y[-1],label="final position 1",color="black")
ax.scatter(a[-1],c[-1],b[-1],label="final position 2",color="red")
plt.legend(loc='upper right',fontsize=12)
ax.view_init(elev=90, azim=0)   #elev指定z轴的倾斜角度（elevation angle），azim指定x-y平面的方位角（azimuth angle）。
plt.show()