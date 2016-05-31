import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math

vel=0
pos=[400,250]
angle=0
angle_vel=0
car=simplegui._load_local_image("cars.png")
thrust=False

def draw(canvas):
	global pos,angle
	#canvas.draw_circle(pos, 4, 1, "red", "red")
	canvas.draw_image(car, [25, 50], [50, 100], pos, [50, 100], angle+math.pi/2)
	if thrust:
		angle=(angle+angle_vel)%(2*math.pi)
	pos[0]=(pos[0]+vel*math.cos(angle))%800
	pos[1]=(pos[1]+vel*math.sin(angle))%500
	
def keydown(key):
	global vel, angle_vel,thrust
	if key==simplegui.KEY_MAP['up']:
		vel=3
		thrust=True
	if key==simplegui.KEY_MAP['down']:
		vel=-1
		if angle_vel!=0:
			angle_vel=-angle_vel/3 
		thrust=True
	if key==simplegui.KEY_MAP['left']:
		if vel>=0:
			angle_vel=-0.03
		else:
			angle_vel=0.01
	if key==simplegui.KEY_MAP['right']:
		if vel>=0:
			angle_vel=0.03
		else:
			angle_vel=-0.01

def keyup(key):
	global vel, angle_vel, thrust
	if key==simplegui.KEY_MAP['up']:
		vel=0
		thrust=False
	if key==simplegui.KEY_MAP['down']:
		vel=0
		thrust=False
	if key==simplegui.KEY_MAP['right']:
		angle_vel=0
	if key==simplegui.KEY_MAP['left']:
		angle_vel=0


frame=simplegui.create_frame("CAR Movement", 800, 500)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.start()
