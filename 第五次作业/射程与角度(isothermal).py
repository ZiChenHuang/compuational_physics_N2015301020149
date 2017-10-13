import math
import matplotlib.pyplot as plt
x=[]
y=[]
vx=[]
vy=[]
g=9.8
A=4*10**(-5)
y0=10**4
dt=0.01

for theta in range(30,61):
    vx.append(700*math.cos(theta*math.pi/180))
    vy.append(700*math.sin(theta*math.pi/180))
    x.append(0.0)
    y.append(0.0)
    while y[-1]>=0.0:
      m=x[-1]+vx[-1]*dt
      n=y[-1]+vy[-1]*dt
      tvx=vx[-1]-A*math.e**(-y[-1]/y0)*(vx[-1]**2+vy[-1]**2)**0.5*vx[-1]*dt
      tvy=vy[-1]-A*math.e**(-y[-1]/y0)*(vx[-1]**2+vy[-1]**2)**0.5*vy[-1]*dt-g*dt
      x.append(m)
      vx.append(tvx)
      y.append(n)
      vy.append(tvy)
    
    print(theta,x[-1])
    
plt.figure(figsize=(8,6))
plt.plot(theta_list,x_list,'ro' , label="(shoot range)")
plt.xlabel("angle($^\circ$)",fontsize=18)
plt.ylabel("shoot range(m)",fontsize=18)
plt.title('Theta and shoot range in isothermal model',fontsize=18)
plt.legend(loc='upper right',fontsize=13)
plt.show()
