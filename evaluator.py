""" This Module is takes a 7 card hand and evaluates it into poker 5 card categories. ie: Flush, Four of Kind, 3 of Kind etc... The final evaluate_hand()
    returns a tuple with the hand rank from 9-1. 9 being the best and details strength of hand via CARD_VALUE.
    ie: evaluate_hand returns (4,12,10,9) == (3 of kind with aces, a queen, and jack) or ('As','Ad','Ah','Qs','Jc') """

import cards 

# --- CONSTANTS ---
HAND_RANK_MAP = {9: 'Straight Flush', 8:'Four of a Kind', 7:'Full House', 6:'Flush', 5:'Straight', 4:'Three of Kind', 3:'Two Pair', 2:'Pair',1:'High Card'}

# --- Mini Functions ----
def convert_ranks(ranks:dict) -> dict:
    ''' Converts a counted rank dictionary and maps to CARD_VALUE. Returns dictionary of mapped ranks'''
    mapped_ranks = {}
    for rank , count in ranks.items():
        value = cards.CARD_VALUE[rank]
        mapped_ranks[value] = count
    
    return mapped_ranks

def count_ranks_suits(seven:tuple) -> tuple[dict,dict]:
    ''' Counts how many ranks and suits are in a given 7 hand tuple, returns dictionary of counts'''
    ranks = {}
    suits = {}
    for card in seven:
        ranks[card[0]] = ranks.get(card[0], 0) + 1
        suits[card[1]] = suits.get(card[1], 0) + 1
    
    mapped_ranks = convert_ranks(ranks)

    return mapped_ranks , suits

def find_groups(ranks:dict) -> dict:
    ''' Groups ranks via count. ie: a hand with 2 kings and 2 queens. It groups them {2:[11,10]}'''
    group_counts = {}
    for rank, count in sorted(ranks.items(), reverse=True):
        group_counts.setdefault(count , []).append(rank)
    
    return group_counts

def find_flush_suit(suits:dict) -> str | None:
    ''' Takes the suits count dictionary and returns the flush suit as string'''
    flush_suit = None
    for suit , count in suits.items():
        if count >= 5:
            flush_suit = suit
    
    return flush_suit

def find_flush_cards(seven:tuple, suit:str) -> tuple | None:
    ''' Takes the flush suit and orginial seven cards to return tuple of cards with the flush suit'''
    flush_cards = []
    for card in seven:
        if card[1] == suit:
            flush_cards.append(card)
    
    flush_cards_tuple = tuple(flush_cards)
    
    return flush_cards_tuple

def find_straight(ranks:dict) -> int| None:
    ''' Takes the dictionary count of ranks and determines if straight exist, if so returns the straight high rank'''
    sorted_ranks = sorted(list(set(ranks)))
    straight_high = None
    consecutive_count = 1
    for i in range(len(sorted_ranks) - 1):
        if sorted_ranks[i] == sorted_ranks[i + 1] - 1:
            consecutive_count += 1
            if consecutive_count >= 5:
                straight_high = sorted_ranks[i + 1]
        else:
            consecutive_count = 1
    
    if straight_high is None:
        if {12,0,1,2,3}.issubset(set(ranks)):
            straight_high = 3

    return straight_high 

def find_straight_flush(flush_cards: tuple) -> int | None:
    ''' Takes flush cards and determines if there is a straight flush, returns straight_high'''
    flush_ranks, _ = count_ranks_suits(flush_cards)
    flush_straight_high = find_straight(flush_ranks)
    return flush_straight_high

def find_kickers(spent:list, groups:dict) -> list:
    ''' Finds kicker values and puts them into a list'''
    flat_list = []
    for i in groups:
        for value in groups[i]:
            flat_list.append(value)
    
    all_else = []
    for i in flat_list:
        if i in spent:
            pass
        else:
            all_else.append(i)

    return sorted(all_else, reverse= True)


# ---- Main evaluator Function -----

def evaluate_hand(seven:tuple) -> tuple:
    ''' Main evalutor function, takes 7-card tuple and returns the hand ranks tuple'''
    ranks, suits = count_ranks_suits(seven)
    groups = find_groups(ranks)
    flush_suit = find_flush_suit(suits)
    flush_cards = None
    sf_high = None
    
    if flush_suit is not None:
        flush_cards = find_flush_cards(seven, flush_suit)
        sf_high = find_straight_flush(flush_cards)
    
    straight_high = find_straight(ranks)
    
    pair = None
    trips = None
    pairs_list = groups.get(2,[])
    trips_list = groups.get(3, [])
    
    candidates = []
    
    if len(trips_list) >= 1:
        trips = groups[3][0]
        if len(trips_list) > 1:
            for i in trips_list:
                if i == trips:
                    pass
                else:
                    candidates.append(i)
        else:
            for i in pairs_list:
                candidates.append(i)
        if len(candidates) >= 1 :
            pair = max(candidates)


    if sf_high is not None:
        return (9, sf_high)
    elif groups.get(4) is not None:
        quads = groups[4][0]
        quad_list = [quads]
        kickers = find_kickers(quad_list, groups)
        kicker = kickers[0]
        return (8, quads, kicker)
    elif trips is not None and pair is not None:
        return (7, trips, pair)
    elif flush_suit is not None:
        flush_values = []
        flush_ranks , _ = count_ranks_suits(flush_cards)
        for rank in flush_ranks:
            flush_values.append(rank) 
        flush_values.sort(reverse= True)
        return (6, flush_values[0], flush_values[1],flush_values[2], flush_values[3], flush_values[4])
    elif straight_high is not None:
        return (5, straight_high)
    elif trips is not None:
        kickers = find_kickers([trips], groups)
        return (4, trips, kickers[0], kickers[1])
    elif len(pairs_list) >= 2:
        high_pair = pairs_list[0]
        low_pair = pairs_list[1]
        kickers = find_kickers(pairs_list[:2],groups)
        return (3, high_pair, low_pair, kickers[0])
    elif len(pairs_list) == 1:
        pair = pairs_list[0]
        kickers = find_kickers(pairs_list, groups)
        return (2, pair, kickers[0], kickers[1], kickers[2])
    else:
        high_card = groups[1][0]
        k1 = groups[1][1]
        k2 = groups[1][2]
        k3 = groups[1][3]
        k4 = groups[1][4]
        return (1, high_card, k1, k2,k3,k4)


