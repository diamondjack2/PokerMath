# Module 2: Building the hand evaluator engine. 🃏

**Status**: Completed ✅

### Hand Evaluation
`evaluate_hand()` takes in a seven card tuple ie: `('As','Ad','Ah','Ac','Ts','Th','7c')` and evaluates it into poker hand ranks. Determine the hands strength like if its a Four of Kind, Two-Pair, etc. The evaluator returns a tuple of numbers representing a hand strength rating mapped to a number. For example the last hand would return `(8,12,8)` decoded as `(8 = Four of Kind, 12 = Ace High, 8 = Ten Kicker)`. 

A tuple serves well here because it makes comparing hands to each other easier. `(0,1) > (1,0)` returns `False` because it checks by index. So having each hand strength mapped to a number in the first position of the tuple makes comparing a table simple. 

In this evaluator, the higher the number the better. 

**Poker Hand Map:**
9 : Straight Flush
8 : Four of Kind
7 : Full House
6 : Flush
5 : Straight
4 : 3 of Kind
3 : Two Pair 
2 : Pair 
1 : High Card

### Hand Comparison
`compare_hands()` takes in a list of outputs from `evaluate_hand()` and returns which index value had the strongest hand. In pots where two players have equally strong hand value (a chop) the function returns multiple values `[0,1]`. These index value represent seat position at a table. 

**For Example:**
The function takes in a list `[(8,12,9),(7,12,5)]` these are two hands that went through `evaluate_hand()`; It would then return `[0]` because the player at index value 0 has the strongest hand from this list. 

### Verification:

`check_evaluator.py` is the verification file that checks 17 different values against known values to ensure proper output and a test 100,000 randomly generated spots against a open-source poker library `import treys`. 

### How to run:
Simply run `python check_evaluator.py` to verify that each of the 17 values pass & treys output match the evaluator. 
