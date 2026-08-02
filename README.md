Module 1: Building cards and poker hand combinations.

Status: Completed ☑️

Taking a dealt two-card hand, i.e., ('7s','Ah') [7 of spades, Ace of hearts], into a standard classification 'A7o'.
This math turns 1326 hand combinations into 169 different classes, which serve as the basis for further poker mathematics.

Card removal is the process of getting rid of combinations based upon which cards are known during any given hand. For example, if a board is ('Jd', '7s','2c') and the hero's hand is ('As','Js'), these 5 known cards eliminate certain combinations from being available. These two known Jacks take the possible combinations of JJ from 6 to just 1. Why? Because the deck contains 6 possible combinations of JJ: ('Js','Jh'), ('Js','Jd'), etc. After two Jacks are known, 'Jd' from the board and 'Js' from the hero's hand, that leaves ('Jc','Jh') as the only possible combination left.

This also makes the total combinations drop from 1326 to 1081. Each known card has 51 other cards it could pair with. Eliminating 51 combos per card [ 51 x 5 = 255 ]. This double counts how each known card could pair with each other [ (5x4)/2 = 10 ], so eliminating those double counts results in [ 255 - 10 = 245 ]. Thus, there are [ 1326 - 245 = 1081 ] combinations left. 

In cards.py, filter_live_combos() keeps all possible combinations left based on what cards are known. tally_combos() then counts how many combinations of each class are left.

Verification:

check_cards.py is the verification file that checks 17 different values against combinatorics worked by hand, including class counts under removal.

How to run:
Simply run python check_cards.py to verify that each of the 17 values pass. 


Roadmap:
1. Cards, Combinations, & Removal 
2. Adding Rules of the game (which hand wins)
3. Pot Odds, Ranges, Equity 
4. Bankroll Mgmt 
5. Hand History Parsing 
6. A Toy Solver 
7. Front End (AI assisted)
