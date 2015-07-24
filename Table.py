from deck import Deck

class Table:
	'''Holds the cards on the table and draws them from the Deck'''

	def __init__(self):
		pass

	def decide(self, stats, playerHand, dealerShow):
		pass

	def playOneGame(self, cardDeck, stats):
		bet = 1
		playerHand = cardDeck.drawCard() + cardDeck.drawCard()

		dealerShow = cardDeck.drawCard()

		stand = false
		decision = 0
		
		while playerHand <= 21:
			decision = self.decide(stats, playerHand, dealerShow)

			if decision == 0:
				break
			elif decision == 1:
