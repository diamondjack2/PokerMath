'''This script checks the compare_hands() output to a 3rd party poker python library (treys) for validity and edge cases.'''
import cards
import evaluator
import random 
from check_cards import helper_check
from treys import Card, Evaluator

random.seed(10)

# --- Constants 
HAND_CHECK = {
    'straight_flush': ('9d','8d','7d','6d','5d','Ah','Kc'),
    'steel_wheel':    ('As','5s','4s','3s','2s','9d','Kc'),
    'quads_trip':     ('As','Ah','Ad','Ac','Ks','Kh','Kd'),
    'boat_2trips':    ('As','Ah','Ad','Ks','Kh','Kd','Qs'),
    'boat_2pairs':    ('As','Ah','Ad','Ks','Kh','Qs','Qd'),
    'flush_six':      ('As','Ks','9s','7s','4s','2s','3h'),
    'flush_not_sf':   ('9s','7s','5s','3s','2s','8h','6d'),
    'wheel':          ('As','5d','4c','3h','2s','9d','Kc'),
    'straight_six':   ('9h','8d','7c','6s','5h','4d','Kc'),
    'trips':          ('Ts','Th','Td','6h','As','4c','2d'),
    'two_pair_three': ('Ks','Kh','9s','9d','4c','4h','2s'),
    'one_pair':       ('Jd','Js','Ks','9h','7c','5d','2c'),
    'high_card':      ('Kh','7d','8c','Js','Td','3s','2h'),
}

MULTI1 = [(7,12,11), (7,12,11), (7,12,11)]
MULTI2 = [(2,9,11,7,5), (2,9,11,7,5), (1,12,10,8,6)]
MULTI3 = [(9,7), (8,12,11), (7,12,11)]
MULTI4 = [(2,9,11,7,5), (2,9,11,7,3)]


# --- Treys ---
treys_eval = Evaluator()

def treys_verdict(board, hole_1, hole_2):
    '''This function converts trey's output to match compare_hands() index output'''
    board_t = [Card.new(c) for c in board]
    s1 = treys_eval.evaluate(board_t, [Card.new(c) for c in hole_1])
    s2 = treys_eval.evaluate(board_t, [Card.new(c) for c in hole_2])
    if s1 < s2:
        return [0]
    elif s2 < s1:
        return [1]
    else:
        return [0, 1]


# --- Main Comparison Loop ---

if __name__ == "__main__":
    
    # Evaluator Test
    straight_flush = evaluator.evaluate_hand(HAND_CHECK['straight_flush'])
    steel_wheel = evaluator.evaluate_hand(HAND_CHECK['steel_wheel'])
    quads_trip = evaluator.evaluate_hand(HAND_CHECK['quads_trip'])
    boat_2trips = evaluator.evaluate_hand(HAND_CHECK['boat_2trips'])
    boat_2pairs = evaluator.evaluate_hand(HAND_CHECK['boat_2pairs'])
    flush_six = evaluator.evaluate_hand(HAND_CHECK['flush_six'])
    flush_not_sf = evaluator.evaluate_hand(HAND_CHECK['flush_not_sf'])
    wheel = evaluator.evaluate_hand(HAND_CHECK['wheel'])
    straight_six = evaluator.evaluate_hand(HAND_CHECK['straight_six'])
    trips = evaluator.evaluate_hand(HAND_CHECK['trips'])
    two_pair_three = evaluator.evaluate_hand(HAND_CHECK['two_pair_three'])
    one_pair = evaluator.evaluate_hand(HAND_CHECK['one_pair'])
    high_card = evaluator.evaluate_hand(HAND_CHECK['high_card'])


    # Compare Hands Test to treys (two way)
    MY_OUTPUT = []
    TREYS_OUTPUT = []
    
    for i in range(100000):
        shuffle = random.sample(cards.DECK, 9)
        board = shuffle[:5]
        h1 = shuffle[5:7]
        h2 = shuffle[7:]

        p1 = board + h1
        p2 = board + h2

        p1_rank = evaluator.evaluate_hand(p1)
        p2_rank = evaluator.evaluate_hand(p2)

        table = [p1_rank, p2_rank]

        eval_verdict = evaluator.compare_hands(table)

        MY_OUTPUT.append(eval_verdict)

        treys_v = treys_verdict(board,h1,h2)

        TREYS_OUTPUT.append(treys_v)
    
    # Compare Hands Test (three way)
    multi_1 = evaluator.compare_hands(MULTI1)
    multi_2 = evaluator.compare_hands(MULTI2)
    multi_3 = evaluator.compare_hands(MULTI3)
    multi_4 = evaluator.compare_hands(MULTI4)

    summary = []

    summary.append(helper_check(straight_flush,(9, 7), 'straight flush'))
    summary.append(helper_check(steel_wheel,(9, 3), 'steel_wheel'))
    summary.append(helper_check(quads_trip,(8, 12, 11), 'quads_trip'))
    summary.append(helper_check(boat_2trips,(7, 12, 11), 'boat_2trips'))
    summary.append(helper_check(boat_2pairs,(7, 12, 11), 'boat_2pairs'))
    summary.append(helper_check(flush_six,(6, 12, 11, 7, 5, 2), 'flush_six'))
    summary.append(helper_check(flush_not_sf,(6, 7, 5, 3, 1, 0), 'flush_not_sf'))
    summary.append(helper_check(wheel,(5, 3), 'wheel'))
    summary.append(helper_check(straight_six,(5, 7), 'straight_six'))
    summary.append(helper_check(trips,(4, 8, 12, 4), 'trips'))
    summary.append(helper_check(two_pair_three,(3, 11, 7, 2), 'two_pair_three'))
    summary.append(helper_check(one_pair,(2, 9, 11, 7, 5), 'one_pair'))
    summary.append(helper_check(high_card,(1, 11, 9, 8, 6, 5), 'high_card'))
   
    print(f'Evalutor Test: {sum(summary)} of {len(summary)} passed!')

    multi_summary = []

    multi_summary.append(helper_check([0,1,2], multi_1, 'Multi-way 1'))
    multi_summary.append(helper_check([0,1], multi_2, 'Multi-way 2'))
    multi_summary.append(helper_check([0], multi_3, 'Multi-way 3'))
    multi_summary.append(helper_check([0], multi_4, 'Multi-way 4'))

    print(f'Evalutor Test: {sum(multi_summary)} of {len(multi_summary)} passed!')


    print(f'Compare Hands & Treys Match: {MY_OUTPUT == TREYS_OUTPUT}')


