import numpy
import random

class Entry:
	'''Contains a single entry in the matrix of games played. Starts with 10 to dampen the initial effect of games'''
	def __init__(self, isSplit):
		self.numPlayedHit = 10
		self.earningsHit = 0
		self.numPlayedStand = 10
		self.earningsStand = 0
		self.numPlayedDouble = 10
		self.earningsDouble = 0
		self.numPlayedSplit = 10 if isSplit else 0
		self.earningsSplit = 0

	def addPlay(self, earnings):
		self.numPlayed += 1
		self.earnings += earnings

	def getExpectedValue(self):
		return self.earnings / self.numPlayed

	def getNextPlay(self):
		

class Stats:
	
	def __init__(self):
		