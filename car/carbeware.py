import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math

a=0
vel=0
pos=[400,250]
angle=0
angle_vel=0
car=simplegui._load_local_image("cars.png")
thrust=False
time=0
i=0
j=0

exp=simplegui._load_local_image("blast.png")
center=[0,0]

def draw(canvas):
	global pos,angle, vel, time, i, j, center
	#canvas.draw_circle(pos, 4, 1, "red", "red")
	if pos[0]>760 or pos[0]<40 or pos[1]>460 or pos[1]<40:
		time+=1
		canvas.draw_image(exp , center, [50,54], pos, [100,100] )
		if time>10:
			time=0
			center=[25+j*50, 27+i*54]
			j=j+1
			if j==10:
				i=i+1
				j=0
		if i>3:
			angle=0
			i=0
			j=0
			vel=0
			pos=[400,250]

	else:		
		canvas.draw_image(car, [25, 50], [50, 100], pos, [50, 100], angle+math.pi/2)
		if vel>1:
			angle=(angle+angle_vel)%(2*math.pi)
		else:
			angle=(angle+angle_vel*vel)%(2*math.pi)
		vel=(1-0.02)*vel+a*0.1
		pos[0]=(pos[0]+vel*math.cos(angle))
		pos[1]=(pos[1]+vel*math.sin(angle))
		

	
def keydown(key):
	global vel, angle_vel,thrust, a
	if key==simplegui.KEY_MAP['up']:
		a=1
		thrust=True
	if key==simplegui.KEY_MAP['down']:
		a=-1/3
		thrust=True
	if key==simplegui.KEY_MAP['left']:
		if vel>=0:
			angle_vel=-0.02
		else:
			angle_vel=-0.006
	if key==simplegui.KEY_MAP['right']:
		if vel>=0:
			angle_vel=0.02
		else:
			angle_vel=0.006

def keyup(key):
	global vel, angle_vel, thrust, a
	if key==simplegui.KEY_MAP['up']:
		a=0
		thrust=False
	if key==simplegui.KEY_MAP['down']:
		a=0
		thrust=False
	if key==simplegui.KEY_MAP['right']:
		angle_vel=0
	if key==simplegui.KEY_MAP['left']:
		angle_vel=0


frame=simplegui.create_frame("CAR", 800, 500)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.start()
