import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math

WIDTH=700
HEIGHT=500
ball_pos=[]
BALL_RADIUS=20

def distance(x,y):
	return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

def draw_circles(canvas):
	for pos in ball_pos:
		canvas.draw_circle(pos,BALL_RADIUS,1,"black","red")

def mouseclicked(pos):
	clkcir=False
	p=[]
	for p in ball_pos:
		if distance(p,pos)<BALL_RADIUS:
			clkcir=True
			break
	if clkcir:
		ball_pos.pop(ball_pos.index(p))
		# can also use ball_pos.remove(p)
	else:	
		ball_pos.append(list(pos))

frame=simplegui.create_frame("MUltiClick",WIDTH, HEIGHT)
frame.set_canvas_background("White")
frame.set_draw_handler(draw_circles)
frame.set_mouseclick_handler(mouseclicked)
frame.start()
