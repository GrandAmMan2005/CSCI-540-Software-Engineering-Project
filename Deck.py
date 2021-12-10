import random

from Cards import Card
# importing card class from cards file

# populating deck with every unique card in a 52 card deck for use in game


class Deck:
    def __init__(self):
        self.deck = [
        Card('C',1,False,"A"),
        Card('C',2,False,''),
        Card('C',3,False,''),
        Card('C',4,False,''),
        Card('C',5,False,''),
        Card('C',6,False,''),
        Card('C',7,False,''),
        Card('C',8,False,''),
        Card('C',9,False,''),
        Card('C',10,False,''),
        Card('C',11,True,'J'),
        Card('C',12,True,'Q'),
        Card('C',13,True,'K'),
        Card('D',1,False,"A"),
        Card('D',2,False,''),
        Card('D',3,False,''),
        Card('D',4,False,''),
        Card('D',5,False,''),
        Card('D',6,False,''),
        Card('D',7,False,''),
        Card('D',8,False,''),
        Card('D',9,False,''),
        Card('D',10,False,''),
        Card('D',11,True,'J'),
        Card('D',12,True,'Q'),
        Card('D',13,True,'K'),
        Card('H',1,False,"A"),
        Card('H',2,False,''),
        Card('H',3,False,''),
        Card('H',4,False,''),
        Card('H',5,False,''),
        Card('H',6,False,''),
        Card('H',7,False,''),
        Card('H',8,False,''),
        Card('H',9,False,''),
        Card('H',10,False,''),
        Card('H',11,True,'J'),
        Card('H',12,True,'Q'),
        Card('H',13,True,'K'),
        Card('S',1,False,"A"),
        Card('S',2,False,''),
        Card('S',3,False,''),
        Card('S',4,False,''),
        Card('S',5,False,''),
        Card('S',6,False,''),
        Card('S',7,False,''),
        Card('S',8,False,''),
        Card('S',9,False,''),
        Card('S',10,False,''),
        Card('S',11,True,'J'),
        Card('S',12,True,'Q'),
        Card('S',13,True,'K')]

    def shuffle(self):
        random.shuffle(self.deck)

    def drawCard(self):
        singleCard = self.deck.pop()
        if singleCard.getFace() == True:
            singleCard.setNumber(10)
        if singleCard.getNumber() == 1:
            singleCard.setNumber(11)

        return singleCard
