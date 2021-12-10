import random

import Wheel

import Position


def createGame():
    userBet = placeBet()
    actualPosition = spinWheel()
    placeHolder = actualPosition.Wheel()
    placeHolderTwo = Wheel(actualPosition)
    result = compareBet(userBet, actualPosition)
    if result:
        win()
    else:
        loss()


def compareBet(predicted, actual):
    if predicted == actual:
        return True
    else:
        return False


def placeBet():
    choice = random(0, 36)
    return choice


def spinWheel():
    ball = random(0, 36)
    return ball


def win():
    return "Win"


def loss():
    return "Loss"
