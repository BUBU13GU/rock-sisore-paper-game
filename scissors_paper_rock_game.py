def win():
	print "you win from " + computerChoice
def lose():
	print "you lose from "+ computerChoice

index=0
while index<5:

	import random
	elementOfList=["paper","scissors","stone"]
	computerChoice=random.choice(elementOfList)


	playerChoice=raw_input("ente your choice from/ paper,scissors,stone ")


	if  playerChoice==computerChoice:
		print "draw!"

	elif playerChoice =="paper" and computerChoice == "stone":
		win()
	elif playerChoice == "scissors" and computerChoice == "paper":
		win()

	elif playerChoice == "stone" and computerChoice == "scissors":
		win()

	else:
		lose()
	index=index+1
