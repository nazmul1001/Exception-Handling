#Multi Threading. We want to exceute the two process simultaneousely by assigning this two process in different core.
from time import sleep
from threading import *
 
class Hello(Thread):
    def run(self): #Run is in-built method of start
        for i in range(500):
            print("Hello")
            sleep(1)

            
class Hi(Thread):
    def run(self): #Run is in-built method of start
        for i in range(500): 
            print("Hi")
            sleep(1)

t1=Hello()
t2=Hi()

t1.start() #Start is method of Thread and run is a method of start
sleep(0.2) # To avoid collision we used sleep here.
t2.start()#Start is method of Thread and run is a method of start

