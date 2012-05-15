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
    def __init__(self, position=0, speed=0):
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
            
class Data(object):
    """A data-holding object which contains histories of each car's position and speed as well as the length of the lane and the number of cars on the lane."""
    def __init__(self):
        self.position_history = []
        self.speed_history = []
        self.lane_length = 0
        self.number_of_cars = 0
    def build_position_history(self, lane):
        for car in lane.carlist:
            self.position_history.append([])
    def append_position_history(self, lane):
        for i in range(len(lane.carlist)):
            self.position_history[i].append(lane.carlist[i].position)
    def build_speed_history(self, lane):
        for car in lane.carlist:
            self.speed_history.append([])
    def append_speed_history(self, lane):
        for i in range(len(lane.carlist)):
            self.speed_history[i].append(lane.carlist[i].speed)
    def update_length(self, lane):
        self.lane_length = lane.length
    def update_number(self, lane):
        self.number_of_cars = len(lane.carlist)

class Rule(object):
    def update_and_move(car, lane, vmax, p, cc):
	if car.speed > car.g:
        	car.speed = car.g
    	if car.speed < car.g and car.speed < vmax:
        	car.speed += 1
    	if car.speed == vmax and cc:
        	prob = 0
    	else:
        	prob = p
    	if car.speed > 0 and to.random.randint(1, 100) <= 100*prob:
        	car.speed -= 1
    	lane.move_car(car)

    def stca(data, lane, vmax, n=10, p=0.50, cc=False):
    	data.build_position_history(lane)
    	data.build_speed_history(lane)
    	data.update_length(lane)
    	data.update_number(lane)
    	biglist = []
    	for j in range(len(lane.carlist)):
		biglist.append([]) #use this code to create biglist
    	for i in range(n):
        	lane.g_update_all()
        	for car in lane.carlist:
        	    update_and_move(car, lane, vmax, p, cc)
		#print lane.carlist
		for k in range(len(lane.carlist)):
			biglist[k].append(lane.carlist[k].position)
        	#this is where you want to grab data for graphs, animation, etc.
        	data.append_position_history(lane)
        	data.append_speed_history(lane)
    	lane.g_update_all()
    	l = biglist
    	return biglist
    
    def ca184(data, lane, vmax, n=10, cc=False):
    	"""Use the CA184 model to simulate the specified lane for 'n' discrete steps with a speed limit of 'vmax' (measured in discrete steps). Setting argument 'cc' to 'True' activates Cruise Control mode. 'data' refers to the data-holding object that will store the simulation's data."""
    	stca(lane, vmax, n, 0, cc)
    
    def asep(data, lane, vmax, n=20, p=0, cc=False):
    	"""Use the ASEP model to simulate the specified lane for 'n' discrete steps with probability 'p' for a car slowing down and with a speed limit of 'vmax' (measured in discrete steps). Setting argument 'cc' to 'True' activates Cruise Control mode. 'data' refers to the data-holding object that will store the simulation's data."""
    	data.build_position_history(lane)
    	data.build_speed_history(lane)
    	data.update_length(lane)
    	data.update_number(lane)
    	for i in range(n):
        	car = to.random.choice(lane.carlist)
        	update_and_move(car, lane, vmax, p, cc)
        	#this is where you want to grab data for graphs, animation, etc.
        	#print lane
        	data.append_position_history(lane)
        	data.append_speed_history(lane)
        	lane.g_update_all()




#lane = Lane(10)
#lane.populate(3)
#print lane.map
#data = Data()
#data.build_position_history(lane)

#pos = stca(data,lane, 3,10,0, True)
#print lane
#print pos


#exit()

