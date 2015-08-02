import os
import sys
import random
from deck import Deck
from Stats import Stats
from Table import Table
import datetime
import csv
from itertools import izip
import argparse
import pdb

#weaknesses: no limit on splits, new dealer draw for every split hand after the original card, no bet modulation


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

	parser = argparse.ArgumentParser(description='Blackjack Learning System.')
	parser.add_argument('numGames', default=100, type=int, nargs='?')
	parser.add_argument('numDecks', default=4, type=int, nargs='?')
	return parser.parse_args(sys.argv[1:])

	


	


def runTrials(numGames, stats, table, deck):
	'''This function runs numGames iterations of BlackJack and saves the statistics in our stats module'''
	for game in range(0, numGames):
		table.playOneGame(deck, stats)
		#if table.games != game + 1:
			#pdb.set_trace()
		if deck.tillShuffle <= 0:
			deck.cleanShuffle()


def analyzeStats(stats):
	'''This is where we make nice pretty numbers from the statistical garbage that will definitely exist earlier'''

	results = stats.getCorrectPlayMatrix()
	now = datetime.datetime.today()
	name = 'results/Blackjack {}.{}.{}.{}.{}.{}.csv'.format(now.year, now.month, now.day, now.hour, now.minute, now.second)
	fileOutput = open('temp.csv', 'wb')

	writer = csv.writer(fileOutput, dialect='excel')
	plays = {0 : 'S', 1 : 'H', 2 : 'D', 3 : 'L'}
	for dealerCard in results:
		encodedPlays = [plays[results[dealerCard][hand]] for hand in range(3, 39)]
		writer.writerow(encodedPlays)

	fileOutput.close()
	pivotData = izip(*csv.reader(open('temp.csv', 'rb')))
	csv.writer(open(name, 'wb')).writerows(pivotData)


	os.remove('temp.csv')
	return name 

def printResults():
	'''This function prints the results of the math that was done in this situation'''
	pass
	
def main():
	options = readOptions()
	cardDeck = Deck(options.numDecks)
	stats = Stats()
	table = Table()
	

	runTrials(options.numGames, stats, table, cardDeck)
	name = analyzeStats(stats)
	print('SUCCESS!\nGames Played: {}\nNet Earnings: {}\nNet Single-game Expected Value: {}\nFull results written to file {}'.format(table.games,
		 table.earnings, table.earnings / table.games, name))
	return

if __name__ == "__main__":
    main()