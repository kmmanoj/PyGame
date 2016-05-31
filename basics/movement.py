import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

vx=0
vy=0

pos=[10,10]

def drawball(canvas):
	canvas.draw_circle(pos,5,1,"blue","blue")
	update()

def move(key):
	global vx, vy
	if key==simplegui.KEY_MAP['left']:
		vx=-1
	elif key==simplegui.KEY_MAP['up']:
		vy=-1
	elif key==simplegui.KEY_MAP['right']:
		vx=1
	elif key==simplegui.KEY_MAP['down']:
		vy=1

	

def stop(key):
	global vx, vy
	if key==simplegui.KEY_MAP['down']:
		vy=0
	elif key==simplegui.KEY_MAP['up']:
		vy=0
	elif key==simplegui.KEY_MAP['left']:
		vx=0	
	elif key==simplegui.KEY_MAP['right']:
		vx=0

def update():
	pos[0]=(pos[0]+vx)%500
	pos[1]=(pos[1]+vy)%500


frame=simplegui.create_frame("frame",500,500)
timer=simplegui.create_timer(10,update)
frame.set_draw_handler(drawball)
frame.set_keydown_handler(move)
frame.set_keyup_handler(stop)
frame.start()
