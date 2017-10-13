import math
import matplotlib.pyplot as plt
c=[]
d=[]
vc=[]
vd=[]
g=9.8
A=4*10**(-5)
y0=10**4
dt=0.001

for theta in range(30,61):
    vc.append(700*math.cos(theta*math.pi/180))
    vd.append(700*math.sin(theta*math.pi/180))
    c.append(0.0)
    d.append(0.0)
    while d[-1]>=0.0:
      m=c[-1]+vc[-1]*dt
      n=d[-1]+vd[-1]*dt
      tvc=vc[-1]-A*(1-6.5*10**(-3)*d[-1]/300)**2.5*(vc[-1]**2+vd[-1]**2)**0.5*vc[-1]*dt
      tvd=vd[-1]-A*(1-6.5*10**(-3)*d[-1]/300)**2.5*(vc[-1]**2+vd[-1]**2)**0.5*vd[-1]*dt-g*dt
      c.append(m)
      vc.append(tvc)
      d.append(n)
      vd.append(tvd)
    
    print(theta,c[-1])
    
plt.figure(figsize=(8,6))
plt.plot(theta_list,x_list,'ro' , label="(shoot range)")
plt.xlabel("angle($^\circ$)",fontsize=18)
plt.ylabel("shoot range(m)",fontsize=18)
plt.title('Theta and shoot range in adiabatic model',fontsize=18)
plt.legend(loc='upper right',fontsize=13)
plt.show()