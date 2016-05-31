# Implementation of classic arcade game Pong

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 800
HEIGHT = 500       
BALL_RADIUS = 15
PAD_WIDTH = 10
PAD_HEIGHT = 100
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
RIGHT = True

ball_vel=[2,2]
ball_pos=[WIDTH/2, HEIGHT/2]
paddle1_pos=HEIGHT/2
paddle2_pos=HEIGHT/2
paddle1_vel=0
paddle2_vel=0
score1=0
score2=-1

def restart():
    global score1, score2,ball_vel,paddle1_pos, paddle2_pos, RIGHT
    ball_vel=[2,2]
    ball_pos=[WIDTH/2, HEIGHT/2]
    paddle1_pos=HEIGHT/2
    paddle2_pos=HEIGHT/2
    score1=0
    score2=-1
    RIGHT = True
    new_game()

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel,ball_pos,ball_vel  # these are numbers
    global score1, score2  # these are ints
    ball_vel[1]=-2
    ball_pos=[WIDTH/2,HEIGHT/2]
    if RIGHT:
        ball_vel[0]=2
        score2+=1
    else:
        ball_vel[0]=-2
        score1+=1

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel, ball_pos, RIGHT
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # update ball
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
    
    if ball_pos[1]<BALL_RADIUS+PAD_WIDTH or ball_pos[1]>HEIGHT-PAD_WIDTH-BALL_RADIUS:
        ball_vel[1]=-ball_vel[1]
     
        
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "white", "white")
    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    canvas.draw_polygon([(0,paddle1_pos+HALF_PAD_HEIGHT),(HALF_PAD_WIDTH,paddle1_pos+HALF_PAD_HEIGHT),(HALF_PAD_WIDTH,paddle1_pos-HALF_PAD_HEIGHT),(0,paddle1_pos-HALF_PAD_HEIGHT)],PAD_WIDTH,"yellow")
    canvas.draw_polygon([(WIDTH-HALF_PAD_WIDTH,paddle2_pos+HALF_PAD_HEIGHT),(WIDTH,paddle2_pos+HALF_PAD_HEIGHT),(WIDTH,paddle2_pos-HALF_PAD_HEIGHT),(WIDTH-HALF_PAD_WIDTH,paddle2_pos-HALF_PAD_HEIGHT)],PAD_WIDTH,"red")
    
    # determine whether paddle and ball collide    
    if ball_pos[0]<BALL_RADIUS+PAD_WIDTH:
        if paddle1_pos-HALF_PAD_HEIGHT-BALL_RADIUS<ball_pos[1]<paddle1_pos+HALF_PAD_HEIGHT+BALL_RADIUS:
            ball_vel[0]=-ball_vel[0]
            ball_vel[1]-=random.randrange(0,2)
    if ball_pos[0]>WIDTH-PAD_WIDTH-BALL_RADIUS:
        if paddle2_pos-HALF_PAD_HEIGHT-BALL_RADIUS<ball_pos[1]<paddle2_pos+HALF_PAD_HEIGHT+BALL_RADIUS:
            ball_vel[0]=-ball_vel[0]
            ball_vel[1]+=random.randrange(0,2)
    if ball_pos[0]>WIDTH:
        RIGHT=False
        new_game()
    if ball_pos[0]<0:
        RIGHT=True
        new_game()
    
    # draw scores
    canvas.draw_text(str(score1),(WIDTH/4,HEIGHT/4),WIDTH/10,"yellow")
    canvas.draw_text(str(score2),(3*WIDTH/4,HEIGHT/4),WIDTH/10,"red")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel=-2
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel=-2
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel=2
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel=2

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["down"] or key==simplegui.KEY_MAP["up"]:
        paddle2_vel=0
    if key==simplegui.KEY_MAP["w"] or key==simplegui.KEY_MAP["s"]:
        paddle1_vel=0

def tick():
    global paddle1_pos, paddle2_pos, ball_vel
    inrangetop1=paddle1_pos>HALF_PAD_HEIGHT 
    inrangebot1=paddle1_pos<(HEIGHT-HALF_PAD_HEIGHT)
    inrangetop2=paddle2_pos>HALF_PAD_HEIGHT 
    inrangebot2=paddle2_pos<(HEIGHT-HALF_PAD_HEIGHT)
    if inrangetop1 and inrangebot1:
        paddle1_pos+=paddle1_vel
    elif not inrangetop1:
        paddle1_pos+=10
    else:
        paddle1_pos-=10
        
    if inrangetop2 and inrangebot2:
        paddle2_pos+=paddle2_vel
    elif not inrangetop2:
        paddle2_pos+=10
    else:
        paddle2_pos-=10
    if ball_vel[0]>0:
        ball_vel[0]+=0.002
    else:
        ball_vel[0]-=0.002
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_canvas_background("blue")
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart game",restart,100)
frame.add_label("CONTROLS: PLAYER1 : w s \nPLAYER2: up down")
timer=simplegui.create_timer(1,tick)

timer.start()
# start frame
new_game()
frame.start()
