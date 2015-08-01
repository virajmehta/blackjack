import sys
import random
from deck import Deck
from Stats import Stats




def readOptions():
	'''reads in the number of decks of cards so the model can have the correct state space'''
	argc = 0
	while argc < len(sys.argv):
		if sys.argv[argc] == '-d':
			numDecks = sys.argv[argc + 1]
			argc += 1
		elif sys.argv[argc] == '-n':
			numGames = sys.argv[argc + 1]
			argc += 1
		argc += 1

	


	


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
	cardDeck = Deck(numDecks)
	stats = Stats()
	

	runTrials(numGames, stats)
	analyzeStats()
	printResults()


if __name__ == "__main__":
    main()