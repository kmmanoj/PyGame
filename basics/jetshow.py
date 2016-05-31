import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math

image=simplegui._load_local_image("ship.png")

class Jet:
	def __init__(self, angle, angle_vel, pos, thrust,offset):
		self.angle=angle
		self.max_angle_vel=angle_vel
		self.angle_vel=0
		self.vel=[0,0]
		self.pos=[pos[0]%800, pos[1]%600]
		self.max_thrust=thrust
		self.thrust=0
		self.forward=[self.thrust*math.cos(self.angle), self.thrust*math.sin(self.angle)]
		self.offset=[offset[0], offset[1]]
	
	def draw(self,canvas):
		self.update()
		if self.thrust==0:
			canvas.draw_image(image, [45,45], [90,90], [(self.pos[0]+self.offset[0])%800,(self.pos[1]+self.offset[1])%600], [30,30],self.angle*math.pi/180)    
		else:
			canvas.draw_image(image, [135,45], [90,90], [(self.pos[0]+self.offset[0])%800,(self.pos[1]+self.offset[1])%600], [30,30],self.angle*math.pi/180)   
	
	def update(self):
		self.angle+=self.angle_vel
		self.forward=[self.thrust*math.cos(self.angle*math.pi/180), self.thrust*math.sin(self.angle*math.pi/180)]
		c=self.max_thrust/15
		self.vel[0]=(1-c)*self.vel[0]+self.forward[0]
		self.vel[1]=(1-c)*self.vel[1]+self.forward[1]
		
		self.pos[0]=(self.pos[0]+self.vel[0])
		self.pos[1]=(self.pos[1]+self.vel[1])
ship=[]
for i in range(3):
	ship.append([])
	for j in range(3):
		ship[i].append(Jet(0,3,[150,100], 0.1, [i*50,j*50]))


def draw(canvas):
	global ship
	for i in range(3):
		for j in range(3):
			ship[i][j].draw(canvas)

def keydown(key):
	global ship
	if key==simplegui.KEY_MAP['up'] :
		for i in range(0,3):
			for j in range(i%2,3,2):
				ship[i][j].thrust=ship[i][j].max_thrust
	if key==simplegui.KEY_MAP['left']:
		for i in range(0,3):
			for j in range(i%2,3,2):
				ship[i][j].angle_vel=-ship[i][j].max_angle_vel
	if key==simplegui.KEY_MAP['right']:
		for i in range(0,3):
			for j in range(i%2,3,2):
				ship[i][j].angle_vel=ship[i][j].max_angle_vel
	if key==simplegui.KEY_MAP['w']:
		for i in range(0,3):
			for j in range(1-i%2,3,2):
				ship[i][j].thrust=ship[i][j].max_thrust
	if key==simplegui.KEY_MAP['a']:
		for i in range(0,3):
			for j in range(1-i%2,3,2):
				ship[i][j].angle_vel=-ship[i][j].max_angle_vel
	if key==simplegui.KEY_MAP['d']:
		for i in range(0,3):
			for j in range(1-i%2,3,2):
				ship[i][j].angle_vel=ship[i][j].max_angle_vel
	
def keyup(key):
	global ship
	if key==simplegui.KEY_MAP['up'] :
		for i in range(0,3):
			for j in range(i%2,3,2):
				ship[i][j].thrust=0
	if key==simplegui.KEY_MAP['left']:
		for i in range(0,3):
			for j in range(i%2,3,2):
				ship[i][j].angle_vel=0
	if key==simplegui.KEY_MAP['right']:
		for i in range(0,3):
			for j in range(i%2,3,2):
				ship[i][j].angle_vel=0
	if key==simplegui.KEY_MAP['w']:
		for i in range(0,3):
			for j in range(1-i%2,3,2):
				ship[i][j].thrust=0
	if key==simplegui.KEY_MAP['a']:
		for i in range(0,3):
			for j in range(1-i%2,3,2):
				ship[i][j].angle_vel=0
	if key==simplegui.KEY_MAP['d']:
		for i in range(0,3):
			for j in range(1-i%2,3,2):
				ship[i][j].angle_vel=0

frame=simplegui.create_frame("JET show : Air fare",800,600)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.start()


