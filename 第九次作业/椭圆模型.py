import math
import matplotlib.pyplot as plt
x_0=-4
y_0=0
Q=36.87*math.pi/180
v_x_0=1*math.cos(Q)
v_y_0=1*math.sin(Q)
dt=0.001
end_t=4000
x=[]
y=[]
v_x=[]
v_y=[]
t=[]
v_x_1=[]
x_1_1=[]
x.append(x_0)
y.append(y_0)
v_x.append(v_x_0)
v_y.append(v_y_0)
t.append(0)

for i in range(int(end_t/dt)):
    x.append(x[i]+v_x[i]*dt)
    y.append(y[i]+v_y[i]*dt)
    v_x.append(v_x[i])
    v_y.append(v_y[i])
    t.append(t[i]+dt)
    #print(x[-1],y[-1])
    #print x[i]**2+y[i]**2
    if  (((x[i+1]-4)**2+y[i+1]**2)**0.5+((x[i+1]+4)**2+y[i+1]**2)**0.5)>10:
        while abs((((x[i+1]-4)**2+y[i+1]**2)**0.5+((x[i+1]+4)**2+y[i+1]**2)**0.5)-10)>0.001:
              #print abs(x[i+1]**2+y[i+1]**2-4) 
              X=(x[i]+x[i+1])/2
              Y=(y[i]+y[i+1])/2
              p=(X*9)/(Y*25)
              if p>0:
               a=(p**2/(1+p**2))**0.5
               b=(1/(1+p**2))**0.5
               v_x[i+1]=(1-2*a**2)*v_x[i]-2*a*b*v_y[i]
               v_y[i+1]=(1-2*b**2)*v_y[i]-2*a*b*v_x[i]
              elif p<=0:
               a=(p**2/(1+p**2))**0.5
               b=-((1/(1+p**2))**0.5)
               v_x[i+1]=(1-2*a**2)*v_x[i]-2*a*b*v_y[i]
               v_y[i+1]=(1-2*b**2)*v_y[i]-2*a*b*v_x[i]
              #v_y[i+1]=-((2.0*a**3-2.0*a)/b)*v_x[i+1]-(2*a**2-1)*v_y[i+1]
              if (((X-4)**2+Y**2)**0.5+((X+4)**2+Y**2)**0.5)>10:
                 x[i+1]=X
                 y[i+1]=Y
                 continue
              else:
                 x[i]=X
                 y[i]=Y
                 continue
    if abs(y[i]-0)<0.0001:
       p=x[i]
       q=v_x[i]
       v_x_1.append(q)
       x_1_1.append(p)

x_1=[-5]
y_1=[0]
x_2=[-5]
y_2=[0]
dx=0.01
for j in range(1000):
    x_1.append(x_1[j]+dx)
    y_1.append((9-(9/25*x_1[j+1]**2))**0.5)
    x_2.append(x_1[j]+dx)
    y_2.append(-(9-(9/25*x_1[j+1]**2))**0.5)
    
fig= plt.figure(figsize=(15,9))
#fig= plt.figure(figsize=(7,6))
#plt.scatter(x_1_1,v_x_1,marker='+',color='b',label='phase space plot')
#plt.plot(x,y,'-' ,label='orbit',linewidth=1)
#plt.plot(x_1,y_1,'-',color="orange",label='bianary')
#plt.plot(x_2,y_2,'-',color="orange")
#plt.plot(-4,0,'*' ,color="r",label='focus')
#plt.plot(4,0,'*' ,color="r")
plt.scatter(x_1_1,v_x_1,marker='+',color='b',label='phase space plot')
plt.title(u'phase space plot under ellipse,$\Theta=36.9°$',fontsize=16) 
plt.xlabel(u'x',fontsize=18)
plt.ylabel(u'$v_x$',fontsize=18)
plt.ylim(-4,4)               
plt.xlim(-7.5,7.5)  
plt.legend(fontsize=12,loc='best')
plt.show(fig)