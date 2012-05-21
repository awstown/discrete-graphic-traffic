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
mode = ['','stca','asep','ca184']
xy = []

class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        try:
            # For Mac OS
            tw.tk.call("::tk::unsupported::MacWindowStyle",
                       "style", tw._w,
                       "help", "noActivates")
        except TclError:
            pass
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def createToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)




class App:

    def __init__(self, root):
	self.length = 30
	self.lane= to.Lane(self.length)
	self.data = to.Data()
	self.data.build_position_history(self.lane)
	self.canvas = Canvas(root,bg="grey", height=100, width=self.length*10,)
	self.DefClr = root.cget("bg")
	self.canvas.pack()

	self.canvas.delete(ALL)
	self.canvas.configure(background=self.DefClr)
	self.lane = to.Lane(0)

	#root.geometry("650x300")
	self.topframe = Frame(root)
	self.topframe.pack(side=TOP,expand=YES)
	otherframe = Frame(root)
	otherframe.pack(side=LEFT,expand=YES,padx = 5)
	centerframe = Frame(root)
	centerframe.pack(side=LEFT,expand=YES)
	frame = Frame(root)
	frame.pack(side=LEFT,expand=YES,padx = 5)

	self.label = Label(otherframe)
	self.label.pack()

	self.label2 = Label(frame)
	self.label2.pack(side=LEFT)

	self.var = IntVar()
	self.var3 = IntVar()
	self.checkvar = StringVar()
	self.check = Checkbutton(otherframe, text="Cruise Control", variable=self.checkvar, onvalue="True", offvalue="False")
	self.check.pack(side=RIGHT)

	self.var2 = IntVar()
	self.R1 = Radiobutton(otherframe, text="stca", variable=self.var2, value=1, command=self.sel)
	self.R1.pack( anchor = W )

	self.R2 = Radiobutton(otherframe, text="asep", variable=self.var2, value=2, command=self.sel)
	self.R2.pack( anchor = W )
	
	self.R3 = Radiobutton(otherframe, text="ca184", variable=self.var2, value=3, command=self.sel)
	self.R3.pack( anchor = W)
	
	self.R1.select()
	self.check.select()
	selection = "traffic simulation in " + str(mode[self.var2.get()]) + " mode"
	self.label.config(text = selection, bg = "grey",bd = 1, relief = SUNKEN)

	#Label(frame, text="probability that drivers will slow down").pack(side=TOP)
	sim = "probability that drivers will slow down:"
	self.label2.config(text = sim)
	self.spin = Spinbox(frame, from_=0, to=1,increment = .1, width = 3)
	self.spin.pack(side=TOP)
	

	Label(centerframe, text="enter the number of cars:").pack(side=TOP)
	
	self.txt_ent = Entry(centerframe)
	self.txt_ent.pack()

	Label(centerframe, text="enter the length of road").pack(side=TOP)
	self.size_ent = Entry(centerframe)
	self.size_ent.pack()

	Label(centerframe, text="enter the duration").pack(side=TOP)
	self.time_ent = Entry(centerframe)
	self.time_ent.pack()

	Label(centerframe, text="enter the max velocity").pack(side=TOP)
	self.velocity_ent = Entry(centerframe)
	self.velocity_ent.pack()

	## enter initial values
	self.txt_ent.insert(0, "10")
	self.size_ent.insert(0, "60")
	self.time_ent.insert(0, "11")
	self.velocity_ent.insert(0, "3")
	##

	## create hover text
	createToolTip(self.check, "determines if cars stay at max speed")
	createToolTip(self.R1, "moves all cars at once")
	createToolTip(self.R2, "moves one car at a time")
	createToolTip(self.R3, "not programmed yet - does stca model")
	##

	self.quit = Button(centerframe, text="QUIT", fg="red", command=frame.quit)
        self.quit.pack(side=LEFT)

	self.play = Button(centerframe, text="Play", command=self.moving)
        self.play.pack(side=LEFT)

	self.restart = Button(centerframe, text="Create Road", command=self.adding)
        self.restart.pack(side=LEFT)

	#self.create_size = Button(frame, text="Length", command=self.lanesize)
        #self.create_size.pack(side=LEFT)

    #def cb(self):
    #    print "variable is", self.var.get()

    def sel(self):
   	selection = "traffic simulation in " + str(mode[self.var2.get()]) + " mode"
	self.label.config(text = selection)

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
	self.canvas.destroy()
	## add lane
	self.length = gg
	self.lane= to.Lane(self.length)
	self.canvas = Canvas(self.topframe,bg="grey", height=100, width=self.length*10)
	#gw = .29 
	#self.canvas.place(relx=gw,rely=0)
	self.canvas.update()
	self.canvas.pack()
	for i in range(1,self.length+1):
		self.canvas.create_line(i*10,0,i*10,100,dash=(3,6))
	##
	self.lane.populate(h)
	duration = kk
	max_v = int(self.velocity_ent.get())
	prob = self.spin.get()
	prob_int = float(prob)
	cruise = self.checkvar.get()
	rad = self.var2.get()
	if rad == 1:
		stca(self.data,self.lane, max_v,duration,prob_int,cruise) ## run code to generate car history
	elif rad == 2:
		asep(self.data,self.lane, max_v,duration,prob_int,cruise)
	else:
		stca(self.data,self.lane, max_v,duration,prob_int,cruise)
	self.pos = self.data.position_history
	self.pos.sort()
	for i in range(len(self.pos)):   #need to extract the first value of every list
		rant = random.randint(0,len(color)-1)
		col.append(rant)
		self.canvas.create_rectangle(self.pos[i][0],50,self.pos[i][0]+10,60,fill=color[rant],tags=cars[i])

    def moving(self):
	if not numcar:
		print 'Create Road First'
		return
	for i in range(len(self.pos)): #resets the rectangles to initial position
		self.canvas.delete(cars[i])
		self.canvas.create_rectangle(self.pos[i][0],50,self.pos[i][0]+10,60,fill=color[col[i]],tags=cars[i])
	self.canvas.update() #this line very necessary to update original positions
	ind = []
	for i in range(len(self.pos[0])-1):
		time.sleep(0.02)
		xx = 0
		self.canvas.update()
		#x1=0
		while xx < 10:
			xx = xx + 1
			time.sleep(0.05)
			for j in range(len(self.pos)):
				if self.pos[j][i+1] > self.pos[j][i]:
					vel = (self.pos[j][i+1] - self.pos[j][i])/10
					self.canvas.move(cars[j],vel,0)
					self.canvas.update()
				elif self.pos[j][i+1] < self.pos[j][i]:
					#vel2 = (self.length*10 - self.pos[j][i])/10
					#self.canvas.move(cars[j],vel2,0)
					self.canvas.update()
					if not ind:
						pass
					else:
						ind.pop(0)
					ind.append(j)
					if xx ==1:
						#yy = 0
						#while yy < 10:
						#	yy = yy + 1
						#	#time.sleep(0.015)
						#	vel3 = (self.length*10 - self.pos[j][i])/10
						#	self.canvas.move(cars[j],vel3,0)
						#	self.canvas.update()
						self.canvas.delete(cars[ind[0]])
						self.canvas.create_rectangle(-10,50,0,60, fill=color[col[ind[0]]], tags=cars[ind[0]])
						self.canvas.update()
					else:
						time.sleep(0.01)
						veloc = (self.pos[ind[0]][i+1]+10)/9.0
						self.canvas.move(cars[ind[0]],veloc,0)
						self.canvas.update()
		self.canvas.update()
	#print self.pos


    def reset(self):
	print 'this also does nothing'

app = App(root)
root.mainloop()