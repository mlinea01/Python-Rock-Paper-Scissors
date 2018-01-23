#Initializes the variables to 0 to start the game.
leaveGame = 0;
player1 = int(0);
player2 = int(0);

#The program will continue until the variable leaveGame equals q
#If you want to continue press enter
while leaveGame != "q":
    import random

    #Displays the score starting at 0 to 0
    #Tells the user to enter 1, 2, or 3 for Rock, Paper, or Scissors to start the game
    print("Player 1: ", player1, " Player 2: ", player2)
    print("Enter 1 for Rock, 2 for Paper, or  3 for Scissors")

    #Sets the choice variable to an int that can be input into the game for user to choose Rock, Paper, or Scissors.
    #Sets the computer to choose a random number ranging from 1 to 3.
    choice = int(input())
    computerChoice = random.randint(1,3)

    #If the users choice matches the computers choice it won't affect the score
    #and will alert the user that the match was a tie.
    #At the end of this if block, it will ask the user if he/she would like to play again.
    if choice == computerChoice:
        print("Player 1: ",player1," Player 2: ",player2)
        print("Tie!")
        print("press q to quit or press Enter to play again!")
        leaveGame = input()

    #This else if block executes whenever the computer wins the game.
    #when the computer wins, the user will be alerted of the choices each player made, and that they lost the match.
    #At the end of this else if statement 1 will be added to player twos score, display the score to the screen
    #and will ask the user if he/she would like to play again.
    elif (choice == 1 and computerChoice == 2) or (choice == 2 and computerChoice == 3) or (choice == 3 and computerChoice == 1):
        if choice == 1:
            print("You chose Rock and computer chose Paper, You Lose!")

        if choice == 2:
            print("You chose Paper and computer chose Scissors, You Lose!")

        if choice == 3:
            print("You chose Scissors and computer chose Rock, You Lose!")

        player2 += 1
        print("Player 1: ", player1, " Player 2: ", player2)
        print("press q to quit or press Enter to play again!")
        leaveGame = input()

    #This else if block executes whenever the user wins the game.
    #When the user wins, the user will be alerted of the choices each player made, and that they won the match.
    #At the end of this else if statement 1 will be added to player ones score, displayed to the screen
    #and will ask the user if he/she would like to play again.
    else:
        if choice == 1:
            print("You chose Rock and computer chose Scissors, You Win!")

        if choice == 2:
            print("You chose Paper and computer chose Rock, You Win!")

        if choice == 3:
            print("You chose Scissors and computer chose Paper, You Win!")

        player1 += 1
        print("Player 1: ", player1, " Player 2: ", player2)
        print("press q to quit or press Enter to play again!")
        leaveGame = input()

