
import matplotlib.pyplot as plt
import math  

w=[] 
vw=[]  
cw=[]         
t=[]   
Ek=[] 
Ep=[]
E=[]                   
a=1            
b=0.5
c=2/3
fd=1  
dt=0.01 
pi=math.pi    
w.append(0.2)     
vw.append(0)
cw.append(0)
t.append(0)   
Ek.append(0) 
Ep.append(0)
E.append(0)
end_time=100      

for i in range(int(end_time/dt)):
    Ek.append(0.5*vw[i]**2*9.8**2)
    Ep.append(9.8*(1-math.cos(w[i]))*9.8)
    E.append(Ek[i]+Ep[i])
    vw.append(vw[i]+(-math.sin(w[i])-0.5*vw[i]+fd*math.sin(t[i]*2/3))*dt)  
    cw.append(w[i]+vw[i+1]*dt)                      
    if cw[i+1]<-pi:        
            w.append(cw[i+1]+2*pi)
    elif cw[i+1]>pi:
            w.append(cw[i+1]-2*pi)
    else:
            w.append(cw[i+1])   
    t.append(t[i]+dt)  
    print(w[-1],t[-1])                  

plt.figure(figsize=(12,9))                                  
#plt.plot(t,Ek,label="kinetic energy",color="r",linewidth=1.2)
#plt.plot(t,Ep,label="Potential energy",color="b",linewidth=1.2)
#plt.plot(t,E,label="Total energy",color="g",linewidth=1.8)
plt.plot(t,w,label="$\Theta$",color="r",linewidth=1.5)
plt.xlabel("time(s)",fontsize=18)             
plt.ylabel("Energy(J)",fontsize=18)       
plt.title("Energy versus $time$,Fd=1.2",fontsize=18) 
plt.ylim(-5,5)               
plt.xlim(0,100)                
plt.legend(loc='upper right',fontsize=15)                  
plt.show()                     