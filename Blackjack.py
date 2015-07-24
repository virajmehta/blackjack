import random
from deck import Deck





def readOptions():
	'''reads in the number of decks of cards so the model can have the correct state space'''
	pass

def setUpState(numDecks):
	'''	This function sets up the number of decks and the lengths of the simulation.'''

	return Deck(numDecks)
	

def setUpStats():
	'''This function sets up the record-keeping for the games'''
	pass

def runTrials(numGames):
	'''This function runs numGames iterations of BlackJack and saves the statistics in our stats module'''
	pass

def analyzeStats():
	'''This is where we make nice pretty numbers from the statistical garbage that will definitely exist earlier'''
	pass

def printResults():
	'''This function prints the results of the math that was done in this situation'''
	pass
	
def main():
	numDecks = 1
	numGames = 1
	readOptions()
	cardDeck = setUpState(numDecks)
	
	

	setUpStats()
	runTrials(numGames)
	analyzeStats()
	printResults()


if __name__ == "__main__":
    main()