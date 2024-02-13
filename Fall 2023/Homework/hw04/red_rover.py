"""
File:    red_rover.py
Author:  Pooja Rajamanikandan
Date:    10/02/2023
Section: 54
E-mail:  le64534@umbc.edu
Description: The programs is used to play a game of Red Rover
"""
if __name__ == "__main__":
    
    red_team = list()  #Initiates the red_team list 
    blue_team = list() #Initiates the blue_team list 
    winner = False     #Sets winner to fasle since games hasn't started  
    team_member = ""   #Initiates
    coin = 1           #A counter to switch between turns of each team
    
    #Alternates between the two teams to add players 
    while team_member != "start game":
        team_member = input("Who should we add to the Red team? ")
        red_team.append(team_member)
        if "start game" in red_team:
            red_team.remove("start game")
        
        #To stop adding players once the game has started 
        if team_member != "start game":
            team_member = input("Who should we add to the Blue team? ")
            blue_team.append(team_member)
            if "start game" in blue_team:
                blue_team.remove("start game")
                
        #To ensure both teams have equal amount of players        
        if len(red_team) > len(blue_team):
            red_team.pop(-1)
        if len(red_team) < len(blue_team):
            blue_team.pop(-1)
        
    #The games only if there are no winner yet    
    while winner == False and len(red_team) == len(blue_team):
        
        #Ask Red team their choices while its their turn
        if team_member == "start game" or coin == 1:
            person_sent_over = input("Who should Red team send over? ")
            
            #displays Team members
            if person_sent_over == "display":
                print("The Red Team is composed of: ")
                for x in red_team:
                    print(x,end=", ")
                person_sent_over = input("Who should Red team send over? ")
            
            #Determines if the person made it through the line
            if person_sent_over in red_team:
                break_through = input("Did they make it through the line? ")
                if break_through == "yes":
                    print(person_sent_over,"stays on Red team")
                if break_through == "no":
                    print(person_sent_over,"change to Blue team")
                    blue_team.append(red_team.remove(person_sent_over))
                    
            coin = 2 #Change to Blue team's turn
            
        #Ask Blue team their choices while its their turn
        if coin == 2:
            person_sent_over = input("Who should Blue team send over? ")
            
            #displays Team members
            if person_sent_over == "display":
                print("The Blue Team is composed of: ")
                for x in blue_team:
                    print(x,end=", ")
                person_sent_over = input("Who should Blue team send over? ")
                
            #Determines if the person made it through the line
            if person_sent_over in blue_team:
                break_through = input("Did they make it through the line? ")
                if break_through == "yes":
                    print(person_sent_over,"stays on Blue team")
                if break_through == "no":
                    print(person_sent_over,"change to Blue team")
                    red_team.append(blue_team.remove(person_sent_over))
                    
            coin = 1 #Change to Red team's turn
        
        #Checks for a winner and determines who it is
        if len(red_team) <= 1 or len(blue_team) <= 1:
            winner = True
            if len(red_team) > len(blue_team):
                print("The Red Team has won")
            if len(red_team) < len(blue_team):
                print("The Blue Team has won")