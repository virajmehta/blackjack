import random

class Entry:
	'''Contains a single entry in the matrix of games played. Starts with 5 to dampen the initial effect of games'''
	def __init__(self, isSplit):
		self.numPlayed = [5 for x in range(0, 4)] if isSplit else [5 for x in range(0, 3)]
		self.earnings = [0 for x in range(0, 4)] if isSplit else [0 for x in range(0, 3)]
		
		

	def addPlay(self, earnings, play):
		self.numPlayed[play] += 1
		self.earnings[play] += earnings

	def getExpectedValue(self, play):
		return self.earnings[play] / float(self.numPlayed[play])

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

		maxVal = max(expectedValue)
		for rank in range(len(self.numPlayed), 1, -1):
			minVal = 3 	#arbitrary big value
			minPlay = 5	#not a value
			for play in range(0, len(self.numPlayed)):
				if expectedValue[play] < minVal:
					minVal = expectedValue[play]
					minPlay = play
			expectedValue[minPlay] = 4 	#arbitrary bigger value
			probs[minPlay] = remainingProb / (rank * ((1 + (maxVal - minVal)) ** 2))  #LOOK HERE THIS IS THE GUESSING ALGO
			remainingProb -= probs[minPlay]

		for play in range(0, len(self.numPlayed)):
			if expectedValue[play] != 4:
				probs[play] = remainingProb
				break

		return self.randomize(probs)

	def getBestPlay(self):
		maxVal = -3  #smaller than any possible value
		maxPlay = -1 #invalid play
		for play in range(0, len(self.numPlayed)):
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
		return {dealerCard : {playerCard : self.history[dealerCard][playerCard].getBestPlay() for playerCard in range(3, 39)} for dealerCard in range(1, 11)}

	def addPlay(self, playerCode, dealerCard, earnings, play):
		self.history[dealerCard][playerCode].addPlay(earnings, play)

	def getEVMatrix(self):
		matrix = []
		for dealerCard in range(1, 11):
			row = []
			for playerCard in range(3, 39):
				entry = self.history[dealerCard][playerCard]
				if len(entry.numPlayed) == 3:
					row.append('S:{:.3} H:{:.3} D:{:.3}        '.format(entry.getExpectedValue(0), entry.getExpectedValue(1), entry.getExpectedValue(2)))
				else:
					row.append('S:{:.3} H:{:.3} D:{:.3} L:{:.3}'.format(entry.getExpectedValue(0), entry.getExpectedValue(1), entry.getExpectedValue(2), entry.getExpectedValue(3)))
			matrix.append(row)
		return matrix

		
		
