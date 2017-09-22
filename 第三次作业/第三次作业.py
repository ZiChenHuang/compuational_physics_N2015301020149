import os
import time;

def printA():
    count1=0
    count2=0
    Str=''
    while count1<30:
        time_start=time.time()
        while count2<count1:
            Str+=' '
            count2=count2+1
        Str+='»Æè÷å·'
        count1=count1+1
        count2=0
        print (Str)
        time_end=time.time()
        while time_end-time_start<1:
                time_end=time.time()
                
        i=os.system('cls')
        Str=''