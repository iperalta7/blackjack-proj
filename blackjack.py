# Name:Isaiah Peralta
# Class: CSC 110 - Fall 2021
# Assignment:  Programming Project Implementation
# Due Date: December 13, 2021

# Puesdocode:
# Create a deck of 52 cards list using the faces and suites lists
# create a player hand list and dealer hand and assign two random cards to each
# Remove cards from deck list after assigning each one
#show player hand and show one card from dealer

# compute hand values

# check if user hand < 21
    # give choice to hit or stay
    # dealer turn if player chooses stay

# On dealer's turn, if dealer hand < 21
    # if dealer less than 17, hit
    # if dealer's hand is more, stay

#compute hand values
#Determine who won
#Give a new hand
# Deal new deck if all cards are used

# Algorithms used:
# For loops to create one list from two lists
# Check values conditionals were used to determine whether to play
# Recursive was pretty fundamental in allowing the dealer and player to keep playing
#



# Function Code
import random


def createDeck():
    deck = []
    faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    suits = ['D', 'C', 'S', 'H']

    for face in faces:
        j = 0
        while j < len(suits):
            suit = suits[j]
            card = face + suit
            deck.append(card)
            j += 1
    # This function will create a list for the deck of 52 cards
    # using two lists, suits and faces and will return the deck of 52
    return deck

def dealCard(deck):
    card = random.choice(deck)
    deck.remove(card)
    #This function will randomly choose one card from the deck and remove it from the deck.
    return card, deck

# deals the first two cards for each hand
def dealhands(deck):
    playerHand = []
    dealerHand = []
    i = 0
    while i < 2:
        playercard, deck = dealCard(deck)
        dealercard, deck = dealCard(deck)
        playerHand.append(playercard)
        dealerHand.append(dealercard)
        i += 1

    print("Your hand is: ", " ".join(playerHand))
    print('Dealer is showing: ', (dealerHand[1]))
    Pvalue, blackjack, aces = computeHands(playerHand)

    # determines whether to print who has blackjack for the first set of hands
    if blackjack == 0:
        checkAce(aces,Pvalue)
    Dvalue, dblackjack, daces = computeHands(dealerHand)
    if blackjack == 1:
        print("You have BLACK JACK!!")
        if dblackjack == 0:
            print("Dealer hand is: ", " ".join(dealerHand))
            print("Dealer does not have BLACK JACK")
        if dblackjack == 1:
            print("Dealer hand is: ", " ".join(dealerHand))
            print("Dealer has BLACK JACK")

    return playerHand, dealerHand, Pvalue

# calculates the value of dealer or player hand
def computeHands(Hand):
    Value = 0
    aces = 0
    blackjack = 0
    # T J K Q A = 10
    for card in Hand:
        if card[0] == 'T':
            Value = Value + 10
        elif card[0] == 'J':
            Value = Value + 10
        elif card[0] == 'K':
            Value = Value + 10
        elif card[0] == 'Q':
            Value = Value + 10
        elif card[0] == 'A':
            # accumulates the number of aces and starts off by giving 1 to the value
            # another function determines the best value
            aces = aces + 1
            Value = Value + 1
        else:
            Value = Value + int(card[0])

    # for loop to determine blackjack
    for card in Hand:
        if len(Hand) == 2:
            if aces == 1 and (card[0] == 'T' or card[0] == 'J' or card[0] == 'K' or card[0] == 'Q'):
                blackjack = 1

    # returns the value, whether there was a blackjack, and how many aces the hand had
    return Value, blackjack, aces

def playerChoice(playerHand, dealerHand, deck):
    # gives the player the choice to hit or stay
    # needs to calculate all the values, blackjacks, and aces first
    playerValue, blackjack, aces = computeHands(playerHand)
    dealerValue, dblackjack, dAces = computeHands(dealerHand)
    dealerValue = dealerAces(dAces, dealerValue)

    # checks if player has blackjack,
    # if they do no need to play
    if blackjack == 0:
        # checks the player hand value to determine if they even need to be asked to hit or stay
        if playerValue <= 21:
            choice = input("\nType H to hit or S to stay: ")
            if choice == "h":
                # adds a card to the new player Hand
                card, deck = dealCard(deck)
                playerHand.append(card)
                playerValue, blackjack, aces = computeHands(playerHand)
                print("Your hand is: ", " ".join(playerHand))
                print('Dealer is showing: ', dealerHand[1])
                playerValue = checkAce(aces, playerValue)
                if playerValue <= 21:
                    # checks if player wants to play still by calling the same function
                    dealerValue, dblackjack, aces = computeHands(dealerHand)
                    dealerValue = dealerAces(aces, dealerValue)
                    dealerHand, playerHand, deck, dealerValue = playerChoice(playerHand, dealerHand, deck)
                else:
                    # prints out only after if player continues to hit
                    print("You have busted - too bad")
            elif choice == "s":
                # determines how dealer plays by calling the dealerPlays function
                print("Dealer hand is: ", " ".join(dealerHand))
                if dblackjack == 1:
                    # checks first if dealer has a blackjack otherwise no need for the dealer to play
                    print("Dealer has BLACK JACK")
                else:
                    # calls the dealerPlays function to determine how the dealer plays
                    print("Dealer hand value is: ", dealerValue)
                    dealerHand, deck, dealerValue = dealerPlays(dealerHand, deck, playerValue)

                if dealerValue > 21:
                    # if dealer already went over then no need to play
                    print("Dealer BUSTS")

        else:
            print("You have busted - too bad")

    return dealerHand, playerHand, deck, dealerValue

