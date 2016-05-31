import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

secret_number=0
end=False
count=7
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    range100()

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number, count
    secret_number=random.randrange(0,100)
    count=7
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number, count
    secret_number=random.randrange(0,1000)
    count=10
    
def input_guess(guess):
    # main game logic goes here	
    global count
    guess=int(guess)
    print "Guess was "+str(guess)
    if guess < secret_number:
        print "higher"
    elif guess > secret_number:
        print "Lower"
    else:
        print "Correct"
        global end
        end=True
        found=True
    if(count==0):
        end=True
    count=count-1
    
    global i
    i.set_text("")
    
    if found:
        print "Congratulations! You found the Secret key!"
    elif end and not(found):
        print "Sorry! You ran out of guesses!"
    
    new_game()
# create frame
frame=simplegui.create_frame("Guess the number!", 400,400)

# register event handlers for control elements and start frame
frame.add_button("Range 0-100",range100,200)
frame.add_button("Range 0-1000",range1000,200)
i=frame.add_input("Guess",input_guess,200)
# call new_game 
new_game()
frame.start()

# always remember to check your completed program against the grading rubric
