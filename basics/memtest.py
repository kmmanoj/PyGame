import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
numbers=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
state=[]
for i in range(16):
	state.append(0)
COMMON_COLOR="Yellow"
SHOW_COLOR="Blue"
tw_turns=0
prev=[]
count=0

def newgame():
	global state, tw_turns,SHOW_COLOR, count, prev
	for i in range(16):
		state[i]=0
	tw_turns=0
	SHOW_COLOR="Blue"
	prev=[]
	count=0
	random.shuffle(numbers)

def drawbox(canvas):
	global SHOW_COLOR
	win=True
	for factor in range(0,16):
        	bound=factor*50
		if state[factor]==0:
	      		canvas.draw_polygon([(bound,0),(bound,100),(bound+50,100),(bound+50,0)],1,"Black",COMMON_COLOR)
			win=False
		else:
			canvas.draw_polygon([(bound,0),(bound,100),(bound+50,100),(bound+50,0)],1,"Black",SHOW_COLOR)
        	canvas.draw_text(str(numbers[factor]),[bound+12,62],50,COMMON_COLOR)
	if win and SHOW_COLOR!="Green":
		SHOW_COLOR="Green"
	global label
	label.set_text("Turns = "+str(tw_turns//2))
	if win:
		label.set_text("Turns = "+str(tw_turns//2)+" GAME OVER")

def cardhit(pos):
	global prev, count, state, tw_turns
	n=pos[0]//50
	if state[n]==0:
		state[n]=1
		if count==0:
			prev.append(n)
			count+=1
		elif count==1:
			if numbers[n]==numbers[prev[0]]:
				state[n]=2
				state[prev[0]]=2
				prev=[]
				count=-1
			else:
				state[n]=1
				prev.append(n)
			count+=1
		elif count==2:
			for i in prev:
				state[i]=0
			prev=[]
			prev.append(n)
			count=1
		tw_turns+=1

frame=simplegui.create_frame("Memory Test",800,100)
frame.add_button("RESTART",newgame)
frame.set_draw_handler(drawbox)
frame.set_mouseclick_handler(cardhit)
label=frame.add_label("Turns = 0") 
newgame()
frame.start()