def dealerPlays(dealerhand, deck, playerValue):
    # no turn if player busts
    # computes value of the hand
    # determines whether the dealer hits or stay
    dealerValue, blackjack, aces = computeHands(dealerhand)
    dealerValue = dealerAces(aces, dealerValue)
    if playerValue > 21:
        # dealer does not play because already won
        dealerhand = dealerhand
    elif dealerValue >= 17:
        # dealer does not play
        dealerhand = dealerhand
    elif dealerValue < 17:
        # dealer takes a card
        newcard, deck = dealCard(deck)
        dealerhand.append(newcard)
        print("Dealer taking")
        print("\nDealer hand is: ", " ".join(dealerhand))
        dealerValue, blackjack, aces = computeHands(dealerhand)
        dealerValue = dealerAces(aces, dealerValue)
        print("Dealer hand value is: ", dealerValue)

    # if its still less after it keeps playing
    if dealerValue < 17:
        dealerhand, deck, dealerValue = dealerPlays(dealerhand, deck, playerValue)

    return dealerhand, deck, dealerValue

# Calculates the lowest value depending how many aces are there in the hand for the dealer
def dealerAces(aces, value):
    # for one ace
    if aces == 1:
        value = value
        if value < 21:
            value = value - 1 + 11
            if value > 21:
                value = value - 11 + 1
    # for 2 aces exactly
    if aces == 2:
        value = value - 2 + 11 + 11
        if value < 21:
            value = value
        elif value > 21:
            value = value - 11 + 1
            if value > 21:
                value = value - 11 + 1

    # uses a for loop to calculate the lowest for n amount of aces
    if aces > 2:
        if value < 21:
            value = value - 1 + 11
            if value > 21:
                value = value - 11
        for i in range(aces-1):
            value = value + 11
            if value > 21:
                value = value - 11
    return value



def WonLossTie(dealerValue, dealerHand, playerHand, deck, score):
    # determines whether the player won, loss, or tied by
    # comparing the hand values and adjusts the score based on the round
    playerValue, blackjack, aces = computeHands(playerHand)
    dValue, dblackjack, aces = computeHands(dealerHand)
    dealerValue = dealerValue
    if playerValue == dealerValue:
        score = score + 0
        print("\nYou tied with the dealer, that is a push and your score for this round is 0")
    elif blackjack == 1 and dblackjack == 1:
        score = score + 0
        print("\nYou tied with the dealer, that is a push and your score for this round is 0")
    elif blackjack == 1:
        score = score + 2
        print("\nBLACK JACK yields a score of 2")
    elif dblackjack == 1:
        score = score - 1
        print("\nThe dealer beat your hand, so your score for this round is -1")
    elif playerValue > 21:
        score = score - 1
        print("\nYou busted, your score for this round is -1")
    elif dealerValue > 21:
        score = score + 1
        print("\nDealer Busted, your score for this round is 1")
    elif playerValue > dealerValue:
        score = score + 1
        print("\nYou beat the dealer, your score for this round is 1")
    elif dealerValue > playerValue:
        score = score - 1
        print("\nThe dealer beat your hand, so your score for this round is -1")

    print('Your total score is: ', score)

    return score

def continuePlaying(score, seedValue, deck):
    # asks the player if they want to play again
    # calls another function to give new hands if yes
    choice = input("\nPlay again? Y or N: ")
    if choice.upper() == 'Y':
        resetHand(score, seedValue, deck)
    if choice.upper() == 'N':
        print("\nThanks for playing, good-bye...")
    return

# resets the hands for the dealer and Player after
# player asks to continue playing again
def resetHand(score, seedValue, deck):
    if len(deck) < 4:
        # creates a new deck if there are no more cards
        deck = createDeck()
        print("\nDealing new deck")

    if len(deck) > 4:
        # if there are still cards available will continue the game with
        # current deck
        print('\n')
        playerHand, dealerHand, value = dealhands(deck)
        dealerHand, playerHand, deck, dealerValue = playerChoice(playerHand, dealerHand, deck)
        score = WonLossTie(dealerValue, dealerHand, playerHand, deck, score)
        continuePlaying(score, seedValue, deck)
    return playerHand, dealerHand, score

# Will always check to calculate the value of the hand
# according to the num of aces and returns the smallest value
def checkAce(aces, value):
    # gonna return the smallest value
    valueList = []
    valueList.append(value)
    # prints out the values of hand according to the diff aces
    if aces != 0:
        print("You have " + str(aces) + " ace(s) in your hand. ", " Your current hand value is: ", value)
        for i in range(aces):
            print("or", value + 10)
            value = value + 10
            valueList.append(value)
    else:
        #will automaticlly print the hand even if there is no aces
        print("Your current hand value is: ", value)
    smallValue = min(valueList)
    return smallValue

#main functions that starts off the game
def main(seedValue):
    random.seed(seedValue)
    score = 0
    deck = createDeck()
    playerHand, dealerHand, value = dealhands(deck)
    dealerHand, playerHand, deck, dealerValue = playerChoice(playerHand, dealerHand, deck)
    score = WonLossTie(dealerValue, dealerHand, playerHand, deck, score)
    continuePlaying(score, seedValue, deck)
    return


x = random.randint(0,10000)
main(x)
