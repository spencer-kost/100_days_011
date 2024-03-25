# 011.py
#
import os
import Asset
import random

deck = [
    '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts', 'Ace of Hearts',
    '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds', 'Ace of Diamonds',
    '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs', 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs', 'Ace of Clubs',
    '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'Jack of Spades', 'Queen of Spades', 'King of Spades', 'Ace of Spades'
]

# blackjack_values = {
#     '2 of Hearts': 2, '3 of Hearts': 3, '4 of Hearts': 4, '5 of Hearts': 5, '6 of Hearts': 6, '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9, '10 of Hearts': 10,
#     'Jack of Hearts': 10, 'Queen of Hearts': 10, 'King of Hearts': 10, 'Ace of Hearts': [1, 11],
#     '2 of Diamonds': 2, '3 of Diamonds': 3, '4 of Diamonds': 4, '5 of Diamonds': 5, '6 of Diamonds': 6, '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9, '10 of Diamonds': 10,
#     'Jack of Diamonds': 10, 'Queen of Diamonds': 10, 'King of Diamonds': 10, 'Ace of Diamonds': [1, 11],
#     '2 of Clubs': 2, '3 of Clubs': 3, '4 of Clubs': 4, '5 of Clubs': 5, '6 of Clubs': 6, '7 of Clubs': 7, '8 of Clubs': 8, '9 of Clubs': 9, '10 of Clubs': 10,
#     'Jack of Clubs': 10, 'Queen of Clubs': 10, 'King of Clubs': 10, 'Ace of Clubs': [1, 11],
#     '2 of Spades': 2, '3 of Spades': 3, '4 of Spades': 4, '5 of Spades': 5, '6 of Spades': 6, '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9, '10 of Spades': 10,
#     'Jack of Spades': 10, 'Queen of Spades': 10, 'King of Spades': 10, 'Ace of Spades': [1, 11]
# }
#
deck = {
    1: ['2 of Hearts', 2], 2: ['2 of Diamonds', 2], 3: ['2 of Clubs', 2], 4: ['2 of Spades', 2],
    5: ['3 of Hearts', 3], 6: ['3 of Diamonds', 3], 7: ['3 of Clubs', 3], 8: ['3 of Spades', 3],
    9: ['4 of Hearts', 4], 10: ['4 of Diamonds', 4], 11: ['4 of Clubs', 4], 12: ['4 of Spades', 4],
    13: ['5 of Hearts', 5], 14: ['5 of Diamonds', 5], 15: ['5 of Clubs', 5], 16: ['5 of Spades', 5],
    17: ['6 of Hearts', 6], 18: ['6 of Diamonds', 6], 19: ['6 of Clubs', 6], 20: ['6 of Spades', 6],
    21: ['7 of Hearts', 7], 22: ['7 of Diamonds', 7], 23: ['7 of Clubs', 7], 24: ['7 of Spades', 7],
    25: ['8 of Hearts', 8], 26: ['8 of Diamonds', 8], 27: ['8 of Clubs', 8], 28: ['8 of Spades', 8],
    29: ['9 of Hearts', 9], 30: ['9 of Diamonds', 9], 31: ['9 of Clubs', 9], 32: ['9 of Spades', 9],
    33: ['10 of Hearts', 10], 34: ['10 of Diamonds', 10], 35: ['10 of Clubs', 10], 36: ['10 of Spades', 10],
    37: ['Jack of Hearts', 10], 38: ['Jack of Diamonds', 10], 39: ['Jack of Clubs', 10], 40: ['Jack of Spades', 10],
    41: ['Queen of Hearts', 10], 42: ['Queen of Diamonds', 10], 43: ['Queen of Clubs', 10], 44: ['Queen of Spades', 10],
    45: ['King of Hearts', 10], 46: ['King of Diamonds', 10], 47: ['King of Clubs', 10], 48: ['King of Spades', 10],
    49: ['Ace of Hearts', 11], 50: ['Ace of Diamonds', 11], 51: ['Ace of Clubs', 11], 52: ['Ace of Spades', 11]
}

ref_deck = {
    1: ['2 of Hearts', 2], 2: ['2 of Diamonds', 2], 3: ['2 of Clubs', 2], 4: ['2 of Spades', 2],
    5: ['3 of Hearts', 3], 6: ['3 of Diamonds', 3], 7: ['3 of Clubs', 3], 8: ['3 of Spades', 3],
    9: ['4 of Hearts', 4], 10: ['4 of Diamonds', 4], 11: ['4 of Clubs', 4], 12: ['4 of Spades', 4],
    13: ['5 of Hearts', 5], 14: ['5 of Diamonds', 5], 15: ['5 of Clubs', 5], 16: ['5 of Spades', 5],
    17: ['6 of Hearts', 6], 18: ['6 of Diamonds', 6], 19: ['6 of Clubs', 6], 20: ['6 of Spades', 6],
    21: ['7 of Hearts', 7], 22: ['7 of Diamonds', 7], 23: ['7 of Clubs', 7], 24: ['7 of Spades', 7],
    25: ['8 of Hearts', 8], 26: ['8 of Diamonds', 8], 27: ['8 of Clubs', 8], 28: ['8 of Spades', 8],
    29: ['9 of Hearts', 9], 30: ['9 of Diamonds', 9], 31: ['9 of Clubs', 9], 32: ['9 of Spades', 9],
    33: ['10 of Hearts', 10], 34: ['10 of Diamonds', 10], 35: ['10 of Clubs', 10], 36: ['10 of Spades', 10],
    37: ['Jack of Hearts', 10], 38: ['Jack of Diamonds', 10], 39: ['Jack of Clubs', 10], 40: ['Jack of Spades', 10],
    41: ['Queen of Hearts', 10], 42: ['Queen of Diamonds', 10], 43: ['Queen of Clubs', 10], 44: ['Queen of Spades', 10],
    45: ['King of Hearts', 10], 46: ['King of Diamonds', 10], 47: ['King of Clubs', 10], 48: ['King of Spades', 10],
    49: ['Ace of Hearts', 11], 50: ['Ace of Diamonds', 11], 51: ['Ace of Clubs', 11], 52: ['Ace of Spades', 11]
}

