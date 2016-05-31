import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

width=900
height=500
pos=[width/2,height/2]
vel=[0,0]
ball_r=7
color="blue"
collist=["blue","white","green","red","yellow"]

def draw(canvas):
	global vel, pos, color
	canvas.draw_circle(pos, ball_r, 1, color,color)
	pos[0]=pos[0]+vel[0]
	pos[1]=pos[1]+vel[1]
	if pos[0]<ball_r or pos[0]>width-ball_r:
		vel[0]=-vel[0]
		x=random.randint(0,4)
		color=collist[x]
	if pos[1]<ball_r or pos[1]>height-ball_r:
		vel[1]=-vel[1]
		x=random.randint(0,4)
		color=collist[x]

def keypressed(key):
	global vel
	a=1
	if key==simplegui.KEY_MAP["left"]:
		vel[0]-=a
	elif key==simplegui.KEY_MAP["right"]:
		vel[0]+=a
	elif key==simplegui.KEY_MAP["up"]:
		vel[1]-=a
	elif key==simplegui.KEY_MAP["down"]:
		vel[1]+=a

frame=simplegui.create_frame("motion", width, height)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keypressed)

frame.start()
