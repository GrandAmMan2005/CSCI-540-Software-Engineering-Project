import random

# Still need bet and win methods, as well as more elegant display methods

# Creating tuple of arrays for each possible outcome, sorted losses first, then by increasing payout
outcomes = (
    # Losses Starting with Jack
    ["J", "Q", "K"], ["J", "Q", "A"], ["J", "Q", "7"],
    ["J", "K", "Q"], ["J", "K", "A"], ["J", "K", "7"],
    ["J", "A", "Q"], ["J", "A", "K"], ["J", "A", "7"],
    ["J", "7", "Q"], ["J", "7", "K"], ["J", "7", "A"],

    # Losses Starting with Queen
    ["Q", "J", "K"], ["Q", "J", "A"], ["Q", "J", "7"],
    ["Q", "K", "J"], ["Q", "K", "A"], ["Q", "K", "7"],
    ["Q", "A", "J"], ["Q", "A", "K"], ["Q", "A", "7"],
    ["Q", "7", "J"], ["Q", "7", "K"], ["Q", "7", "A"],

    # Losses Starting with King
    ["K", "J", "Q"], ["K", "J", "A"], ["K", "J", "7"],
    ["K", "Q", "J"], ["K", "Q", "A"], ["K", "Q", "7"],
    ["K", "A", "J"], ["K", "A", "Q"], ["K", "A", "7"],
    ["K", "7", "J"], ["K", "7", "Q"], ["K", "7", "A"],

    # Losses Starting with Ace
    ["A", "J", "Q"], ["A", "J", "K"], ["A", "J", "7"],
    ["A", "Q", "J"], ["K", "Q", "K"], ["A", "Q", "7"],
    ["A", "K", "J"], ["A", "K", "Q"], ["A", "K", "7"],
    ["A", "7", "J"], ["A", "7", "Q"], ["A", "7", "K"],

    # Losses Starting with 7
    ["7", "J", "Q"], ["7", "J", "K"], ["7", "J", "A"],
    ["7", "Q", "J"], ["7", "Q", "K"], ["7", "Q", "A"],
    ["7", "K", "J"], ["7", "K", "Q"], ["7", "K", "A"],
    ["7", "A", "J"], ["7", "A", "Q"], ["7", "A", "K"],

    # Jack Pairs
    ["J", "J", "Q"], ["J", "J", "K"], ["J", "J", "A"], ["J", "J", "7"],
    ["J", "Q", "J"], ["J", "K", "J"], ["J", "A", "J"], ["J", "7", "J"],
    ["Q", "J", "J"], ["K", "J", "J"], ["A", "J", "J"], ["7", "J", "J"],

    # Queen Pairs
    ["Q", "Q", "J"], ["Q", "Q", "K"], ["Q", "Q", "A"], ["Q", "Q", "7"],
    ["Q", "J", "Q"], ["Q", "K", "Q"], ["Q", "A", "Q"], ["Q", "7", "Q"],
    ["J", "Q", "Q"], ["K", "Q", "Q"], ["A", "Q", "Q"], ["7", "Q", "Q"],

    # King Pairs
    ["K", "K", "J"], ["K", "K", "Q"], ["K", "K", "A"], ["K", "K", "7"],
    ["K", "J", "K"], ["K", "Q", "K"], ["K", "A", "K"], ["K", "7", "K"],
    ["J", "K", "K"], ["Q", "K", "K"], ["A", "K", "K"], ["7", "K", "K"],

    # Ace Pairs
    ["A", "A", "J"], ["A", "A", "Q"], ["A", "A", "K"], ["A", "A", "7"],
    ["A", "J", "A"], ["A", "Q", "A"], ["A", "K", "A"], ["A", "7", "A"],
    ["J", "A", "A"], ["Q", "A", "A"], ["K", "A", "A"], ["7", "A", "A"],

    # 7 Pairs
    ["7", "7", "J"], ["7", "7", "Q"], ["7", "7", "K"], ["7", "7", "A"],
    ["7", "J", "7"], ["7", "Q", "7"], ["7", "K", "7"], ["7", "A", "7"],
    ["J", "7", "7"], ["Q", "7", "7"], ["K", "7", "7"], ["A", "7", "7"],

    # Triples
    ["J", "J", "J"],
    ["Q", "Q", "Q"],
    ["K", "K", "K"],
    ["A", "A", "A"],
    ["7", "7", "7"],
)

# List that tells if any given outcome is a win or loss
win = []
for i in range(0, 60):
    win.append(False)
for i in range(60, 125):
    win.append(True)

# List for storing proper win modifiers
modifier = []
# All losses
for i in range(0, 60):
    modifier.append(0)
# Wins with 2 Jacks
for i in range(60, 72):
    modifier.append(1.2)
# Wins with 2 Queens
for i in range(72, 84):
    modifier.append(1.4)
# Wins with 2 Kings
for i in range(84, 96):
    modifier.append(1.6)
# Wins with 2 Aces
for i in range(96, 108):
    modifier.append(1.8)
# Wins with 2 Lucky 7s
for i in range(108, 120):
    modifier.append(2.0)
# All Jacks
modifier.append(4.0)
# All Queens
modifier.append(6.0)
# All Kings
modifier.append(8.0)
# All Aces
modifier.append(10.0)
# All 7s
modifier.append(20.0)


# Method to generate a random index from 0 to 124 to signify an outcome and payout
def generate_index():
    return random.randint(0, 124)


# Method to define how games are played
def play():
    # Use generate index to set result
    result = generate_index()
    # Store each individual slot as a variable so it can be read easily
    suits = ["D", "H", "C", "S"]

    firstResult = outcomes[result][0] + suits[random.randint(0, 3)]
    secondResult = outcomes[result][1] + suits[random.randint(0, 3)]
    thirdResult = outcomes[result][2] + suits[random.randint(0, 3)]

    if win[result]:
        win_str = "Win"

        return win_str, firstResult, secondResult, thirdResult, modifier[result]
    else:
        loss_str = "Loss"

        return loss_str, firstResult, secondResult, thirdResult, modifier[result]


