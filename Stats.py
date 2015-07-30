import numpy
import random

class Entry:
	'''Contains a single entry in the matrix of games played. Starts with 10 to dampen the initial effect of games'''
	def __init__(self):
		self.numPlayed = [10 for x in range(0, 4)]
		self.earnings = [0 for x in range(0, 4)]
		
		

	def addPlay(self, earnings, play):
		self.numPlayed[play] += 1
		self.earnings[play] += earnings

	def getExpectedValue(self, play):
		return self.earnings[play] / self.numPlayed[play]

	def randomize(self, probs):
		sumProb = 0
		for play in range(0, 4):
			sumProb += probs[play]
			probs[play] = sumProb
		myAss = random.random()

		for play in range(0, 4):
			if myAss < probs[play]
				return play

		return -1

	def getNextPlay(self):
		
		expectedValue = []
		for play in range(0, 4):	#update EV
			expectedValue.append(self.getExpectedValue(play))

		probs = [0 for x in range(0, 4)]
		remainingProb = 1.0


		for rank in range(4, 1, -1):
			minVal = 3 	#arbitrary big value
			minPlay = 4	#not a value
			for play in range(0, 4):
				if expectedValue[play] < minVal:
					minVal = expectedValue[play]
					minPlay = play
			expectedValue[minPlay] = 4 	#arbitrary bigger value
			probs[minPlay] = remainingProb / (rank * ((1 + minVal) ** 2))

		for play in range(0, 4):
			if expectedValue[play] != 4:
				probs[play] = remainingProb
				break

		return self.randomize(probs)
		


class Stats:
	
	def __init__(self):
		table = [[Entry() for total in range(3, 38)] for dealerCard in range(1, 10)]
		#3-20 are hard 3-20, 21-28 are soft 13-20, and 29-38 are splittable pairs of A-10

		#TODO: figure out what else is needed from the stats app, fill out the rest of the blackjack game logic with a list of drawn cards, and fill out the rest of the 'business logic' of Blackjack.py
		