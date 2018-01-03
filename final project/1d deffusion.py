import pylab as plt
import numpy as np 

N=101
dx=2./(N-1)
dt=0.1
D=1./4*(dx**2)/dt

class diffusion:
 	def __init__(self,step):
 		self.step=step
 		self.x=np.linspace(-1,1,N)
 		self.y=np.linspace(0,0,N)
 		self.old_y=np.linspace(0,0,N)
 		self.y[50]=1

 	def update(self):
 		for i in range(N):
 			self.old_y[i]=self.y[i]

 		for i in range(1,N-1):
 			self.y[i]=self.old_y[i]+D*dt/(dx**2)*(self.old_y[i+1]+self.old_y[i-1]-2*self.old_y[i])

 	def fire(self):
 		for i in range(self.step):
 			self.update()
 			i+=1

 		plt.plot(self.x,self.y,label="step="+str(self.step))

fig = plt.figure(figsize=[15,9])   

A=diffusion(10)
A.fire()
A=diffusion(30)
A.fire()
A=diffusion(100)
A.fire()
A=diffusion(500)
A.fire()
plt.xlabel('X',fontsize=18)
plt.ylabel('density',fontsize=18)
plt.title('Diffusion in one dimension',fontsize=18)
plt.legend(loc='upper right',fontsize=15)
plt.ylim(0,0.180)
plt.xlim(-1,1)
plt.show()