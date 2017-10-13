import math
import matplotlib.pyplot as plt
dt=0.001
g=9.8
A=4*10**(-5)
y0=10**4
Q=45*math.pi/180
end_time = 200
x=[]
y=[]
vx=[]
vy=[]
a=[]
b=[]
va=[]
vb=[]
c=[]
d=[]
vc=[]
vd=[]
x.append(0)
y.append(0)
vx.append(700*math.cos(Q))
vy.append(700*math.sin(Q))
a.append(0)
b.append(0)
va.append(700*math.cos(Q))
vb.append(700*math.sin(Q))
c.append(0)
d.append(0)
vc.append(700*math.cos(Q))
vd.append(700*math.sin(Q))

for i in range(int(end_time/dt)):
    m=x[i]+vx[i]*dt
    n=y[i]+vy[i]*dt
    tvx=vx[i]-A*math.e**(-y[i]/y0)*(vx[i]**2+vy[i]**2)**0.5*vx[i]*dt
    tvy=vy[i]-A*math.e**(-y[i]/y0)*(vx[i]**2+vy[i]**2)**0.5*vy[i]*dt-g*dt
    x.append(m)
    vx.append(tvx)
    y.append(n)
    vy.append(tvy)
    if n <= 0 :
        		break
            
for i in range(int(end_time/dt)):
    m=a[i]+va[i]*dt
    n=b[i]+vb[i]*dt
    tva=va[i]
    tvb=vb[i]-g*dt
    a.append(m)
    va.append(tva)
    b.append(n)
    vb.append(tvb)
    if n <= 0 :
        		break
    
for i in range(int(end_time/dt)):
    m=c[i]+vc[i]*dt
    n=d[i]+vd[i]*dt
    tvc=vc[i]-A*(1-6.5*10**(-3)*d[i]/300)**2.5*(vc[i]**2+vd[i]**2)**0.5*vc[i]*dt
    tvd=vd[i]-A*(1-6.5*10**(-3)*d[i]/300)**2.5*(vc[i]**2+vd[i]**2)**0.5*vd[i]*dt-g*dt
    c.append(m)
    vc.append(tvc)
    d.append(n)
    vd.append(tvd)
    if n <= 0 :
        		break
            
print(x[-1],y[-1])
print(a[-1],b[-1])
print(c[-1],d[-1])
plt.figure(figsize=(12,9))
plt.title("Trajectory of cannon shell",fontsize=18)
plt.plot(a,b,label="$45^\circ$no airdrag",color="green",linewidth=2)
plt.plot(x,y,label="$45^\circ$isothermal",color="red",linewidth=2)
plt.plot(c,d,label="$45^\circ$adiabatic",color="blue",linewidth=2)
plt.xlabel("x(m)",fontsize=18)
plt.ylabel("y(m)",fontsize=18)
plt.ylim(0,15000)
plt.xlim(0,55000)
plt.legend(loc='upper right',fontsize=13)
plt.show()