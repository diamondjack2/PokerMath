# The Poker Trainer Engine 🂮
This is the math engine behind my mobile app, Poker Trainer - SuitedUp. It generates random poker scenarios and grades the mathematically optimal decision a player should take.

This code and repo is not AI generated, and all math is verified by hand and 3rd party checks.

### Module 1:
Covers generating a deck, all possible hand combinations, card removal, and combinatorics.

Check it out [here](docs/module-1-cards.md).

### Module 2:
Covers turning random cards into the game of poker. It turns 7 random cards into poker ranks ie: Flush, Two-Pair, etc.

Check it out [here](docs/module-2-evaluator.md).

### Module 3:
Covers calculating exact and estimated equity in a specific poker hand. It takes a flop, the hero's cards, and the villain's range to calculate the hero's equity.
It serves as the foundational piece for grading mathematically optimal decisions in the game.

Check it out [here](docs/module-3-equity.md).

### Module 4:
Covers preflop ranges. It expands poker shorthand like `"22+, ATs+, KQo"` into the actual hands it describes, converts those into card combinations, and looks up the right preflop chart for a given position and action. This is what feeds villain's range into the equity engine, and what the preflop trainer grades against.

Check it out [here](docs/module-4-ranges.md).


### How to run"
python check_cards.py
python check_evaluator.py
python check_equity.py

### Modules:
1. Cards, Combinations, & Removal ✅
2. Rules of the game (Hand Evaluation) ✅
3. Equity ✅
4. Ranges ✅
5. Pot Odds & Grading
4. Spot Generator