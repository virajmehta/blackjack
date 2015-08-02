import sys
import random
from deck import Deck
from Stats import Stats
from Table import Table
import datetime
import csv
import argparse
#import pdb

#weaknesses: no limit on splits, new dealer draw for every split hand after the original card, no bet modulation


def readOptions():
	'''reads in the number of decks of cards so the model can have the correct state space'''
	parser = argparse.ArgumentParser(description='Blackjack Learning System.')
	


	


def runTrials(numGames, stats, table, deck):
	'''This function runs numGames iterations of BlackJack and saves the statistics in our stats module'''
	for game in range(0, numGames):
		table.playOneGame(deck, stats)
		if deck.tillShuffle <= 0:
			deck.cleanShuffle()


def analyzeStats(stats):
	'''This is where we make nice pretty numbers from the statistical garbage that will definitely exist earlier'''

	results = stats.getCorrectPlayMatrix()
	now = datetime.datetime.today()
	name = 'Blackjack {}.{}.{}.{}.{}.{}.csv'.format(now.year, now.month, now.day, now.hour, now.minute, now.second)
	fileOutput = open(name, 'wb')

	writer = csv.writer(fileOutput, dialect='excel')
	plays = {0 : 'S', 1 : 'H', 2 : 'D', 3 : 'L'}
	for dealerCard in results:
		encodedPlays = [plays[results[dealerCard][hand]] for hand in range(3, 39)]
		writer.writerow(encodedPlays)

	fileOutput.close()


	return name 

def printResults():
	'''This function prints the results of the math that was done in this situation'''
	pass
	
def main():
	numDecks = 4
	numGames = 1
	readOptions()
	cardDeck = Deck(numDecks)
	stats = Stats()
	table = Table()
	

	runTrials(numGames, stats, table, cardDeck)
	name = analyzeStats(stats)
	print('SUCCESS!\nGames Played: {}\nNet Earnings: {}\nNet Single-game Expected Value: {}\nFull results written to file {}'.format(table.games,
		 table.earnings, table.earnings / table.games, name))
	return

if __name__ == "__main__":
    main()