""" This module generates a playing deck of cards and basic combinations for the game."""

# --- Constants ---
RANKS = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
SUITS = ['h','s','c','d']

# --- Building Functions ----
def build_deck(ranks:list, suits:list):
    deck = []
    for r in ranks:
        for s in suits:
            card = r + s 
            deck.append(card)
    return deck

def build_card_values(ranks:list):
    card_value = {}
    for i, rank in enumerate(ranks):
        card_value[rank] = i
    return card_value

def generate_all_combos(deck:list):
    all_hand_combos = []

    for i, card_1 in enumerate(deck):
        for card_2 in deck[i+1:]:
            hand = (card_1,card_2)
            all_hand_combos.append(hand)

    return all_hand_combos

# --- Derived constants ---
DECK = build_deck(RANKS,SUITS)
CARD_VALUE = build_card_values(RANKS)
ALL_COMBOS = generate_all_combos(DECK)

# --- Hand classification ---
def label_hand(hand):
    if CARD_VALUE[hand[0][0]] > CARD_VALUE[hand[1][0]]:
        high_card = hand[0]
        low_card = hand[1]
    else:
        high_card = hand[1]
        low_card = hand[0]

    if high_card[0] == low_card[0]:
        label = high_card[0] + low_card[0]
    elif high_card[1] == low_card[1]:
        label = high_card[0] + low_card[0] + 's'
    else:
        label = high_card[0] + low_card[0] + 'o'
    
    return label

def tally_combos(combos:list):
    combo_tally = {}

    for i in combos:
        hand = label_hand(i)
        
        combo_tally[hand] = combo_tally.get(hand, 0) + 1

    return combo_tally

# --- Card removal ---
def find_combos_left(combos:list, known_cards:tuple):
    possible_combos = []
    
    for combo in combos:
        if combo[0] in known_cards or combo[1] in known_cards:
            pass
        else:
            possible_combos.append(combo)    
    
    return possible_combos


