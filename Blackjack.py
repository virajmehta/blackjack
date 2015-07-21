
numDecks = 1
numGames = 1
deck
table
stats



def readOptions():
	'''reads in the number of decks of cards so the model can have the correct state space'''
	pass

def setUpState():
	'''	This function sets up the number of decks and the lengths of the simulation.'''
	pass

def setUpStats():
	'''This function sets up the record-keeping for the games'''
	pass

def runTrials(numGames):
	'''This function runs numGames iterations of BlackJack and saves the statistics in our stats module'''
	pass

def printResults():
	'''This function prints the results of the math that was done in this situation'''
	pass
	
def main():
	readOptions()
	setUpState()
	setUpStats()
	runtrials(numGames)
	analyzeStats()
	printResults()


if __name__ == "__main__":
    main()