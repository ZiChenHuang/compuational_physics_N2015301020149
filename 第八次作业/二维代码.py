
import matplotlib.pyplot as plt

x1=[];x2=[];x3=[]
y1=[];y2=[];y3=[]
z1=[];z2=[];z3=[]
t1=[];t2=[];t3=[]
x1.append(1);x2.append(1);x3.append(1)
y1.append(0);y2.append(0);y3.append(0)
z1.append(0);z2.append(0);z3.append(0)
t1.append(0);t2.append(0);t3.append(0)
end_time=100
dt=0.0001 
a=10
b=8/3
r1=160;r2=22;r3=10

for i in range(int(end_time/dt)):
    x1.append(x1[i]+a*(y1[i]-x1[i])*dt)
    y1.append(y1[i]+(-x1[i]*z1[i]+r1*x1[i]-y1[i])*dt)
    z1.append(z1[i]+(x1[i]*y1[i]-b*z1[i])*dt)
    t1.append(t1[i]+dt)

#for i in range(int(end_time/dt)):
    x2.append(x2[i]+a*(y2[i]-x2[i])*dt)
    y2.append(y2[i]+(-x2[i]*z2[i]+r2*x2[i]-y2[i])*dt)
    z2.append(z2[i]+(x2[i]*y2[i]-b*z2[i])*dt)
    t2.append(t2[i]+dt)
    
#for i in range(int(end_time/dt)):
    x3.append(x3[i]+a*(y3[i]-x3[i])*dt)
    y3.append(y3[i]+(-x3[i]*z3[i]+r3*x3[i]-y3[i])*dt)
    z3.append(z3[i]+(x3[i]*y3[i]-b*z3[i])*dt)
    t3.append(t3[i]+dt)
    
plt.figure(figsize=(12,9))                                  
#plt.plot(t1,z1,label="r=164",color="y",linewidth=1.2)
#plt.plot(t2,z2,label="r=22",color="g",linewidth=1.5)
#plt.plot(t3,z3,label="r=10",color="b",linewidth=1.5)
plt.plot(x1,z1,color="r",label='r=160',linewidth=1.5)
plt.xlabel("X(temperature)",fontsize=18)             
plt.ylabel("Z(velocity)",fontsize=18)       
plt.title("Phase space plot: Z versus X",fontsize=18) 
plt.ylim(0,325)               
plt.xlim(-60,75)                
plt.legend(loc='upper right',fontsize=15)                  
plt.show()         