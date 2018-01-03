from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import random

N=100
accuracy=1e-10
class Fields:
	def __init__(self):
		self.v=[]
		self.old_v=[]
		for i in range(N):
			self.v.append([])
			self.old_v.append([])

		#print len(self.old_v)

		for i in range(N):
			for j in range(N):
				self.v[i].append(0)
				self.old_v[i].append(0)

		for i in range(25,50):
			for j in range(25,50):
				self.v[i][j]=1
                
		for i in range(50,75):
			for j in range(50,75):
				self.v[i][j]=1

	def update(self):
		self.Delta_v=0.
		for i in range(N):
			self.v[i][0]=0
			self.v[i][N-1]=0

		for j in range(N):
			self.v[0][j]=0
			self.v[N-1][j]=0

		for i in range(N):
			for j in range(N):
				self.old_v[i][j]=self.v[i][j]


		for i in range(1,N-1):
			for j in range(1,N-1):
				self.v[i][j]=(self.old_v[i+1][j]+self.old_v[i-1][j]+self.old_v[i][j+1]+self.old_v[i][j-1])/4.

		#print self.Delta_v

	def fire(self):
		counter=0
		for i in range(500):
			self.update()
			counter+=1
			i+=1

		return self.v


Super=Fields()
Soup=Super.fire()

fig = plt.figure(figsize=[10,5])
ax = fig.gca(projection='3d')
x=np.linspace(-1,1,N)
y=np.linspace(-1,1,N)
x, y = np.meshgrid(x, y)
surf = ax.plot_surface(x, y, Soup, rstride=1, cstride=1, cmap='coolwarm',linewidth=0, antialiased=False)
ax.set_zlim(0, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
#plt.xlabel("X",fontsize=16)
#plt.ylabel("Y",fontsize=16)
#ax.set_zlabel('density',fontsize=16)
ax.set_title('step=500',fontsize=18)
plt.show()