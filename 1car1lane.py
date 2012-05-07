#This code defines two objects, a Car and a Lane, then creates
#an instance of each of those objects, then adds the car to the
#lane, then moves the car along the lane at a constant, user-
#defined velocity. To represent the lane visually, I have the
#terminal print an 'n' to represent where the car is on a lane
#of underscores. Each line printed represents a single moment
#in time.

#import Tkinter as tk
#import time
#root = tk.Tk()
#root.title("Traffic Simulation")
#canvas = tk.Canvas(root, width =1000,height=300)
#canvas.pack

class Car(object):
    def __init__(self, pos=0, vel=0):
        self.position = pos
        self.speed = vel
    def __str__(self):
        return 'Position: %d, Speed: %d' % (self.position, self.speed)

class Lane(object):
    def __init__(self, spaces=1):
        self.length = spaces
        self.map = []
        self.carlist = []
        for i in range(self.length):
            self.map.append('_')
    def __str__(self):
        return ' '.join(self.map)
    def add_car(self, car):
        if car not in self.carlist:
            self.carlist.append(car)
        self.map[car.position] = 'n'
    def update_all(self):
        for car in self.carlist:
            self.map[car.position] = '_'
            car.position += car.speed
            if car.position > self.length - 1:
                car.position = car.position - self.length
            self.map[car.position] = 'n'

length = 100
vel = 6
lane = Lane(length)
toyota = Car(0, vel)
lane.add_car(toyota)
duration = 20
a=[]
t=[]
for i in range(duration):
	a.append(toyota.position)
   	lane.update_all()
	t.append(i)
print a
#print t

##plotting the time graph

import matplotlib.pyplot as plt
import numpy as np
from numpy import *
from matplotlib import rc
import pylab
from pylab import * 
fig = plt.figure()
fig.subplots_adjust(bottom=0.2)
ax = fig.add_subplot(111)
delta =(1,2,3,4)
vf = (5,6,7,8)
plt.scatter(a,t,c='b',alpha=0.7,cmap=cm.Paired)
xlabel('position')
ylabel('time')
title('traffic')
#plt.show()

##visualization
from Tkinter import *
root = Tk()
import time
#import Tkinter
#import tkMessageBox

#root = Tkinter.Tk()
Height= 150
canvas = Canvas(root, bg="grey", height=Height, width=10*length)


canvas.create_line(0,Height/2,10*length,Height/2)
canvas.pack()


class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Play", command=self.moving)
        self.hi_there.pack(side=LEFT)

	self.restart = Button(frame, text="add", command=self.timeadd)
        self.restart.pack(side=LEFT)

    def moving(self):
	canvas.delete('mycar')
	blue_car = canvas.create_rectangle(0, 100, 10, 110, fill="blue",tags='mycar')
	for x in range(duration-1):
		time.sleep(0.25)
		x1,y1,x2,y2 = canvas.coords('mycar')
		if a[x+1] > a[x]:
			if x1 > 10*length:
				canvas.delete('mycar')
				blue_car = canvas.create_rectangle(0, 100, 10, 110, fill="blue",tags='mycar')
				canvas.update()
				x1,y1,x2,y2 = canvas.coords('mycar')
				print x1
			else:
                		veloc = 10*(a[x+1] - a[x])
				move('mycar',veloc,0)
				canvas.update()
				x1,y1,x2,y2 = canvas.coords('mycar')
				print x1
		else:
			veloc = length - a[x] + a[x+1]
			canvas.delete('mycar')
			blue_car = canvas.create_rectangle(0, 100, 10, 110, fill="blue",tags='mycar')
			move('mycar',10*a[x+1],0)
			x1,y1,x2,y2 = canvas.coords('mycar')
			print x1
		#time.sleep(0.025)
		#move('mycar',veloc,0)
		#canvas.update()
		#canvas.itemcget('mycar')
		#x1, y1, x2,y2 = canvas.coords('mycar')
		#if x1 > length:
		#	canvas.delete('mycar')
		#	blue_car = canvas.create_rectangle(0, 100, 10, 110, fill="blue",tags='mycar')
		#	move('mycar',x1-length-vel,0)
		#else:
		#	print x1
    def reset(self):
	canvas.delete('mycar')
	blue_car = canvas.create_rectangle(0, 100, 10, 110, fill="blue",tags='mycar')
    def timeadd(self):
	print 'this button does nothing'
	

def move(self,x,y):
	canvas.move(self,x,y)
blue_car = canvas.create_rectangle(0, 100, 10, 110, fill="blue",tags='mycar')
x1, y1, x2,y2 = canvas.coords('mycar')
#print x1
#print x2
app = App(root)
root.mainloop()

