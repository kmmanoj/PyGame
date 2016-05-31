# template for "Stopwatch: The Game"
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
# define global variables
time="0:00.0"
unformatted_time=0
tenth=0
wins=0
lose=0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global tenth
    if t==0:
        return "0:00.0"
    tenth=t%10
    second=t//10
    minute=second//60
    second=second-minute*60
    if second<10:
        second="0"+str(second)
    else:
        second=str(second)
    
    return str(minute)+":"+second+"."+str(tenth)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
def stop():
    global wins, lose
    if timer.is_running():
        timer.stop()
        if unformatted_time%10==0:
            wins+=1
        else:
            lose+=1
def reset():
    global unformatted_time, wins, lose
    timer.stop()
    unformatted_time=0
    wins=0
    lose=0
# define event handler for timer with 0.1 sec interval
def timehandler():
    global unformatted_time
    unformatted_time+=1

# define draw handler
def drawhandle(canvas):
    canvas.draw_text(format(unformatted_time),(200,200),40, "white")
    canvas.draw_text(str(wins)+"/"+str(lose),(400,50),30,"green")
# create frame
frame=simplegui.create_frame("Stopwatch: The Game",500,500)

# register event handlers
frame.add_button("Start",start,100)
frame.add_button("Stop",stop,100)
frame.add_button("Reset",reset,100)
timer=simplegui.create_timer(100,timehandler)
frame.set_draw_handler(drawhandle)

# start frame
frame.start()

# Please remember to review the grading rubric
