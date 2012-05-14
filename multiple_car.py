# Defines the Car object and the Lane object. This was built assuming the movement of the cars would be handled by a 'rules' script.

import random
from Tkinter import *
root = Tk()
root.title("Traffic Simulation")
import time

class Car(object):
    """Defines a Car object with attributes position, speed, and g, where g is
reserved to store the number of empty spaces ahead of the car.
    """
    def __init__(self, position=0, speed=1):
        self.position = position
        self.speed = speed
        self.g = 0
    def __str__(self):
        return 'Position: %d, Speed: %d\nEmpty spaces ahead: %d' % (self.position, self.speed, self.g)
    def reset(self, position, speed):
        """A slightly more convenient way to set the position and speed simultaneously.
        """
        self.position = position
        self.speed = speed

class Lane(object):
    """Defines a Lane object with attributes length, map, and carlist.
    """
    def __init__(self, spaces=1):
        self.length = spaces
        self.map = []   # uses '_' to represent an empty space, 'n' to represent a space with a car in it.
        self.carlist = []
        for i in range(self.length):
            self.map.append('_')
    def __str__(self):
        return ' '.join(self.map)
    def add_car(self, car):
        """Adds the specified instance 'car' to the lane."""
        if car not in self.carlist:
            self.carlist.append(car)
        self.map_update()
    def remove_car(self, car):
        """Removes the specified instance 'car' from the lane."""
        if car in self.carlist:
            self.carlist.remove(car)
        self.map_update()
    def populate(self, n):
        """Adds n cars to the lane in random positions.
        """
        self.map_update()
        if n > self.map.count('_'):
            if self.map.count('_') == 1: ss = ''
            else: ss = 's'
            if n == 1: ns = ''
            else: ns = 's'
            raise ValueError('Tried to put %d car%s in a lane that has %d empty space%s.' % (n, ns, self.map.count('_'), ss))
        for i in range(n):
            x = random.randint(0, self.length - 1)
            while True:
                if self.map[x] == '_':
                    self.add_car(Car(x))
                    break
                else:
                    x = random.randint(0, self.length - 1)
            self.map_update()
    def map_update(self):
        """Updates the map list to reflect changes in car positions."""
        for spot in range(self.length):
            self.map[spot] = '_'
        for car in self.carlist:
            self.map[car.position] = 'n'
    def g_update_car(self, car):
        """Finds and sets the appropriate g value for a specific car instance.
        """
        self.map_update()
        if car.position != self.length - 1:
            n = car.position + 1
        else:
            n = 0
        count = 0
        while self.map[n] == '_':
            count += 1
            n += 1
            if n > self.length - 1:
                n = n - self.length
        car.g = count
    def g_update_all(self):
        """Finds and sets the appropriate g value for each car instance in the lane.
        """
        for car in self.carlist:
            self.g_update_car(car)
    def print_cars(self):
        """Displays information about each car in 'carlist'. May be useful for debugging, etc.
        """
        for car in self.carlist:
            print '\n', car, '\n' + '-'*27
    def car_positions(self):
        """Returns a list containing the position of each car in carlist."""
        l = []
        for car in self.carlist:
            l.append(car.position)
        return l
    def car_speeds(self):
        """Returns a list containing the speed of each car in carlist."""
        l = []
        for car in self.carlist:
            l.append(car.speed)
        return l
    def move_car(self, car):
        """Changes the position of a given car based on its speed attribute, making sure to loop to the beginning of the lane appropriately."""
        car.position += car.speed
        if car.position > self.length - 1:
            car.position -= self.length

color = ['snow','gainsboro','linen','moccasin','cornsilk','ivory','cornsilk','seashell','honeydew','azure','green','red','blue','turquoise','cyan','aquamarine','chartreuse','yellow','khaki','gold','goldenrod','sienna','peru','burlywood','beige','tan','chocolate','firebrick','orange','coral','tomato','salmon','pink','maroon','magenta','violet','plum','orchid','purple','thistle','slateblue1','royalblue1','lavenderblush1','skyblue1','SpringGreen2','DarkOliveGreen4','IndianRed1']


cars=['mycar0','mycar1','mycar2','mycar3','mycar4','mycar5','mycar6','mycar7','mycar8','mycar9','mycar10','mycar11','mycar12','mycar13','mycar14','mycar15','mycar16','mycar17','mycar18','mycar19','mycar20','mycar21','mycar22','mycar23','mycar24','mycar25','mycar26','mycar27','mycar28','mycar29','mycar30','mycar31','mycar32','mycar33','mycar34','mycar35','mycar36','mycar37','mycar38','mycar39','mycar40','mycar41','mycar42','mycar43','mycar44','mycar45','mycar46','mycar47','mycar48','mycar49','mycar50']

col =[]
numcar=[]
a5=[]
a3=[]
alist, blist, clist, dlist, elist, flist, glist, hlist, ilist, jlist = ([] for i in range(10))
thelist = [alist,blist,clist,dlist,elist,flist,glist,hlist,ilist,jlist]

