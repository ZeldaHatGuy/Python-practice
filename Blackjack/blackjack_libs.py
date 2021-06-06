import random
import sys

# Supporting Libraries for main blackjack game.


# Creates a dealer object
class dealer():
    def __init__(self, faceUpCard, faceDownCard):
        self.faceUpCard = faceUpCard
        self.faceDownCard = faceDownCard
        self.hand = [faceDownCard, faceUpCard]

    def addToHand(self, card):
        self.hand.append(card)
# A simple method to force the dealer to try and beat the player

    def evaluateHand(self, dealerScore, playerScore):
        if dealerScore >= playerScore:
            return "Stand"
        elif dealerScore < playerScore:
            return "Hit"

# Create player instance. This will allow support for multiple players


class player():
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2
        self.hand = [card1, card2]

    def addToHand(self, card):
        self.hand.append(card)

# Creates and keeps track of cards in the deck.


class deck():
    def __init__(self):
        self.cards = ['A', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2,
                      'A', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2,
                      'A', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2,
                      'A', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2]

    def dealCard(self):
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card

    def cards_left(self):
        return len(self.cards)

# method to return the score of a blackjack hand and has simple logic to deal with Aces.


def get_score(hand):
    score = 0
    face_cards = ['K', 'Q', 'J']
    for card in hand:
        if card in face_cards:
            card = 10
        elif card == 'A':
            card = 11
        score += card
    if score > 21 and 'A' in hand:
        score = score - 10
    return score
