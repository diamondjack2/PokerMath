# Module 3: Calculating Equity 🃏

**Status**: Completed ✅

### Calculating Equity
`find_equity()` takes in the flop from the board, the hero's hand, and the villain's range and calculates the equity in the hero's hand. 
Equity in this context just represents how often the hero's hand wins in the given scenario. 

**For Example:**
If equity is 14%, that means the hero wins that hand 14% of the time.

`estimate_equity()` estimates the equity via Monte Carlo simulation. Its use case is to save computation compared to `find_equity()` when evaluating many hands. 
How many iterations you run will lower or increase the amount of error.

The sweet spot for this case is around 10,000 iterations to save computing speed. 10,000 iterations has an average error below .5%.

### Verification:

`check_equity.py` is the verification file that checks 4 different values against known values to ensure proper output.

### How to run:
Simply run `python check_equity.py` to verify that each of the 4 values. The estimate should be in the ballpark of the given exact value less than .5%.