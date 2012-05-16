<<<<<<< HEAD
=======
# Defines the Car object and the Lane object. This was built assuming the movement of the cars would be handled by a 'rules' script.
>>>>>>> dev

import random
from Tkinter import *
root = Tk()
root.title("Traffic Simulation")
import time
<<<<<<< HEAD
from traffic_objects import Lane as Lane


color = ['snow','gainsboro','linen','moccasin','cornsilk','ivory','cornsilk','seashell','honeydew','azure','green','red','blue','turquoise','cyan','aquamarine','chartreuse','yellow','khaki','gold','goldenrod','sienna','peru','burlywood','beige','tan','chocolate','firebrick','orange','coral','tomato','salmon','pink','maroon','magenta','violet','plum','orchid','purple','thistle','slateblue1','royalblue1','lavenderblush1','skyblue1','SpringGreen2','DarkOliveGreen4','IndianRed1']


cars=['mycar0','mycar1','mycar2','mycar3','mycar4','mycar5','mycar6','mycar7','mycar8','mycar9','mycar10','mycar11','mycar12','mycar13','mycar14','mycar15','mycar16','mycar17','mycar18','mycar19','mycar20','mycar21','mycar22','mycar23','mycar24','mycar25','mycar26','mycar27','mycar28','mycar29','mycar30','mycar31','mycar32','mycar33','mycar34','mycar35','mycar36','mycar37','mycar38','mycar39','mycar40','mycar41','mycar42','mycar43','mycar44','mycar45','mycar46','mycar47','mycar48','mycar49','mycar50']

col =[]
numcar=[]
=======
from rules import *

color = ['snow','gainsboro','linen','moccasin','cornsilk','ivory','cornsilk','seashell','honeydew','azure','green','red','blue','turquoise','cyan','aquamarine','chartreuse','yellow','khaki','gold','goldenrod','sienna','peru','burlywood','beige','tan','chocolate','firebrick','orange','coral','tomato','salmon','pink','maroon','magenta','violet','plum','orchid','purple','thistle','slateblue1','royalblue1','lavenderblush1','skyblue1','SpringGreen2','DarkOliveGreen4','IndianRed1']

col =[]
numcar=[]
cars = []
size = []
>>>>>>> dev

class App:

    def __init__(self, root):
<<<<<<< HEAD
        # Hard Coded Length of the Lane you can change this
        self.length = 30
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
        h=int(self.txt_ent.get())
        print h
        numcar.append(h)
        self.lane.populate(h)
        pos = self.lane.car_positions()
        a2 = [x * 10 for x in pos] 
        for i in range(h):
                rant = random.randint(0,len(color)-1)
                col.append(rant)
                self.canvas.create_rectangle(a2[i],50,a2[i]+10,60,fill=color[rant],tags=cars[i])
        print col
        for i in range(h):
                space = self.lane.map.index('n')
                self.lane.map.insert(space,'_')
                self.lane.map.remove('n')
        self.lane.map_update()
        print self.lane.map
        print self.lane.car_positions()

    def moving(self):
        if not numcar:
                print 'no cars added to lane'
                return
        print numcar
        velocity = 10
        duration = 50
        car_object = self.lane.carlist
        print car_object
        for i in range(duration):
                time.sleep(0.1)
                #h=int(self.txt_ent.get())
                for i in range(numcar[0]):
                        x1,y1,x2,y2 = self.canvas.coords(cars[i])
                        if x1+velocity > self.length*10:
                                self.canvas.delete(cars[i])
                                self.canvas.create_rectangle(0,50,10,60, fill=color[col[i]], tags=cars[i])
                        elif x1+velocity == self.length*10:
                                self.canvas.delete(cars[i])
                                self.canvas.create_rectangle(0,50,10,60, fill=color[col[i]], tags=cars[i])
                        else:
                                self.canvas.move(cars[i],velocity,0)
                self.canvas.update()

    def reset(self):
        print 'this also does nothing'
=======
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
	stca(self.data,self.lane, 4,15,0, True) ## run code to generate car history
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
	ind = []
	for i in range(len(self.pos[0])-1):
		time.sleep(0.5)
		xx = 0
		self.canvas.update()
		x1=0
		while xx < 10:
			xx = xx + 1
			time.sleep(0.1)
			for j in range(len(self.pos)):
				if self.pos[j][i+1] > self.pos[j][i]:
					vel = (self.pos[j][i+1] - self.pos[j][i])/10
					self.canvas.move(cars[j],vel,0)
					self.canvas.update()
				elif self.pos[j][i+1] < self.pos[j][i]:
					vel2 = (self.length*10 - self.pos[j][i])/10
					self.canvas.move(cars[j],vel2,0)
					self.canvas.update()
					#self.canvas.delete(cars[j])
					#self.canvas.update()
					#self.canvas.create_rectangle(0,50,10,60, fill=color[col[j]], tags=cars[j])
					#self.canvas.update()
					#vel3 = self.pos[j][i+1]/10
					#self.canvas.move(cars[j],vel3,0)
					#self.canvas.update()
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
			time.sleep(0.1)
			xy = 0
			while xy < 10:
				time.sleep(0.01)
				xy = xy+1
				veloc = (self.pos[ind[0]][i+1])/10
				#print veloc
				self.canvas.move(cars[ind[0]],veloc,0)
				self.canvas.update()
		self.canvas.update()

		#for j in range(len(self.pos)):
		#	#velocity = self.pos[j][i+1]-self.pos[j][i]
		#	self.canvas.update()
		#	#x1,y1,x2,y2 = self.canvas.coords(cars[j])
		#	if self.pos[j][i+1] > self.pos[j][i]:
		#		while xx < 10:
		#			xx = xx + 1
		#			time.sleep(0.1)
		#			for g in range(len(self.pos)):
		#				vel = (self.pos[g][i+1] - self.pos[g][i])/10
		#				self.canvas.move(cars[g],vel,0)
		#			self.canvas.update()
		#			#print xx
		#		#xx = 0
		#	elif self.pos[j][i+1] < self.pos[j][i]:
		#		while xx < 10:
		#			xx = xx + 1
		#			time.sleep(0.01)
		#			vel = (self.length*10 - self.pos[j][i])/10
		#			for g in range(len(self.pos)):
		#				vel = (self.length*10 - self.pos[g][i])/10
		#				self.canvas.move(cars[g],vel,0)	
		#			self.canvas.update()
		#			print vel
		#	
		#	self.canvas.update()

    def reset(self):
	print 'this also does nothing'
>>>>>>> dev

app = App(root)
root.mainloop()