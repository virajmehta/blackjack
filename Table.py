from deck import Deck

class Table:
	'''Holds the cards on the table and draws them from the Deck'''

	def __init__(self):
		self.ourAces = 0
		self.dealerAces = 0
		self.games = 0
		self.earnings = 0
		pass

	def decide(self, stats, playerHand, dealerShow):
		'''When given a set of parameters for the blackjack decision, decide returns the random value from stats that covers this scenario'''

		return stats.get

	def addCard(self, playerHand, nextCard):
		'''returns the table value for the hand that results from a given card being added to a hand.  returns -1 if bust. returns 0 if the value is 21'''

		if playerHand >= 29:  	#SPLIT HAND REMOVAL CENTER
			playerHand -= 28 #split encoding
			playerHand *= 2


		if playerHand >= 21 and playerHand <= 28: 	#SOFT HAND (13-20)
			playerHand += nextCard
			if playerHand < 29:
				return playerHand
			else:
				return playerHand - 8 - 10 #8 for removing soft encoding and 10 for hardening the ace

		if nextCard == 1 and playerHand + 11 < 21:
			return nextCard + 11 + 8 #11 for soft ace and 8 for soft encoding

		if nextCard == 1 and playerHand + 11 == 21:	#SOFT 21
			return 0

		if nextCard + playerHand == 21:	#regular 21
			return 0

		playerHand += nextCard

		return playerHand if playerHand < 21 else -1


	def dealerPlay(self, cardDeck, dealerCard):
		'''Runs the dealer's side of the game after the initial draw and play of the players.  returns a value or returns a -1 for bust'''
		soft = dealerCard == 1
		if soft: 
			dealerCard += 10

		
		while dealerCard <= 21:
			if (not soft and dealerCard > 16) or dealerCard > 17:  #Dealer hits on soft 17
				return dealerCard
			nextCard = cardDeck.drawCard()
			if nextCard == 1 and dealerCard + 11 <= 21:
				soft = True
				nextCard += 10
			dealerCard += nextCard
			if dealerCard > 21 and soft:
				soft = False
				dealerCard -= 10
			

		return -1





	def playOneGame(self, cardDeck, stats):
		'''Does the work of starting one game of blackJack using the given deck and making decisions based on the stats module'''
		playerHand = cardDeck.drawCard()
		dealerCard = cardDeck.drawCard()
		secondCard = cardDeck.drawCard()

		if (playerHand == 1 and secondCard == 10) or (playerHand == 10 and secondCard == 1):	#BLACKJACK MOTHERFUCKERS
			self.games += 1
			self.earnings += 1.5
			return

		if playerHand == secondCard:
			playerHand *= 2
			playerHand += 28 #split encoding

		elif playerHand == 1 or secondCard == 1:
			playerHand += 10 + secondCard + 8 #8 for soft encoding, 10 for softening the ace

		else:
			playerHand += secondCard

		self.gameAfterDraw(cardDeck, playerHand, dealerCard, stats, True)

	def record(self, playerHand, dealerCard, play, stats, earnings, orig = False):
		if orig:
			self.games += 1
			self.earnings += earnings
		stats.addPlay(playerHand, dealerCard, earnings, play)

	def getEarnings(self, playerHand, dealer, bet):
		if dealer == -1 or playerHand > dealer:
			return bet
		elif dealer == playerHand:
			return 0
		else:
			return -1 * bet


	def gameAfterDraw(self, cardDeck, playerHand, dealerCard, stats, canDouble = False, bet = 1):
		'''After the initial card are drawn in playOneGame, gameAfterDraw manages the rest of the game.  This method should be essentially private.  
		It is separate so it can be recursively called'''

		play = stats.getRandomPlay(playerHand, dealerCard)
		while not canDouble and play == 2:
			play = stats.getRandomPlay(playerHand, dealerCard)

		if play == 0:											#STAND
			dealer = self.dealerPlay(cardDeck, dealerCard)
			earnings = self.getEarnings(playerHand, dealer, bet)
			self.record(playerHand, dealerCard, play, stats, earnings, True)
			return earnings

		if play == 1:											#HIT
			newHand = self.addCard(playerHand, cardDeck.drawCard())
			if newHand == 0:		#total = 21
				dealer = self.dealerPlay(cardDeck, dealerCard)
				earnings = self.getEarnings(21, dealer, bet)
				self.record(playerHand, dealerCard, play, stats, earnings, True)
				return earnings
			elif newHand == -1:	#player bust
				earnings = bet * -1
				self.record(playerHand, dealerCard, play, stats, earnings, True)
				return earnings
			else:					#continue playing
				earnings = self.gameAfterDraw(cardDeck, newHand, dealerCard, stats, bet)
				self.record(playerHand, dealerCard, play, stats, earnings)
				return earnings
		if play == 2:											#DOUBLE
			newHand = self.addCard(playerHand, cardDeck.drawCard())
			if newHand == -1:	#BUST
				earnings = bet * -2
				self.record(playerHand, dealerCard, play, stats, earnings, True)
				return earnings
			elif newHand == 0: #total = 21
				dealer = self.dealerPlay(cardDeck, dealerCard)
				earnings = self.getEarnings(21, dealer, bet * 2)
				self.record(21, dealerCard, play, stats, earnings, True)
				return earnings
			else:					#not bust
				dealer = self.dealerPlay(cardDeck, dealerCard)
				earnings = self.getEarnings(playerHand, dealer, bet * 2)
				self.record(playerHand, dealerCard, play, stats, earnings, True)
				return earnings
		if play == 3:											#SPLIT
			playerHand -= 28 #remove split encoding
			hand1 = self.addCard(playerHand, cardDeck.drawCard())
			hand2 = self.addCard(playerHand, cardDeck.drawCard())
			earnings = self.gameAfterDraw(cardDeck, hand1, dealerCard, stats, True) + self.gameAfterDraw(cardDeck, hand2, dealerCard, stats, True)
			self.record(playerHand + 28, dealerCard, play, stats, earnings)
			self.games -= 1
			return earnings





	
