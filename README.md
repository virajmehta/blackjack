Viraj Mehta
2015.8.1

This is my pass at writing a program that learns blackjack.

It was built from vanilla Python as a project that should ideally improve my facility with Python, ability to design software, and Blackjack knowledge.

It is implemented with a 3D grid of expected values for each dealer card, hand possibility, and blackjack play.  This grid is continually updated as more games are played and the algorithm's knowledge of how to play blackjack improves.  Nowhere in this algorithm is there any suggestion of what might be a good move in blackjack.

Currently, I am building in a few option and the output to a spreadsheet.

Future development might include card counting and variable betting, options in the ruleset a little larger than just number of decks (soft 17 rule, split rule, etc.).  

There are a couple know flaws in this (and I'm sure plenty of bugs to find!):

When you split, each hand gets a different allocation of post-hand dealer cards.
It can split as many times as the cards allow.