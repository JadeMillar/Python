'''
The Objective of this program is to make a Rock, Paper, Scissors game
 for the user to play against the computer. 
 
@author: Jade Millar

'''

#import random

import random

#make a boolean variable called keepPlaying to track weather they want to 
#keep playing and set it to true
keepPlaying =True
#LOOP 1:Make a game loop that continues while keepPlaying is true.
while(keepPlaying):
    #Print out a statement to welcome the user to the game
    print("Welcome to the Rock Paper Scissors game!")
    print("best two out of three. Press 'q' to quit")
    #Make variables called userScore and cpuScore to track scores. Set to 0.
    cpuScore = 0
    userScore= 0
    #LOOP 2: make a round loop that continues while the userScore or cpuScore is less 
    #than 2
    while(userScore < 2 and cpuScore < 2):
        #LOOP 3: use input() to get a choice from the user (rock, paper, or scissors, q)
        #Store the choice in a variable. Use .lower() to make the users choice
        #all lower case
        choice = input("Please choose (Rock, Paper, Scissors):")

        
        #Make a list of choices, then use random. choice to get a random choice 
        #for the cpu. Store the choice in a variable. 
        choiceList = ["rock", "paper", "scissos"]
        cpuChoice = random.choice(choiceList)
        #Make a If/elif/else statement to check the users input against the 
        #cpu's choice:
        #NOTE: you will have to compare the users choice and the cpu choice to
        #"rock", "paper", "scissors" separately and combine with logical 
        #operators. EXAMPLE of a tie: 
        
        if((user =="rock" and cpu == "rock") or (user == "paper" and cpu == "paper") or  ( user == "scissors" and cpu == "scissors")):
            
            print ("DRAW")
            print(("User:" +str(userScore) +"CPU :" +str(cpuScore))

        #If the user won, add one to the users score, then print out the score 
        #"User : [#], CPU: [#]" 
        if((user=="paper"and cpu=="rock")or (user == "rock" and cpu ==
             "scissors") or (user == "scissors" and cpu == "paper")):
      
            print("User Won!")
            print(("User:" +str(userScore) +"CPU :" +str(cpuScore))
        #else if (elif) the computer won, then add one to the computer's score, then 
        #print out the scores...
        elif(cpuScore + 1):
            print("CPU Won!")
            print(("User:" +str(userScore) +"CPU :" +str(cpuScore))
        #else if it is a draw, print "DRAW", then print out the scores...
          if((user =="rock" and cpu == "rock") or (user == "paper" and cpu == "paper") or  ( user == "scissors" and cpu == "scissors")):
            
            print ("DRAW")
            print(("User:" +str(userScore) +"CPU :" +str(cpuScore))
        #else if the user enter( 'q', then end the round, and the game loop.
        #Use the break statement to end the round. Make keepPlaying equal false. 
        elif( choice.lower()== 'q'):
            keepPlaying = False
        #else the user didn't enter an accepted input, print "Not an option,
        #try again." 
        else:
            print("Not an option, try again")

    #print out the thank you message
    #print out who won:
    print("Thanks for playing!") 
    #if the userScore is 2, then the user won
        #code
    #elif the cpuScore is 2, then the cpu won    
        #code
        if(userScore == 2):
            print("user won!")
        elif(cpuScore == 2):
            print("cpu won!")
    #print out the final scores
         
            print ("DRAW")
            print(("User:" +str(userScore) +"CPU :" +str(cpuScore))