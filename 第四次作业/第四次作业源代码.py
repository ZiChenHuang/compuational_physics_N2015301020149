import numpy as np
import matplotlib.pyplot as plt  #to import matplotlib's package

N=[]            #population
t=[]            #time
a=10            #assign a value to a
b=0.01          #assign a value to b
det_t=0.001     #time step
N.append(1)     #assign a value to first item of v[]
t.append(0)     #assign a value to first item of t[]
end_time=2      #total time

for i in range(int(end_time/det_t)):
    tmp=N[i]+(a*N[i]-b*N[i]**2)*det_t   #Euler method
    N.append(tmp)                       #add new value of v to v[]
    t.append(det_t*(i+1))               #add new value of t to t[]
    print(t[-1],N[-1])                  #print the value of v and t on each stap)

plt.figure(figsize=(12,9))                                  #set the size of corresponding figure
plt.plot(t,N,label="population",color="red",linewidth=1.2) #plot the figure and set label and color and linewidth of the figure
plt.xlabel("time")             #set the label of x axis
plt.ylabel("Population")       #set the label of y axis
plt.title("Population") #set title
plt.ylim(0,2000)               #set the range of y axis
plt.xlim(0,1.7)                #set the range of x axis
plt.legend()                   #make it to show everything
plt.show()                     #activate