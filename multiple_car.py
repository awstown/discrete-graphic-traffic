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
	self.length = 30
	self.lane= to.Lane(self.length)
	self.data = to.Data()
	self.data.build_position_history(self.lane)
	self.canvas = Canvas(root,bg="grey", height=100, width=self.length*10,)
	self.DefClr = root.cget("bg")
	self.canvas.pack()

	#for i in range(1,self.length+1):
	#	self.canvas.create_line(i*10,0,i*10,100,dash=(3,6))

	self.canvas.delete(ALL)
	self.canvas.configure(background=self.DefClr)
	self.lane = to.Lane(0)

	root.geometry("500x300")
	frame = Frame(root)
	frame.pack()

	Label(frame, text="enter the number of cars:").pack(side=TOP)
	self.txt_ent = Entry(frame)
	self.txt_ent.pack()

	Label(frame, text="enter the length of road").pack(side=TOP)
	self.size_ent = Entry(frame)
	self.size_ent.pack()

	Label(frame, text="enter the duration").pack(side=TOP)
	self.time_ent = Entry(frame)
	self.time_ent.pack()

	Label(frame, text="enter the max velocity").pack(side=TOP)
	self.velocity_ent = Entry(frame)
	self.velocity_ent.pack()

	self.quit = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.quit.pack(side=LEFT)

	self.play = Button(frame, text="Play", command=self.moving)
        self.play.pack(side=LEFT)

	self.restart = Button(frame, text="Create Road", command=self.adding)
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
	#gw = .29
	gw = 0 
	self.canvas = Canvas(root, bg="grey", height=100, width=self.length*10,)
	self.canvas.place(relx=gw,rely=0)

	for i in range(1,self.length+1):
		self.canvas.create_line(i*10,0,i*10,100,dash=(3,6))

	frame = Frame(root)
	frame.pack()

    def adding(self):
	if not self.txt_ent.get():
		print 'input the number of cars'
		return
	if not self.size_ent.get():
		print 'input the length of the road'
		return
	if not self.time_ent.get():
		print 'input the duration'
		return
	if not self.velocity_ent.get():
		print 'input a max velocity'
		return
	h=int(self.txt_ent.get())
	gg = int(self.size_ent.get())
	kk = int(self.time_ent.get())
	numcar.append(h)
	pos = self.lane.car_positions()
	#print pos
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
	## add lane
	self.length = gg
	self.lane= to.Lane(self.length)
	self.canvas = Canvas(root,bg="grey", height=100, width=self.length*10)
	gw = .29 
	self.canvas.place(relx=gw,rely=0)
	self.canvas.update()
	for i in range(1,self.length+1):
		self.canvas.create_line(i*10,0,i*10,100,dash=(3,6))
	frame = Frame(root)
	frame.pack()
	##
	self.lane.populate(h)
	duration = kk
	max_v = int(self.velocity_ent.get())
	stca(self.data,self.lane, max_v,duration,0, True) ## run code to generate car history
	self.pos = self.data.position_history
	#print self.pos
	self.pos.sort()
	#print self.pos, 'sorted'
	for i in range(len(self.pos)):   #need to extract the first value of every list
		rant = random.randint(0,len(color)-1)
		col.append(rant)
		self.canvas.create_rectangle(self.pos[i][0],50,self.pos[i][0]+10,60,fill=color[rant],tags=cars[i])

    def moving(self):
	if not numcar:
		print 'Create Road First'
		return
	#print numcar, 'numcar'
	#print self.pos
	#print cars
	for i in range(len(self.pos)): #resets the rectangles to initial position
		self.canvas.delete(cars[i])
		self.canvas.create_rectangle(self.pos[i][0],50,self.pos[i][0]+10,60,fill=color[col[i]],tags=cars[i])
	self.canvas.update() #this line very necessary to update original positions
	ind = []
	for i in range(len(self.pos[0])-1):
		time.sleep(0.2)
		xx = 0
		self.canvas.update()
		x1=0
		while xx < 10:
			xx = xx + 1
			time.sleep(0.05)
			for j in range(len(self.pos)):
				if self.pos[j][i+1] > self.pos[j][i]:
					vel = (self.pos[j][i+1] - self.pos[j][i])/10
					self.canvas.move(cars[j],vel,0)
					self.canvas.update()
				elif self.pos[j][i+1] < self.pos[j][i]:
					vel2 = (self.length*10 - self.pos[j][i])/10
					self.canvas.move(cars[j],vel2,0)
					self.canvas.update()
					if not ind:
						pass
					else:
						ind.pop(0)
					ind.append(j)
					x1,y1,x2,y2 = self.canvas.coords(cars[j])
		#print x1
		#print ind[0]	
		if x1 == self.length*10:
			#print 'true'
			self.canvas.delete(cars[ind[0]])
			self.canvas.create_rectangle(0,50,10,60, fill=color[col[ind[0]]], tags=cars[ind[0]])
			self.canvas.update()
			#x1,y1,x2,y2 = self.canvas.coords(cars[j])
			#print x1, 'yoo', self.pos[ind[0]][i+1]
			time.sleep(0.05)
			xy = 0
			while xy < 10:
				time.sleep(0.01)
				xy = xy+1
				veloc = (self.pos[ind[0]][i+1])/10
				#print veloc
				self.canvas.move(cars[ind[0]],veloc,0)
				self.canvas.update()
		self.canvas.update()


    def reset(self):
	print 'this also does nothing'

app = App(root)
root.mainloop()