## visual display of cars moving  
from Tkinter import *  
a = []
class App:
	def __init__(self,master):  
		bottomframe = Frame(root)
		bottomframe.pack( side = BOTTOM )
		frame = Frame(master,background = "red")  
		frame.pack()  
		self.button = Button(frame, text = "quit", fg = "red", command = frame.quit) 
		self.button.pack(side=LEFT) 
		#text = Text(root)
		#text.insert(INSERT, "Hello.....")
		#text.insert(END, "Bye Bye.....")
		#text.pack(side = BOTTOM)
		e = Entry(master,)
		e.pack()

		e.focus_set()
		
		a = []

		def callback():
				h = e.get()
				hh = int(h)
   				a.append(hh)
   				print a

		b = Button(master, text="get", width=10, command=callback)
		b.pack()  

root = Tk()  

app = App(root)  

root.mainloop()