color = ['snow','gainsboro','linen','moccasin','cornsilk','ivory','cornsilk','seashell','honeydew','azure','green','red','blue','turquoise','cyan','aquamarine','chartreuse','yellow','khaki','gold','goldenrod','sienna','peru','burlywood','beige','tan','chocolate','firebrick','orange','coral','tomato','salmon','pink','maroon','magenta','violet','plum','orchid','purple','thistle','slateblue1','royalblue1','lavenderblush1','skyblue1','SpringGreen2','DarkOliveGreen4','IndianRed1']

col =[]
numcar=[]
cars = []
size = []

class App:

    def __init__(self, root):
	self.length = 10
	self.lane= Lane(self.length)
	self.data = Data()
	self.data.build_position_history(self.lane)
	self.canvas = Canvas(root, height=100, width=self.length*10,)
	self.DefClr = root.cget("bg")
	self.canvas.pack()
	
	for i in range(1,self.length+1):
		self.canvas.create_line(i*10,0,i*10,100,dash=(3,6))

	self.canvas.delete(ALL)
	self.canvas.configure(background=self.DefClr)
	self.lane = Lane(0)
	
	frame = Frame(root)
	frame.pack()
	
	Label(frame, text="enter the number of cars:").pack(side=TOP)
	self.txt_ent = Entry(frame)
	self.txt_ent.pack()

	Label(frame, text="enter the length of road").pack(side=TOP)
	self.size_ent = Entry(frame)
	self.size_ent.pack()

	self.quit = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.quit.pack(side=LEFT)

	self.play = Button(frame, text="Play", command=self.moving)
        self.play.pack(side=LEFT)

	self.restart = Button(frame, text="Cars", command=self.adding)
        self.restart.pack(side=LEFT)

	self.create_size = Button(frame, text="Length", command=self.lanesize)
        self.create_size.pack(side=LEFT)

    def lanesize(self):
	if not numcar:
		pass
	else:
		numcar.pop(0)
	if not col:
		pass
	else:
		while col:
			col.pop(0)
	if not cars:
		pass
	else:
		while cars:
			cars.pop(0)
	if not size:
		pass
	else:
		size.pop(0)
	sizelane = int(self.size_ent.get())
	size.append(sizelane)
	self.length = size[0]
	self.lane= Lane(self.length)
	gw = .29 
	self.canvas = Canvas(root, bg="grey", height=100, width=self.length*10,)
	self.canvas.place(relx=gw,rely=0)
	
	for i in range(1,self.length+1):
		self.canvas.create_line(i*10,0,i*10,100,dash=(3,6))
	
	frame = Frame(root)
	frame.pack()

    def adding(self):
	h=int(self.txt_ent.get())
	numcar.append(h)
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
		while cars:
			cars.pop(0)
	for g in range(h): # creates strings
		x = str(g)
		s = 'mycar' + x
		cars.append(s)
	self.lane.populate(h)
	pos = self.lane.car_positions()
	a2 = [x * 10 for x in pos] 
	for i in range(h):
		rant = random.randint(0,len(color)-1)
		col.append(rant)
		self.canvas.create_rectangle(a2[i],50,a2[i]+10,60,fill=color[rant],tags=cars[i])
	print cars
	print self.lane.map

    def moving(self):
	if not numcar:
		print 'no cars added to lane'
		return
	print numcar, 'numcar'
	car_object = self.lane.carlist
	duration = 5
	pos = Rule.stca(self.data,self.lane, 3,5,0, True)
	print pos
	print car_object
	for i in range(len(pos[0])-1):
		for j in range(len(pos)):
			time.sleep(0.3)
			velocity = pos[j][i+1]-pos[j][i]
			print velocity
			#self.canvas.move(cars[j],10,0)
			if pos[j][i+1] > pos[j][i]:
				self.canvas.move(cars[j],velocity,0)
			else:
				self.canvas.delete(cars[j])
				self.canvas.create_rectangle(pos[j][i+1],50,pos[j][i+1]+10,60, fill=color[col[j]], tags=cars[j])
	

    def reset(self):
	print 'this also does nothing'

app = App(root)
root.mainloop()