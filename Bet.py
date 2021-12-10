import Database

def startingBet(username,amount):
    newBalance = Database.withdrawBalance(username=username, amount=amount)
    return newBalance

def bettingResult(username,amount,result,multiplier):
    if result == "Win":
        Database.depositBalance(username,amount=amount*multiplier)
    elif result == "Tie":
        Database.depositBalance(username,amount)