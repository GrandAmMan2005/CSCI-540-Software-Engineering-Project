import random
# random utility imported

from Cards import Card
# importing card class from cards file

from Deck import Deck


# importing Deck class from Deck file


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def addCard(self, card):
        self.cards.append(card)
        self.value += card.getNumber()

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getCards(self):
        new = []
        for i in self.cards:
            new.append(i.cardStr())
        return new


# method to initilize the different hands and the deck


def createGame():
    result = ''
    deck = Deck()
    deck.shuffle()
    dealerHand = Hand()
    (dealerHand, deck, result) = hit(dealerHand, deck)
    playerHand = Hand()
    (playerHand, deck, result) = hit(playerHand, deck)
    (playerHand, deck, result) = hit(playerHand, deck)
    return deck, dealerHand, playerHand



# different methods to easily determine results throughout the game
def win():
    return "Win"


def loss():
    return "Loss"


def tie():
    return "Tie"


def compareHands(dealerHand, playerHand):  # compares the hands and determines result
    if dealerHand == playerHand and playerHand <= 21:
        return tie()
    elif dealerHand < playerHand and dealerHand <= 21 and playerHand <= 21:
        return win()
    else:
        return loss()


def hit(hand, deck):  # adds another card to user's hand
    card = deck.drawCard()
    hand.addCard(card)
    if hand.getValue() <= 21:
        result = ''
        return hand, deck, result
    elif hand.getValue() > 21:
        result = "Loss"
        return hand, deck, result


# computes dealer hand then compares the two then returns the result of the games
def passTurn(dealerHand,playerHand):
    return compareHands(dealerHand.getValue(), playerHand.getValue())


def dealerHandComputation(dealerHand, deck):
    (dealerHand, deck, result) = hit(dealerHand, deck)
    while dealerHand.getValue() < 17:
        (dealerHand, deck, result) = hit(dealerHand, deck)
    if dealerHand.getValue() <= 21:
        return dealerHand
    else:
        dealerHand.setValue(0)
        return dealerHand
