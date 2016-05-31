import random

#converts given name into its corresponding number
def name_to_number(name):
    number=-1
    if name=="rock":
        number=0
    elif name=="spock":
        number=1
    elif name=="paper":
        number=2
    elif name=="lizard":
        number=3
    elif name=="scissors":
        number=4
    else:
        print("invalid input")
    return number

#converts given umber into corrseponding name
def number_to_name(number):
    name=""
    if number==0:
        name="rock"
    elif number==1:
        name="spock"
    elif number==2:
        name="paper"
    elif number==3:
        name="lizard"
    elif number==4:
        name="scissors"
    else:
        print("invalid input")
    return name

#game
def rpsls(player_choice):
    print("Player chooses "+player_choice)
    comp_number=random.randrange(0,5)
    comp_choice=number_to_name(comp_number)
    print("Computer chooses "+comp_choice)
    player_number=name_to_number(player_choice)
    #in case of an invalid number , do not move ahead hence return 
    if player_number==-1 or player_choice=="":
        return
    difference=(comp_number-player_number)%5
    # when difference is 3,4 , player wins.
    # Computer wins, if it is 3,4
    # if the difference is 0 it is a tie
    if(difference>2.5):
        print("Player wins!")
    elif(difference==0):
        print("Player and computer tie!")
    else:
        print("Computer wins!")
    print("")
    return

#rpsls("stone")
rpsls("rock")
rpsls("paper")
rpsls("scissors")
rpsls("lizard")
rpsls("spock")

    
    
            
    
    
    
