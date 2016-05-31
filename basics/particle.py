import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

HEIGHT=500
WIDTH=500
COLOR_LIST=["white","red","blue","green","yellow"]
DIRECTION_LIST=[[1,0],[0,1],[-1,0],[0,-1]]
n=100

class Particle:
	def __init__(self,pos,color):
		self.color=color
		self.pos=pos
		self.radius=2

	def draw(self, canvas,offset):
		canvas.draw_circle(self.pos,self.radius,0.1,self.color,self.color)

		self.pos[0]+=offset[0]
		self.pos[1]+=offset[1]
	
def drawparts(canvas):
	for i in range(n):
		particles[i].draw(canvas,random.choice(DIRECTION_LIST))

frame=simplegui.create_frame("Particles",WIDTH,HEIGHT)
particles=[]
for i in range(n):
	p=Particle([WIDTH/2,HEIGHT/2],random.choice(COLOR_LIST))
	particles.append(p)

frame.set_draw_handler(drawparts)	
frame.start()