class App:

    def __init__(self, root):
	self.length = 10
	self.lane= Lane(self.length)
	self.canvas = Canvas(root, bg="grey", height=100, width=self.length*10)
	self.canvas.pack()
	
	for i in range(1,self.length+1):
		self.canvas.create_line(i*10,0,i*10,100,dash=(3,6))
	
	frame = Frame(root)
	frame.pack()
	
	Label(frame, text="enter the number of cars:").pack(side=TOP)
	self.txt_ent = Entry(frame)
	self.txt_ent.pack()

	self.quit = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.quit.pack(side=LEFT)

	self.play = Button(frame, text="Play", command=self.moving)
        self.play.pack(side=LEFT)

	self.restart = Button(frame, text="Cars", command=self.adding)
        self.restart.pack(side=LEFT)

    def adding(self):
	if not self.txt_ent.get():
		print 'input a number into the blank field'
		return
	pos = self.lane.car_positions()
	if not pos:
		pass
	else:
		numcar.pop(0)
		while self.lane.car_positions():
			col.pop(0) 
			a = self.lane.carlist[0]
			self.lane.remove_car(a)
			for i in range(len(cars)):
				self.canvas.delete(cars[i])
			self.lane.map_update
		for i in range(len(pos)):   #code for resetting the big list
			#print thelist[i], 'the list'
			while thelist[i]:
				thelist[i].pop(0)
			#print thelist[i], 'the list after'
			#print thelist, 'the whole list'
	h=int(self.txt_ent.get())
	numcar.append(h)
	self.lane.populate(h)
	pos = self.lane.car_positions()
	a2 = [x * 10 for x in pos] 
	for i in range(h):
		rant = random.randint(0,len(color)-1)
		col.append(rant)
		self.canvas.create_rectangle(a2[i],50,a2[i]+10,60,fill=color[rant],tags=cars[i])
	#print col, 'prints the index for the color list'
	#car_object = self.lane.carlist
	#for i in range(h):
		#space = self.lane.map.index('n')
		#self.lane.map.insert(space,'_')
		#self.lane.map.remove('n')
		#x1,y1,x2,y2 = self.canvas.coords(cars[i])
		#thelist[i].append(car_object[i].position)
		#print x1
	#self.lane.map_update()
	#print self.lane.map
	#print self.lane.car_positions()
    	#car_object = self.lane.carlist
    	#print car_object[0].position #gets the position of a single car created
	#a5.append(car_object[0].position) #records the initial position
	#print a5
	#print alist
	#print blist
	#print clist

    def moving(self):
	if not numcar:
		print 'no cars added to lane'
		return
	print numcar, 'numcar'
	for k in range(numcar[0]):   #code for resetting the big list
			#print k, 'this is k'
			#print thelist[k], 'the list in moving'
			while thelist[k]:
				thelist[k].pop(0)
			#print thelist[k], 'the list after in moving '
			#print thelist, 'the whole list in moving'
	car_object = self.lane.carlist
	for w in range(numcar[0]): # puts the initial position back in
		thelist[w].append(car_object[w].position)
	#velocity = 10
	duration = 5
	print car_object
	for i in range(duration):
		time.sleep(0.5)
		#h=int(self.txt_ent.get())
		for j in range(numcar[0]):
			self.lane.move_car(car_object[j]) #this is the code for moving cars. will be replaced by rules
			thelist[j].append(car_object[j].position)
			if thelist[j][i+1] > thelist[j][i]:
				self.canvas.move(cars[j],10,0)
			else:
				self.canvas.delete(cars[j])
				self.canvas.create_rectangle(thelist[j][i+1],50,thelist[j][i+1]+10,60, fill=color[col[j]], tags=cars[j])
				
			#a5.append(car_object[0].position)
			#x1,y1,x2,y2 = self.canvas.coords(cars[i])
			#if thelist[i][j]*10+thelist[i][j+1]*10-thelist[i][j]*10 > self.length*10:
			#	self.canvas.delete(cars[i])
			#	self.canvas.create_rectangle(0,50,10,60, fill=color[col[i]], tags=cars[i])
			#elif thelist[i][j]*10+thelist[i][j+1]*10-thelist[i][j]*10 == self.length*10:
			#	self.canvas.delete(cars[i])
			#	self.canvas.create_rectangle(0,50,10,60, fill=color[col[i]], tags=cars[i])
			#else:
			#	self.canvas.move(cars[i],thelist[i][j+1]-thelist[i][j],0)
			#x1,y1,x2,y2 = self.canvas.coords(cars[i])
		#a3.append(x1) 
		self.canvas.update()
	print car_object[0].position,'end position'
	#print a5,#prints the actual map location of car
	#print a3 #prints the location of rectangle which represents car
	#print alist, 'youou'
	#print blist
	#print clist
	#print thelist[0][3]

    def reset(self):
	print 'this also does nothing'

app = App(root)
root.mainloop()