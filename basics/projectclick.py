import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math

WIDTH=800
HEIGHT=600
projectiles=[]

cannon=simplegui._load_local_image("cannon.png")

angle=0
v=1

def draw(canvas):
	remover=[]
	if len(projectiles)==0:
		canvas.draw_image(cannon,(67.5,62),(135,124),(20,HEIGHT-20),(40,40),math.pi-angle)
	for p in projectiles:
		if p.inside():
			p.draw_ball(canvas)
			canvas.draw_image(cannon,(67.5,62),(135,124),(20,HEIGHT-20),(40,40),math.pi-angle)
		else:
			remover.append(p)
	for rp in remover:
		projectiles.remove(rp)



def shot(pos):
	global angle,v
	angle=math.atan(float((HEIGHT-pos[1]))/float(pos[0]))
	v=float(max(pos[0],HEIGHT-pos[1]))/WIDTH*45
	projectiles.append(Projectile(float(v)/10,angle))

class Projectile:
	def __init__(self,v,angle):
		self.vx=v*math.cos(angle)
		self.vy=-v*math.sin(angle)
		self.radius=5
		if self.vx==0 and self.vy==0:
			self.vx=1
			self.vy=-1
		self.pos=[20,HEIGHT-20]
	def __str__(self):
		return "Projectile of "+str(self.vx)+"i + "+str(self.vy)+"j "
	def draw_ball(self,canvas):
		canvas.draw_circle(self.pos,self.radius,1,"blue","blue")
		self.pos[0]+=self.vx
		self.pos[1]+=self.vy
		self.vy+=0.01
	def inside(self):
		return (self.pos[0]>0 and self.pos[0]<WIDTH-self.radius) and self.pos[1]<=HEIGHT-self.radius


frame=simplegui.create_frame("Projectile",WIDTH,HEIGHT)
frame.set_draw_handler(draw)
frame.set_canvas_background("#0f0f0f")
frame.add_label("Projectile: click on screen to shoot",30);
frame.set_mouseclick_handler(shot)
frame.start()