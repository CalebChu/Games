#Imports--------------------------------------------------------------------------------------------------------------------------------------------------------
import time
import secrets
import random
import sys

#Misc--------------------------------------------------------------------------------------------------------------------------------------------------------
def Thinking(Text,Text2):
    print('\rThinking', end=" ")
    sys.stdout.flush()
    time.sleep(0.5)
    ...
    print('\rThinking.', end=" ")
    sys.stdout.flush()
    time.sleep(0.5)
    ...
    print('\rThinking..', end=" ")
    sys.stdout.flush()
    time.sleep(0.5)
    ...
    print('\rThinking...', end=" ")
    sys.stdout.flush()
    time.sleep(0.5)
    print('\r',Text, Text2, end= " ")

#Commands-----------------------------------------------------------------------------------------------------------------------------------------------------
#Games--------------------------------------------------------------------------------------------------------------------------------------------------------
class RPSGame:

    Playerscore = 0
    Programscore = 0
    program_options = ["rock", "paper", "scissors"]

    def getUserChoice(self):
        validInput = False
        while validInput == False:
            userChoice = input("What would you like to do?\nRock, Paper, or Scissors:").lower()
            if userChoice == "rock" or userChoice == "paper" or userChoice == "scissors":
                validInput = True
            else:
                print("Please choose from: rock, paper, or scissors")
                self.getUserChoice()
            return userChoice

    def getComputerChoice(self):
        ProgramChoice = random.choice(self.program_options)
        Thinking("The Computer chose", ProgramChoice)
        return ProgramChoice

    def judge(self, player, computer):
        if player == computer:
            print("\nIts a tie!\nYou both chose", player, ", the score remains the same.")
            return "tie"

        #winning scenarios
        if (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
            print("\n",player, " beats ", computer, "!  You win!")
            return "win"

        #losing scenarios
        if (computer == "rock" and player == "scissors") or (computer == "scissors" and player == "paper") or (computer == "paper" and player == "rock"):
            print("\n",computer, " beats ", player, "!  You lose!")
            return "lose"

    def calculateScore(self, outcome):
        if outcome == "win":
            self.Playerscore = self.Playerscore+1

        if outcome == "lose":
            self.Programscore = self.Programscore+1

    def printScore(self):
        print("The Score is now (Player):", self.Playerscore, "(Program):", self.Programscore)


    def playRound(self, currentRound):

        print("\n\nRound", currentRound, "!\n Ready?")
        time.sleep(1)
        print("Go!")
        userChoice = self.getUserChoice()
        computerChoice = self.getComputerChoice()
        outcome = self.judge(userChoice, computerChoice)


        self.calculateScore(outcome)
        self.printScore()

    def playRounds(self):
        self.printInstructions()

        currentRound = 1
        totalRounds = 3
        while currentRound <= totalRounds:
            self.playRound(currentRound)
            currentRound = currentRound+1

    def printInstructions(self):
        print("You chose 'Rock, Paper, Scissors'")
        time.sleep(1)
        print("\n\n\nWelcome to Rock, Paper, Scissors.")
        print("How to play: On your turn type: rock, paper, or scissors, then the program will go and whoever wins will get a point!\nYou play the rounds and who had the most by the end wins.")
        time.sleep(1)

#Menu--------------------------------------------------------------------------------------------------------------------------------------------------------
#Settings--------------------------------------------------------------------------------------------------------------------------------------------------------
#Run--------------------------------------------------------------------------------------------------------------------------------------------------------
game1 = RPSGame()
game1.playRounds()