import math
import matplotlib.pyplot as plt
x_0=1.2
y_0=0
Q=45*math.pi/180
v_x_0=1*math.cos(Q)
v_y_0=1*math.sin(Q)
dt=0.001
end_t=3000
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
    #print x[i]**2+y[i]**2
    if  x[i+1]**2+y[i+1]**2>4:
        while abs(x[i+1]**2+y[i+1]**2-4)>0.001:
              #print abs(x[i+1]**2+y[i+1]**2-4) 
              X=(x[i]+x[i+1])/2
              Y=(y[i]+y[i+1])/2
              a=X/(X**2+Y**2)**0.5
              b=Y/(X**2+Y**2)**0.5
              v_x[i+1]=(1-2*a**2)*v_x[i]-2*a*b*v_y[i]
              v_y[i+1]=(1-2*b**2)*v_y[i]-2*a*b*v_x[i]
              #v_y[i+1]=-((2.0*a**3-2.0*a)/b)*v_x[i+1]-(2*a**2-1)*v_y[i+1]
              if X**2+Y**2>4:
                 x[i+1]=X
                 y[i+1]=Y
                 continue
              else:
                 x[i]=X
                 y[i]=Y
                 continue
    if  x[i+1]**2+y[i+1]**2<1:
        while abs(x[i+1]**2+y[i+1]**2-1)>0.001:
              X=(x[i]+x[i+1])/2
              Y=(y[i]+y[i+1])/2
              a=X/(X**2+Y**2)**0.5
              b=Y/(X**2+Y**2)**0.5
              v_x[i+1]=(1-2*a**2)*v_x[i]-2*a*b*v_y[i]
              v_y[i+1]=(1-2*b**2)*v_y[i]-2*a*b*v_x[i]
              if X**2+Y**2<1:
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
x_1=[-1]
y_1=[0]
x_2=[-1]
y_2=[0]
x_3=[-2]
y_3=[0]
x_4=[-2]
y_4=[0]
dx=0.0001
for j in range(20000):
    x_1.append(x_1[j]+dx)
    y_1.append((1-x_1[j+1]**2)**0.5)
    x_2.append(x_1[j]+dx)
    y_2.append(-(1-x_1[j+1]**2)**0.5)
for k in range(40000):
    x_3.append(x_3[k]+dx)
    y_3.append((4-x_3[k+1]**2)**0.5)
    x_4.append(x_4[k]+dx)
    y_4.append(-(4-x_4[k+1]**2)**0.5)
    
fig= plt.figure(figsize=(12,12))
#plt.scatter(x_1_1,v_x_1,marker='+',color='b',label='phase space plot')
#plt.plot(x,y,'--',label='orbit')
#plt.plot(x_1,y_1,'-',color="orange",label='binary')
#plt.plot(x_2,y_2,'-',color="orange")
#plt.plot(x_3,y_3,'-',color="orange")
#plt.plot(x_4,y_4,'-',color="orange")
plt.scatter(x_1_1,v_x_1,marker='+',color='b',label='phase space plot')
plt.title(u'phase space plot under concentric circles',fontsize=18) 
plt.xlabel(u'x',fontsize=18)
plt.ylabel(u'y',fontsize=18)
plt.ylim(-1.2,1.2)               
plt.xlim(-4.5,4.5)  
plt.legend(fontsize=12,loc='best')
plt.show(fig)