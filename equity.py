'''' This module has functions that calculate a given hands equity based on the board, hero's hand, and villians range'''
import cards
import random
import evaluator


def find_equity(flop:tuple, hero:tuple, villan_range:list) -> float:
    ''' This function returns exact equity calcuated based on hero's hand, board, and villian's range'''
    wins = 0
    ties = 0
    total = 0
    
    hero_hand = flop + hero
    live_range = cards.find_combos_left(villan_range, known_cards=hero_hand)

    for pos_combo in live_range:

        known_cards = flop + hero + pos_combo
        remaining_deck = [] 
        
        for card in cards.DECK:
            if card  not in known_cards:
                remaining_deck.append(card)

        remaining_combos = cards.generate_all_combos(remaining_deck)
        
        for combo in remaining_combos:
            hero_7 = flop + hero + combo
            vil_7 = flop + pos_combo + combo

            hero_str = evaluator.evaluate_hand(hero_7)
            vil_str = evaluator.evaluate_hand(vil_7)
            
            if hero_str > vil_str:
                wins += 1
            elif hero_str == vil_str:
                ties+= 1
            
            total += 1

    equity = ((wins + ties/2)) / total 
    
    return equity


def estimate_equity(flop:tuple, hero:tuple, villan_range:list, n:int) -> float:
    ''' This function estimates the equity via Monte Carlo simulation. It's purpose is to save computational time compared to find_equity()'''
    wins = 0
    ties = 0
    
    hero_hand = flop + hero
    live_range = cards.find_combos_left(villan_range, known_cards=hero_hand)

    for _ in range(n):
        ran_combo = random.choice(live_range)
        known_cards = flop + hero + ran_combo
        remaining_deck = [] 
        
        for card in cards.DECK:
            if card  not in known_cards:
                remaining_deck.append(card)

        combo = tuple(random.sample(remaining_deck, 2))
        
        hero_7 = flop + hero + combo
        vil_7 = flop + ran_combo + combo

        hero_str = evaluator.evaluate_hand(hero_7)
        vil_str = evaluator.evaluate_hand(vil_7)
            
        if hero_str > vil_str:
            wins += 1
        elif hero_str == vil_str:
            ties+= 1

    equity = ((wins + ties/2)) / n 
    return equity