def deal():
    '''Return a random card out of a 52 card deck "deck"'''
    card = random.choice(list(deck.keys()))
    del deck[card]
    return card
def redeal():
    deck = {
        1: ['2 of Hearts', 2], 2: ['2 of Diamonds', 2], 3: ['2 of Clubs', 2], 4: ['2 of Spades', 2],
        5: ['3 of Hearts', 3], 6: ['3 of Diamonds', 3], 7: ['3 of Clubs', 3], 8: ['3 of Spades', 3],
        9: ['4 of Hearts', 4], 10: ['4 of Diamonds', 4], 11: ['4 of Clubs', 4], 12: ['4 of Spades', 4],
        13: ['5 of Hearts', 5], 14: ['5 of Diamonds', 5], 15: ['5 of Clubs', 5], 16: ['5 of Spades', 5],
        17: ['6 of Hearts', 6], 18: ['6 of Diamonds', 6], 19: ['6 of Clubs', 6], 20: ['6 of Spades', 6],
        21: ['7 of Hearts', 7], 22: ['7 of Diamonds', 7], 23: ['7 of Clubs', 7], 24: ['7 of Spades', 7],
        25: ['8 of Hearts', 8], 26: ['8 of Diamonds', 8], 27: ['8 of Clubs', 8], 28: ['8 of Spades', 8],
        29: ['9 of Hearts', 9], 30: ['9 of Diamonds', 9], 31: ['9 of Clubs', 9], 32: ['9 of Spades', 9],
        33: ['10 of Hearts', 10], 34: ['10 of Diamonds', 10], 35: ['10 of Clubs', 10], 36: ['10 of Spades', 10],
        37: ['Jack of Hearts', 10], 38: ['Jack of Diamonds', 10], 39: ['Jack of Clubs', 10], 40: ['Jack of Spades', 10],
        41: ['Queen of Hearts', 10], 42: ['Queen of Diamonds', 10], 43: ['Queen of Clubs', 10], 44: ['Queen of Spades', 10],
        45: ['King of Hearts', 10], 46: ['King of Diamonds', 10], 47: ['King of Clubs', 10], 48: ['King of Spades', 10],
        49: ['Ace of Hearts', [1, 11]], 50: ['Ace of Diamonds', [1, 11]], 51: ['Ace of Clubs', [1, 11]], 52: ['Ace of Spades', [1, 11]]
    }

def read_card(player_hand):
    full_hand = []
    for cards in range(len(player_hand)):
        full_hand.append(ref_deck.get(player_hand[cards])[0])
    return full_hand

# print(Asset.logo)
def blackjack():
    '''Function that plays blackjack with one player against a computer using a single deck that is dealt at the beginning of each round'''
    os.system('cls' if os.name == 'nt' else 'clear')
    redeal() # Start out the game by dealing a fresh deck
    print(Asset.logo)
    comp_hand = [deal(), deal()] #deal two cards to the comptuer
    usr_hand = [deal(), deal()] #deal two cards to the user
    print(f"You have a {ref_deck.get(usr_hand[0])[0]} and a {ref_deck.get(usr_hand[1])[0]}.")
    print(f"The dealer is showing a {ref_deck.get(comp_hand[0])[0]}")

    #Add the sum of both hands: user and computer
    usr_sum = ref_deck.get(usr_hand[0])[1]+ref_deck.get(usr_hand[1])[1]
    comp_sum = ref_deck.get(comp_hand[0])[1]+ref_deck.get(comp_hand[1])[1]
    # print(usr_sum)

    hit = True
    while hit == True:
        hitstay = input(f"Do you want to hit? (y/n)\n")
        if hitstay == "y": #Enter the hit sequence for the user.
            last_card = deal()
            usr_hand.append(last_card)
            usr_sum += ref_deck.get(last_card)[1]
            readable_usr = read_card(usr_hand)
            print(f"Your hand is {readable_usr} the dealer is showing {ref_deck.get(comp_hand[0])[0]}")
        else:
            hit = False
        if usr_sum > 21:
            print(f"You busted! Your total was {usr_sum}. Dealer Wins.")
            hit = False
    while comp_sum <= 17:
        last_card = deal()
        comp_hand.append(last_card)
        comp_sum += ref_deck.get(last_card)[1]
    readable_comp = read_card(comp_hand)
    readable_usr = read_card(usr_hand)
    if  comp_sum >= 21:
        print(f"Your hand was {readable_usr}. The dealers hand was {readable_comp} adding to {comp_sum}. The dealer Busted. You win!")
    elif usr_sum >= comp_sum and comp_sum <= 21:
        print(f"Your hand was {readable_usr} adding to {usr_sum} and the dealers hand was {readable_comp} adding to {comp_sum}. You win!")
    else:
        print(f"Your hand was {readable_usr} adding to {usr_sum} and the dealers hand was {readable_comp} adding to {comp_sum}. You lose!")

gameplay = True

while gameplay == True:
    playask = input("Do you want to play blackjack?(y/n)\n")
    if playask == "y":
        blackjack()
    else:
        gameplay = False
