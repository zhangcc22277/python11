from tkinter import *
class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()

class creatWidgerts(self):
	self.helloLabel = Label(self,text='Hello,world!')
	self.helloLabel.pack()
	self.quitButton = Button(self,text='Quit',command=self.quit)
	self.quitButton.pack()

app=Application()
app.master.title('Hello world')
app.mainloop()