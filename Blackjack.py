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
'''
Blackjack Learning System
Viraj Mehta
August 2015

Blackjack.py is an attempt to write a program that learns to play blackjack by working through the game of blackjack and seeing which guesses work well.

It takes the parameters numGames, the number of iterations of blackjack, and numDecks, the number of decks. 

It outputs a csv timestamped with its blackjack strategy inside.
'''

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
	parser.add_argument('-v', action='store_true')
	return parser.parse_args(sys.argv[1:])

	


	


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
	name = 'results/Blackjack {}.{}.{}.{}.{}.{}.csv'.format(now.year, now.month, now.day, now.hour, now.minute, now.second)
	fileOutput = open('temp.csv', 'wb')

	writer = csv.writer(fileOutput, dialect='excel')
	plays = {0 : 'S', 1 : 'H', 2 : 'D', 3 : 'L'}
	for dealerCard in results:
		encodedPlays = [plays[results[dealerCard][hand]] for hand in range(3, 39)]
		writer.writerow(encodedPlays)

	fileOutput.close()
	rowHeadings = ['H{}'.format(i) if i <= 20 else 'S{}'.format(i - 8) if i <= 29 else 'P{}'.format((i - 28) * 2) for i in range(3, 38)]
	pivotData = izip(rowHeadings, *csv.reader(open('temp.csv', 'rb')))
	newFile = open(name, 'wb')
	writer = csv.writer(newFile, dialect='excel')
	writer.writerow([i for i in range(0, 11)])
	writer.writerows(pivotData)
	os.remove('temp.csv')
	newFile.close()
	return name 

def outputEV(stats, name):
	newName = name[:-4] + 'EV.csv'
	fileOutput = open(newName, 'wb')
	writer = csv.writer(fileOutput, dialect='excel')
	writer.writerow([i for i in range(0, 11)])
	rowHeadings = ['H{}'.format(i) if i <= 20 else 'S{}'.format(i - 8) if i <= 29 else 'P{}'.format((i - 28) * 2) for i in range(3, 38)]
	matrix = stats.getEVMatrix()
	pivotData = izip(rowHeadings, *matrix)
	writer.writerows(pivotData)
	fileOutput.close()
	print('Expected Values for each hand output to {}'.format(newName))
	return


def printResults(name, table):
	'''This function prints the results of the math that was done in this situation'''
	print('SUCCESS!\nGames Played: {}\nNet Earnings: {}\nNet Single-game Expected Value: {}\nFull results written to file {}'.format(table.games,
		 table.earnings, table.earnings / table.games, name))

	
def main():
	options = readOptions()
	cardDeck = Deck(options.numDecks)
	stats = Stats()
	table = Table()
	runTrials(options.numGames, stats, table, cardDeck)
	name = analyzeStats(stats)
	printResults(name, table)
	if options.v:
		outputEV(stats, name)
	return

if __name__ == "__main__":
    main()