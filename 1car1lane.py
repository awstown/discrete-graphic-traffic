#This code defines two objects, a Car and a Lane, then creates
#an instance of each of those objects, then adds the car to the
#lane, then moves the car along the lane at a constant, user-
#defined velocity. To represent the lane visually, I have the
#terminal print an 'n' to represent where the car is on a lane
#of underscores. Each line printed represents a single moment
#in time.

import Tkinter as tk
root = tk.Tk()
root.title("Traffic Simulation")
canvas = tk.Canvas(root, width =1000,height=300, bg="#FFFFFF")

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

length = 10
vel = 1
lane = Lane(length)
toyota = Car(0, vel)
lane.add_car(toyota)
a=[]
t=[]
for i in range(19):
	print lane
   	lane.update_all()
	a.append(toyota.position)
	t.append(i)
	
print a
print t

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
plt.show()



#root.mainloop()
