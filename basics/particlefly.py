import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

COLOR_LIST=["white","red","blue","green","yellow"]
DIRECTION_LIST=[[2,0],[0,1],[-1,0],[0,-2]]
n=40

class Particle:
	def __init__(self,pos,color):
		self.color=color
		self.pos=pos
		self.radius=5

	def draw(self, canvas,offset):
		canvas.draw_circle(self.pos,self.radius,0.1,self.color,self.color)
		canvas.draw_circle([self.pos[0]+self.radius,self.pos[1]+self.radius],self.radius,0.1,self.color,self.color)
		canvas.draw_circle([self.pos[0],self.pos[1]+self.radius],self.radius,0.1,self.color,self.color)
		self.radius=random.randint(1,5)
		self.pos[0]=(self.pos[0]+offset[0])%500
		self.pos[1]=(self.pos[1]+offset[1])%500
	
	def touched(self,pos,newcolor):
		if self.pos[0]-15<pos[0]<self.pos[0]+15 and self.pos[1]-15<pos[1]<self.pos[1]+15:
			self.color=newcolor

def touch(pos):
	global particles
	for i in particles:	
		color=random.choice(COLOR_LIST)
		i.touched(pos,color)	

def drawparts(canvas):
	for i in range(n):
		particles[i].draw(canvas,random.choice(DIRECTION_LIST))

frame=simplegui.create_frame("Particles",500,500)
particles=[]
for i in range(n):
	p=Particle([random.randrange(500),random.randrange(500)],random.choice(COLOR_LIST))
	particles.append(p)
frame.set_draw_handler(drawparts)	
frame.set_mouseclick_handler(touch)
frame.add_label("Touch the flies to change its color",200)
frame.start()
