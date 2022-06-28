def win():
	print ("you win from " + computerChoice)
def lose():
	print ("you lose from "+ computerChoice)

index=0
while index<5:

	import random
	elementOfList=["paper","scissors","rock"]
	computerChoice=random.choice(elementOfList)


	playerChoice=input("ente your choice from/ paper,scissors,rock")


	if  playerChoice==computerChoice:
		print ("draw!")

	elif playerChoice =="paper" and computerChoice == "rock":
		win()
	elif playerChoice == "scissors" and computerChoice == "paper":
		win()

	elif playerChoice == "rock" and computerChoice == "scissors":
		win()

	else:
		lose()
	index=index+1
