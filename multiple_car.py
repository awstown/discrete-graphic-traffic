# Defines the Car object and the Lane object. This was built assuming the movement of the cars would be handled by a 'rules' script.

import random
from Tkinter import *
root = Tk()
root.title("Traffic Simulation")
import time
from rules import *

color = ['snow','gainsboro','linen','moccasin','cornsilk','ivory','cornsilk','seashell','honeydew','azure','green','red','blue','turquoise','cyan','aquamarine','chartreuse','yellow','khaki','gold','goldenrod','sienna','peru','burlywood','beige','tan','chocolate','firebrick','orange','coral','tomato','salmon','pink','maroon','magenta','violet','plum','orchid','purple','thistle','slateblue1','royalblue1','lavenderblush1','skyblue1','SpringGreen2','DarkOliveGreen4','IndianRed1']

col =[]
numcar=[]
cars = []
size = []

class App:

    def __init__(self, root):
	self.length = 10
	self.lane= to.Lane(self.length)
	self.data = to.Data()
	self.data.build_position_history(self.lane)
	self.canvas = Canvas(root,bg="grey", height=100, width=self.length*10,)
	#self.DefClr = root.cget("bg")
	self.canvas.pack()
	
	for i in range(1,self.length+1):
		self.canvas.create_line(i*10,0,i*10,100,dash=(3,6))

	#self.canvas.delete(ALL)
	#self.canvas.configure(background=self.DefClr)
	#self.lane = to.Lane(0)
	
	frame = Frame(root)
	frame.pack()
	
	Label(frame, text="enter the number of cars:").pack(side=TOP)
	self.txt_ent = Entry(frame)
	self.txt_ent.pack()

	#Label(frame, text="enter the length of road").pack(side=TOP)
	#self.size_ent = Entry(frame)
	#self.size_ent.pack()

	self.quit = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.quit.pack(side=LEFT)

	self.play = Button(frame, text="Play", command=self.moving)
        self.play.pack(side=LEFT)

	self.restart = Button(frame, text="Cars", command=self.adding)
        self.restart.pack(side=LEFT)

	#self.create_size = Button(frame, text="Length", command=self.lanesize)
        #self.create_size.pack(side=LEFT)

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
	self.lane= to.Lane(self.length)
	gw = .29 
	self.canvas = Canvas(root, bg="grey", height=100, width=self.length*10,)
	self.canvas.place(relx=gw,rely=0)
	
	for i in range(1,self.length+1):
		self.canvas.create_line(i*10,0,i*10,100,dash=(3,6))
	
	frame = Frame(root)
	frame.pack()

    def adding(self):
	if not self.txt_ent.get():
		print 'input a number into the blank field'
		return
	h=int(self.txt_ent.get())
	numcar.append(h)
	pos = self.lane.car_positions()
	if not pos:
		pass
	else:
		numcar.pop(0)
		while self.pos:
			self.pos.pop(0)
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
	stca(self.data,self.lane, 3,6,0, True) ## run code to generate car history
	self.pos = self.data.position_history
	print self.pos
	self.pos.sort()
	print self.pos, 'sorted'
	for i in range(len(self.pos)):   #need to extract the first value of every list
		rant = random.randint(0,len(color)-1)
		col.append(rant)
		self.canvas.create_rectangle(self.pos[i][0],50,self.pos[i][0]+10,60,fill=color[rant],tags=cars[i])

    def moving(self):
	if not numcar:
		print 'no cars added to lane'
		return
	print numcar, 'numcar'
	print self.pos
	print cars
	for i in range(len(self.pos)): #resets the rectangles to initial position
		self.canvas.delete(cars[i])
		self.canvas.create_rectangle(self.pos[i][0],50,self.pos[i][0]+10,60,fill=color[col[i]],tags=cars[i])
	self.canvas.update() #this line very necessary to update original positions
	for i in range(len(self.pos[0])-1):
		time.sleep(0.9)
		for j in range(len(self.pos)):
			velocity = self.pos[j][i+1]-self.pos[j][i]
			self.canvas.update()
			x1,y1,x2,y2 = self.canvas.coords(cars[j])
			if self.pos[j][i+1] > self.pos[j][i]:
				#x1,y1,x2,y2 = self.canvas.coords(cars[j])
				while x1 < self.pos[j][i+1]:
					time.sleep(0.01)
					self.canvas.move(cars[j],1,0)
					self.canvas.update() 
					x1,y1,x2,y2 = self.canvas.coords(cars[j])
				#print x1
			elif self.pos[j][i+1] < self.pos[j][i]:
				while x1 < self.length*10:
					pass
					time.sleep(0.01)
					self.canvas.move(cars[j],1,0)
					self.canvas.update() 
					x1,y1,x2,y2 = self.canvas.coords(cars[j])
				self.canvas.update()
				self.canvas.delete(cars[j])
				self.canvas.update()
				self.canvas.create_rectangle(0,50,10,60, fill=color[col[j]], tags=cars[j])
				self.canvas.update()
				x1,y1,x2,y2 = self.canvas.coords(cars[j])
				while x1 < self.pos[j][i+1]:
					pass
					time.sleep(0.01)
					self.canvas.move(cars[j],1,0)
					self.canvas.update() 
					x1,y1,x2,y2 = self.canvas.coords(cars[j])
			self.canvas.update()

    def reset(self):
	print 'this also does nothing'

app = App(root)
root.mainloop()