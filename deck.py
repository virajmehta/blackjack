import random

class Deck:
	'''Holds the state of the decok of Cards for the simulation'''

	def cleanShuffle(self):
		'''Clears the cardList and replaces it with a full, newly shuffled deck of cards'''
		self.cardList = []
		#initializing card list in deck
		for deck in range(0, self.numDecks):
			for card in range (1, 10):
				self.cardList.append(card)

			for i in range(0, 4):
				self.cardList.append(10)

		#Shuffle the deck at the start
		random.shuffle(self.cardList)
		self.tillShuffle = int(self.numDecks * 52 * random.uniform(0.6, 0.8))

	def __init__(self, numDecks):
		self.tillShuffle = int(numDecks * 52 * random.uniform(0.6, 0.8))
		self.cardList = []
		self.numDecks = numDecks
		self.cleanShuffle()

	def drawCard(self):
		self.tillShuffle -= 1

		return self.cardList.pop()
		
