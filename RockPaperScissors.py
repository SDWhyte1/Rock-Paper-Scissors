import random
correctAnswer = True
playAgain = True
computerAnswer = ""
computerScore = 0
playerScore = 0
while playAgain:
    ranNum = random.randint(0,2) #0 = rock, 1 = paper, 2 = scissor
    if ranNum == 0:
        computerAnswer = "rock"
        playAgain = False
    elif ranNum == 1:
        computerAnswer = "paper"
        playAgain = False
    else:
        computerAnswer = "scissor"
        playAgain = False

    while correctAnswer:
        userAnswer = input("Please enter whether you are rock, paper or scissor: ")
        userAnswer = userAnswer.lower()
        if userAnswer == "rock" or userAnswer == "scissor" or userAnswer == "paper":
            print ("User has locked in their answer")
            correctAnswer = False
        else:
            print("Please enter a valid selection")
    if userAnswer == computerAnswer:
        print("We have a draw, both users chose " +userAnswer)
    elif userAnswer == "scissor" and computerAnswer == "paper":
        print("Player wins, " +userAnswer+ " beats " +computerAnswer)
        playerScore = playerScore +1
    elif userAnswer == "rock" and computerAnswer == "scissor":
        print("Player wins, " +userAnswer+ " beats " +computerAnswer)
        playerScore = playerScore +1
    elif userAnswer == "paper" and computerAnswer == "rock":
        print("Player wins, " +userAnswer+ " beats " +computerAnswer)
        playerScore = playerScore +1
    else:
        print("Computer wins, " +computerAnswer+ " beats " +userAnswer)
        computerScore = computerScore +1
        
    print("\n")
    playAgainQ = input("Would you like to play again (Please enter y or n)? ")
    if playAgainQ == "n":
        print("\n")
        print("Game over")
        print("Player score equals " +str(playerScore))
        print("Computer score equals " +str(computerScore))
        playAgain = False
    else:
        correctAnswer = True
        playAgain = True
        print("\n")
        print("Next game is starting now..........")
