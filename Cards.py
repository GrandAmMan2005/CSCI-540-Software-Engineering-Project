"""
CardsClass
The purpose of this class is to define the 'Card' object for use in
the Blackjack game of the app.  It takes in three parameters; Suite,
Number, and Color.  The four possible Suites are Spades, Clubs, Diamonds,
Hearts.  The possible numbers range from 1 - Ace, 2, 3, 4, 5, 6, 7, 8,
9, 10, 11 - Jack, 12 - Queen, King - 13. I also added the Color variable in
the event that we end up needing it for another game (like Solitaire).
- Alex
"""


class Card:
    def __init__(self,suit,number,isFace,rank):
        self.suit = suit
        self.number = number
        self.isFace = isFace
        self.rank = rank

    def setSuit(self, suit):
        self.suit = suit

    def setNumber(self, number):
        self.number = number

    def getNumber(self):
        return self.number

    def getFace(self):
        return self.isFace

    def cardStr(self):
        if self.rank != "":
            return self.rank + "" + self.suit
        else:
            return str(self.number) + "" + self.suit
