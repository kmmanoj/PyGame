import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

pos=[400,300]
def draw(canvas):
    canvas.draw_circle(pos,5,20,"blue","blue")

def keydown(key):
    global pos
    vel=4
    if key==simplegui.KEY_MAP["up"]:
        pos[1]-=vel
    elif key ==simplegui.KEY_MAP["down"]:
        pos[1]+=vel
    elif key==simplegui.KEY_MAP["left"]:
        pos[0]-=vel
    elif key==simplegui.KEY_MAP["right"]:
        pos[0]+=vel
    
    
frame=simplegui.create_frame("THE ECHO",800,600)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.start()
