import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

RADIUS=5
WIDTH=800
HEIGHT=600
AvailableHeight=[HEIGHT-RADIUS]*(WIDTH/(2*RADIUS))
beads=[]

class bead:
	def __init__(self,pos):
		self.pos=pos
		self.radius=RADIUS
		self.notfinalpos=True
		self.vel=[0,random.randint(1,5)]
	def __str__(self):
		return "bead of radius "+str(self.radius)
	def draw(self,canvas):
		global AvailableHeight
		self.pos[0]+=self.vel[0]
		if self.pos[1]>AvailableHeight[self.pos[0]/(2*RADIUS)] and self.notfinalpos:
			self.vel[1]=0
			self.pos[1]=AvailableHeight[self.pos[0]/(2*RADIUS)]
			AvailableHeight[self.pos[0]/(2*RADIUS)]-=2*RADIUS
			self.notfinalpos=False			
		self.pos[1]+=self.vel[1]
		canvas.draw_circle(self.pos,self.radius,1,"blue","blue")


def draw(canvas):
	for bead in beads:
		bead.draw(canvas)

def mouseclick(pos):
	if pos[1]<AvailableHeight[pos[0]/(2*RADIUS)]:
		beads.append(bead([pos[0],pos[1]]))
		
frame=simplegui.create_frame("Window",WIDTH,HEIGHT)
frame.set_draw_handler(draw)
frame.set_canvas_background("#0f0f0f");
frame.set_mouseclick_handler(mouseclick)
frame.start();