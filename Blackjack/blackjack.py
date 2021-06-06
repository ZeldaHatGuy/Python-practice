from blackjack_libs import dealer, player, deck, get_score
from os import system, name


'''Blackjack game for coding practice
   Written by: Greg Singletary
   todos:
     - Add support for more players
     - Add support for doubling down and splitting pairs
   Requires blackjack_libs
'''

# Function to clear the screen.


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


dealer_deck = deck()
play_again = 'yes'

print("Welcome to BlackJack!")
while play_again == 'yes':
    clear()
    # Since blackjack decks are only shuffled back in when they run out, we will reinstantiate the deck class to simulate this effect when there are less than 6 cards left.
    cards_left = dealer_deck.cards_left()
    #print("There are {} cards left in the deck".format(cards_left))
    if cards_left < 6:
        print("Reshuffling deck")
    dealer_deck = deck()
    dealer_card1 = dealer_deck.dealCard()
    dealer_card2 = dealer_deck.dealCard()
    player_card1 = dealer_deck.dealCard()
    player_card2 = dealer_deck.dealCard()
    winner = None

    dealr = dealer(dealer_card1, dealer_card2)
    player1 = player(player_card1, player_card2)

# Deal with Blackjacks
    dealer_score = get_score(dealr.hand)
    if dealer_score == 21 and player_score != 21:
        print("Dealer has blackjack! Dealer Wins! {}".format(dealr.hand))
        winner = "Dealer"
    player_score = get_score(player1.hand)
    if player_score == 21 and dealer_score != 21:
        print("You have blackjack! You Win!!".format(player1.hand))
        winner = "Player"
    if player_score == 21 and dealer_score == 21:
        print("DOUBLE BLACKJACK!! WHAT ARE THE ODDS?? TIE GAME!!!")
        winner = "Tie"

# Section for player to make their choices
    if not winner:
        player_choice = ' '
        player_bust = False
        while player_choice.lower() != 'stand':
            player_choice = input("Your current score is {}({}). The dealer is showing {}. Would you like to stand or hit?: ".format(
                player_score, player1.hand, dealr.faceDownCard))
            if player_choice.lower() == 'hit':
                new_card = dealer_deck.dealCard()
                player1.addToHand(new_card)
                player_score = get_score(player1.hand)
            if player_score > 21:
                print("You have busted! Dealer wins!")
                player_bust = True
                winner = "Dealer"
                break

# section that lets the dealer evaluateHand method run to see if it can beat the player
        if not player_bust:
            dealer_choice = ' '
            dealer_bust = False
            while dealer_choice.lower() != 'stand':
                dealer_choice = dealr.evaluateHand(dealer_score, player_score)
                if dealer_choice.lower() == 'hit':
                    new_card = dealer_deck.dealCard()
                    dealr.addToHand(new_card)
                    dealer_score = get_score(dealr.hand)
                    if dealer_score > 21:
                        print("The Dealer has busted({}). You win!!!!".format(
                            dealer_score))
                        dealer_bust = True
                        winner = "Player"
                        break

# Determine winner if there are no busts or blackjack
    if not player_bust and not dealer_bust and not winner:
        if dealer_score > player_score:
            print("The dealer has {}({}). You have {}. Dealer wins!".format(
                dealer_score, dealr.hand, player_score))
        elif player_score > dealer_score:
            print("The dealer has {}. You have {}. You win!".format(
                dealer_score, player_score))
        elif player_score == dealer_score:
            print("The dealer has {}({}). You have {}. Tie Game!".format(
                dealer_score, dealr.hand, player_score))

    play_again = input("Would you like to play again? (yes/no:) ")
