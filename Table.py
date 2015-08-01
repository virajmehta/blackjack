from deck import Deck

class Table:
	'''Holds the cards on the table and draws them from the Deck'''

	def __init__(self, splitCount = 3):
		self.splitsLeft = splitCount
		self.ourAces = 0
		self.dealerAces = 0
		pass

	def decide(self, stats, playerHand, dealerShow):
		'''When given a set of parameters for the blackjack decision, decide returns the random value from stats that covers this scenario'''

		return stats.get



	def playOneGame(self, cardDeck, stats):
		'''Does the work of starting one game of blackJack using the given deck and making decisions based on the stats module'''
		playerHand = cardDeck.drawCard()
		if playerHand == 1:
			playerHand += 10
			self.ourAces += 1
		dealerCard = cardDeck.drawCard()
		if dealerCard == 1:
			dealerCard += 10
			self.dealerAces += 1
		nextCard = cardDeck.drawCard()
		if playerHand == 1:
			playerHand += 10
			self.ourAces += 1

		gameAfterDraw(self, cardDeck, playerHand, dealerCard)

		

	def gameAfterDraw(self, cardDeck, playerHand, dealerShow, bet = 1):
		'''After the initial card are drawn in playOneGame, gameAfterDraw manages the rest of the game.  This method should be essentially private.  
		It is separate so it can be recursively called'''
		stand = false
		decision = 0

		if self.ourAces == 2 and playerHand == 22:
			self.ourAces -= 1
			playerHand -= 10
		
		while playerHand <= 21:
			decision = self.decide(stats, playerHand, dealerShow)

			if decision == 0:#		stand
				break
			elif decision == 1:#	hit
				pass
			elif decision == 2:#	double
				pass
			elif decision ===3:#	split
				pass