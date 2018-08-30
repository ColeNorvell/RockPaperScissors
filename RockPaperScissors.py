import random
import sys
#Greet
answer = raw_input("Would you like to play a game? ")
if answer == "yes":
	print ("Very well")
else:
	sys.exit("Have it as you may.")

currentGameNumber = 1
totalGamesToBePlayed = raw_input("HOW MANY GAMES? ")
totalGamesToBePlayed = int(totalGamesToBePlayed) # cast string variable as integer

while currentGameNumber <= totalGamesToBePlayed:
	#Ask question
	player = raw_input("Rock, paper, or scissors? ")

	#Generate computer's answer
	randomNumber = random.randint (1,3)
	if randomNumber == 1:
		enemy = "rock"
	if randomNumber == 2:
		enemy = "paper"
	if randomNumber == 3:
		enemy = "scissors"
	#Compare
	if player == "rock" and enemy == "paper":
		print ("PC chose paper")
		print ("You lost! Better luck next time!")
	if player == "rock" and enemy == "scissors":
		print ("PC chose scissors")
		print ("You won! Rock always works!")
	if player == "rock" and enemy == "rock":
		print ("PC chose rock")
		print ("You tied. I guess the enemy had the same strategy.")
	if player == "scissors" and enemy == "paper":
		print ("PC chose paper")
		print ("You won! Nice job!")
	if player == "scissors" and enemy == "scissors":
		print ("PC chose scissors")
		print ("You tied. Surprising. You know whats not surprising? 15 minutes could save you 15% or more on car insurance with Geico")
	if player == "scissors" and enemy == "rock":
		print ("PC chose rock")
		print ("You lost! You're pretty bad at this.")
	if player == "paper" and enemy == "paper":
		print ("PC chose paper")
		print ("You tied. End of story.")
	if player == "paper" and enemy == "scissors":
		print ("PC chose scissors")
		print ("You lost! A two year old is better at this than you.")
	if player == "paper" and enemy == "rock":
		print ("PC chose rock")
		print ("You won! Impressive, most impressive")
	currentGameNumber = currentGameNumber + 1
