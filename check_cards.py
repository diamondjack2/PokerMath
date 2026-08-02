""" This helper file checks that cards.py math is correct when counting and generating cards and combos."""

import cards

KNOWN_CARDS = ('Jd', '7s','2c','As','Js')
CLASS_CHECK = {'JJ':1,'AA':3,'77':3,'22':3,'KK':6,'AJs':2,'AJo':4,'AKs':3,'AKo':9,'KQo':12}
EXP_DECK = 52
EXP_COMBOS = 1326
EXP_TALLY_KEYS = 169
EXP_TALLY_SET = {4,6,12}
EXP_TALLY_SUM = 1326
EXP_LIVE_COMBOS = 1081
EXP_LIVE_TALLY_SUM = 1081

# -- Helper Function ---

def helper_check(expected_value, value, description:str):
    if expected_value == value:
        print(f'{description}: Pass')
    else:
        print(f'{description}: Failed - expected {expected_value}, got {value}')
    
    return expected_value == value

# -- Running Helper Function ---
if __name__ == "__main__":

    tally = cards.tally_combos(cards.ALL_COMBOS)
    live_filter = cards.filter_live_combos(cards.ALL_COMBOS, known_cards=KNOWN_CARDS)
    live_tally = cards.tally_combos(live_filter)
    
    deck_length = len(set(cards.DECK))
    combos_length = len(cards.ALL_COMBOS)

    tally_key_length = len(tally.keys())
    tally_set = set(tally.values())
    tally_sum = sum(tally.values())

    live_filter_len = len(live_filter)
    live_tally_sum = sum(live_tally.values())
    live_tally_keys = len(live_tally.keys())

    summary = []

    summary.append(helper_check(EXP_DECK, deck_length, 'deck size'))
    summary.append(helper_check(EXP_COMBOS, combos_length, 'all combos'))
    summary.append(helper_check(EXP_TALLY_KEYS, tally_key_length, 'tally keys'))
    summary.append(helper_check(EXP_TALLY_SET, tally_set,'set of tally values'))
    summary.append(helper_check(EXP_LIVE_COMBOS, live_filter_len, 'live combos'))
    summary.append(helper_check(EXP_LIVE_TALLY_SUM, live_tally_sum, 'live tally sum'))
    summary.append(helper_check(EXP_TALLY_KEYS, live_tally_keys, 'live tally keys'))

    for hand, count in CLASS_CHECK.items():
        summary.append(helper_check(count,live_tally.get(hand, 0),f'{hand}'))
    
    print(f'Results: {sum(summary)} of {len(summary)} passed!')
