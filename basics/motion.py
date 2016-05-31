import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

width=900
height=500
pos=[width/2,height/2]
vel=[1,1]
ball_r=7

def draw(canvas):
	global vel, pos
	canvas.draw_text("["+str(mod(vel[0]))+","+str(mod(vel[1]))+"]",(width-50,15),15,"white")
	canvas.draw_circle(pos, ball_r, 2, "red","red")
	pos[0]=pos[0]+vel[0]
	pos[1]=pos[1]+vel[1]
	if pos[0]<ball_r or pos[0]>width-ball_r:
		vel[0]=-vel[0]
	if pos[1]<ball_r or pos[1]>height-ball_r:
		vel[1]=-vel[1]

def mod(x):
	if x<0:
		return -x
	else:
		return x
def incrementx():
	if vel[0]<0:
		vel[0]-=1
	else:
		vel[0]+=1

def decrementx():
	if vel[0]>0:
		vel[0]-=1
	elif vel[0]!=0:
		vel[0]+=1

def incrementy():
	if vel[1]<0:
		vel[1]-=1
	else:
		vel[1]+=1

def decrementy():
	if vel[1]>0:
		vel[1]-=1
	elif vel[1]!=0:
		vel[1]+=1

frame=simplegui.create_frame("motion", width, height)
frame.set_draw_handler(draw)
frame.add_label("x:",200)
frame.add_button("+",incrementx,50) 
frame.add_button("-",decrementx,50)
frame.add_label("y:",200)
frame.add_button("+",incrementy,50)
frame.add_button("-",decrementy,50)

frame.start()
