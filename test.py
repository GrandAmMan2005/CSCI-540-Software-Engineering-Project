import BlackJack
from BlackJack import Hand
while(True):
    (deck, dealerHand, playerHand) = BlackJack.createGame()
    result = ""
    print("dealer's hand"+str(dealerHand.getCards()))
    print("player's hand"+str(playerHand.getCards()))
    while(True):
        if input("h/p: ") == "h" and result == '' and playerHand.getValue() <= 21:
            (playerHand,deck,result) = BlackJack.hit(playerHand,deck)
            print("player's hand"+str(playerHand.getCards()))
        else:
            break



    dealerHand = BlackJack.dealerHandComputation(dealerHand,deck)
    print("dealer's hand"+str(dealerHand.getCards()))
    if result == "":
        result = BlackJack.passTurn(playerHand,dealerHand,deck)
    print("You " + result)
    if input("continue? y/n: ") == "n":
        break