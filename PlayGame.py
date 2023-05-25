from AbacoStack import AbacoStack,Card

def main(): #defining main function to run the game
    """
    function main: main function the run AbacoStack game
    Paramters: None
    Returns: None
    """
    #variable stacks to accept input from user for number of stacks
    stacks=int(input("Please enter the number of stacks between 2 and 5: "))
    while stacks<2 or stacks>5:
        stacks=int(input("Invalid input:please enter valid input:"))
    #variable depth to accept input from user for depth of stacks
    depth=int(input("Please enter the depth of stacks between 2 and 4: "))
    while depth<2 or depth>4:
        depth=int(input("Invalid input:please enter valid input:"))
        
    game_over=False
    card=Card(stacks,depth) #variable card to hold target card for user
    card.reset()
    
    user_card=AbacoStack(stacks,depth) #variable user_card to hold user's card
    
    while not game_over: #main loop to keep the game running
        user_card.show(card) 
        
        move=input("Enter your move(s) [Q for quit and R to reset]: ")
        
        if move.upper()=="Q":
            print("Quit game, goodbye...")
            game_over=True
        elif move.upper()=="R":
            user_card.reset()
        elif move[0].isdigit() and move[1].isalpha():
            moves=move.split()
            if len(moves)>5:
                moves=moves[:5]
            try:
                for x in moves:
                    user_card.moveBead(x)
            except Exception:
                print("Invalid move")
        else:
            print("Invalid move")
        
        if user_card.isSolved(card): #if condition to stop the game when both cards match
            user_card.show(card)
            print("Congratulations! Well done.")
            valid=False
            while not valid:
                reset=input("Would you like another game? [Y/N]: ")
                if reset.upper()=="Y":
                    user_card.reset()
                    card.reset()
                    valid=True
                if reset.upper()=="N":
                    print("Quit game, goodbye...")
                    game_over=True
                    valid=True
                else:
                    print("Invalid Input:"+str(reset))                
                
    
    

main()
    
    