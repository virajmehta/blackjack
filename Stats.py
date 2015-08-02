import random

class Entry:
	'''Contains a single entry in the matrix of games played. Starts with 10 to dampen the initial effect of games'''
	def __init__(self, isSplit):
		self.numPlayed = [10 for x in range(0, 3)] if isSplit else [10 for x in range(0, 4)]
		self.earnings = [0 for x in range(0, 3)] if isSplit else [0 for x in range(0, 4)]
		
		

	def addPlay(self, earnings, play):
		self.numPlayed[play] += 1
		self.earnings[play] += earnings

	def getExpectedValue(self, play):
		return self.earnings[play] / self.numPlayed[play]

	def randomize(self, probs):
		sumProb = 0
		for play in range(0, len(self.numPlayed)):
			sumProb += probs[play]
			probs[play] = sumProb
		myAss = random.random()

		for play in range(0, len(self.numPlayed)):
			if myAss < probs[play]:
				return play

		return -1

	def getNextPlay(self):
		
		expectedValue = []
		for play in range(0, len(self.numPlayed)):	#update EV
			expectedValue.append(self.getExpectedValue(play))

		probs = [0 for x in range(0, len(self.numPlayed))]
		remainingProb = 1.0


		for rank in range(len(self.numPlayed), 1, -1):
			minVal = 3 	#arbitrary big value
			minPlay = 5	#not a value
			for play in range(0, len(self.numPlayed)):
				if expectedValue[play] < minVal:
					minVal = expectedValue[play]
					minPlay = play
			expectedValue[minPlay] = 4 	#arbitrary bigger value
			probs[minPlay] = remainingProb / (rank * ((1 + minVal) ** 2))
			remainingProb -= probs[minPlay]

		for play in range(0, len(self.numPlayed)):
			if expectedValue[play] != 4:
				probs[play] = remainingProb
				break

		return self.randomize(probs)

	def getBestPlay(self):
		maxVal = -3  #smaller than any possible value
		maxPlay = -1 #invalid play
		for play in range(0, len(numPlayed)):
			val = self.getExpectedValue(play)
			if val > maxVal:
				maxVal = val
				maxPlay = play
		return maxPlay

class Stats:
	
	def __init__(self):
		self.history = {dealerCard : {playerCard : Entry(True) if playerCard > 28 else Entry(False) for playerCard in range(3, 39)} for dealerCard in range(1, 11)}
		#3-20 are hard 3-20, 21-28 are soft 13-20, and 29-38 are splittable pairs of A-10

	def getRandomPlay(self, playerCode, dealerCard):
		return self.history[dealerCard][playerCode].getNextPlay()

	def getCorrectPlayMatrix(self):
		return {dealerCard : {total : entry.getBestPlay() for total, entry in row} for dealerCard, row in self.history}

	def addPlay(self, playerCode, dealerCard, earnings, play):
		self.history[dealerCard][playerCode].addPlay(earnings, play)

		#TODO: figure out what else is needed from the stats app, fill out the rest of the blackjack game logic with a list of drawn cards, and fill out the rest of the 'business logic' of Blackjack.py
		
