Viraj Mehta
2015.8.1

This project is in Python 3.

This is my pass at writing a program that learns blackjack.

It was built from vanilla Python as a project that should ideally improve my facility with Python, ability to design software, and Blackjack knowledge.

It is implemented with a 3D grid of expected values for each dealer card, hand possibility, and blackjack play.  This grid is continually updated as more games are played and the algorithm's knowledge of how to play blackjack improves.  Nowhere in this algorithm is there any suggestion of what might be a good move in blackjack.

Currently, I am building in a few option and the output to a spreadsheet.

Future development might include:
card counting and variable betting 
options in the ruleset a little larger than just number of decks (soft 17 rule, split rule, etc.)
true randomness leveraging the RANDOM.ORG API 
after training, having the stats module play blackjack and finding how good it is!

There are a couple know flaws in this (and I'm sure plenty of bugs to find!):

When you split, each hand gets a different allocation of post-hand dealer cards.
It can split as many times as the cards allow.


Here's the current issue:

when you're on a lower number and you make a decision to hit, you get to another decision, where the learning algorithm tries again.  this is bad, because there's no guarantee it's gonna do the right thing.  Let me give an example: you're on H8 showing 7.  There's a chance here that the dealer will bust.  But you should probably hit.  So lets say the computer hits and youre on H18 showing 7 after a 10 draw.  Here there's a nonnegligible chance the algorithm chooses to hit again, irrevocably altering the expected value of the lower (correct) decision.  I think the fix is to make one test decision and then play the best possible strategy, which will eventually evolve to better play.

I'm not sure this explains why doubling isn't working properly, since it should not suffer from these problems
