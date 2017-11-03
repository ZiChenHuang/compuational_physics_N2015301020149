import math
import matplotlib.pyplot as plt

x=[]
xa=[]
y=[]
ya=[]
z=[]
za=[];zb=[]
t=[]
x.append(1)
y.append(0)
z.append(0)
xa.append(1)
ya.append(0)
za.append(0)
zb.append(0)
t.append(0)
end_time=3000
dt=0.001 
a=10
b=8/3
r=30

for i in range(int(end_time/dt)):
    x.append(x[i]+a*(y[i]-x[i])*dt)
    y.append(y[i]+(-x[i]*z[i]+r*x[i]-y[i])*dt)
    z.append(z[i]+(x[i]*y[i]-b*z[i])*dt)
    t.append(t[i]+dt)
    if abs(x[i])<0.01:
        ya.append(y[i])
        za.append(z[i])
    else:
        pass
    
plt.figure(figsize=(12,9))                                  
#plt.plot(t,z,label="$\Theta$",color="r",linewidth=1.5)
#plt.plot(x,z,label="$\Theta$",color="r",linewidth=1.5)
plt.plot(ya,za,',',color="black")
plt.xlabel("Y(density)",fontsize=18)             
plt.ylabel("Z(velocity)",fontsize=18)       
plt.title("Z versus Y when X=0, r=30",fontsize=18) 
plt.ylim(5,40)               
plt.xlim(-12,12)                
plt.legend(loc='upper right',fontsize=15)                  
plt.show()  