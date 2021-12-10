import sqlite3

# creating a table
# cursor.execute("""CREATE TABLE users (
#            username TEXT PRIMARY KEY,
#            password TEXT,
#            securityQuestion1 TEXT,
#            securityQuestion2 TEXT,
#            balance INTEGER,
#            gamesWon INTEGER,
#            totalGamesPlayed INTEGER
#            )""")

# Methods to connect to db
# checks to see if two passwords are similar
def passwordCheck(password1, password2):
    return password1 == password2


def login(username, password):
    # connecting to a database
    conn = sqlite3.connect('user.db')
    # creating a cursor
    cur = conn.cursor()
    # this is SQL code to find the username in the database
    cur.execute("SELECT * FROM users WHERE username = '{un}'".format(un=username))
    password2 = cur.fetchone()[1]
    # does a password check and if it passes it will pass on the username
    if passwordCheck(password, password2):
        return username
    # return "Fails" if password is wrong
    else:
        return "Fails"


def creatingAccount(username, password1, password2, security1, security2):
    if passwordCheck(password1, password2):
        # connecting to a database & creating cursor
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        # when user is creating account it creates a new record in the db
        cur.execute("INSERT INTO users VALUES ('{us}','{pw}','{s1}','{s2}','{bal}','{gw}','{tgp}')".format(
            us=username,
            pw=password1,
            s1=security1,
            s2=security2,
            bal=1000,  # starting balance
            gw=0,  # games won
            tgp=0  # total games played
        ))
        # committing the new record into the database
        conn.commit()

def getBalance(username):
    # connecting to a database
    conn = sqlite3.connect('user.db')
    # creating a cursor
    cur = conn.cursor()
    # this is SQL code to find the username in the database
    cur.execute("SELECT * FROM users WHERE username = '{un}'".format(un=username))
    # fetches the balance and returns it
    balance = cur.fetchone()[4]
    return balance

def withdrawBalance(username,amount):
    # connecting to a database
    conn = sqlite3.connect('user.db')
    # creating a cursor
    cur = conn.cursor()
    # this is SQL code to find the username in the database
    cur.execute("SELECT * FROM users WHERE username = '{un}'".format(un=username))
    balance = cur.fetchone()[4]
    # checks to see if the amount can be taken from the account, if it cant it fails
    if balance > amount:
        # calculates the new balance
        newBalance = int(balance) - amount
        # executing the sql code to update the record in database and committing the changes
        cur.execute("UPDATE users SET balance = '{nb}' WHERE username = '{un}'".format(nb = newBalance,un=username))
        conn.commit()
        # returns the new balance
        return newBalance
    else:
        return "Fails"

def depositBalance(username,amount):
    # connecting to a database
    conn = sqlite3.connect('user.db')
    # creating a cursor
    cur = conn.cursor()
    # this is SQL code to find the username in the database
    cur.execute("SELECT * FROM users WHERE username = '{un}'".format(un=username))
    balance = cur.fetchone()[4]
    newBalance = int(balance) + amount
    cur.execute("UPDATE users SET balance = '{nb}' WHERE username = '{un}'".format(nb = newBalance,un=username))
    conn.commit()
    return newBalance

def addToGamesWon(username):
    # connecting to a database
    conn = sqlite3.connect('user.db')
    # creating a cursor
    cur = conn.cursor()
    # this is SQL code to find the username in the database
    cur.execute("SELECT * FROM users WHERE username = '{un}'".format(un=username))
    # fetches the games won and adds one to it
    gamesWon = cur.fetchone()[5]
    newGamesWon = int(gamesWon) + 1
    # executing the sql code to update the record in database and committing the changes
    cur.execute("UPDATE users SET gamesWon = '{ngw}' WHERE username = '{un}'".format(ngw = newGamesWon,un=username))
    conn.commit()

def addToTotalGamesPlayed(username):
    # connecting to a database
    conn = sqlite3.connect('user.db')
    # creating a cursor
    cur = conn.cursor()
    # this is SQL code to find the username in the database
    cur.execute("SELECT * FROM users WHERE username = '{un}'".format(un=username))
    # fetches the total games and adds one to it
    totalGamesPlayed = cur.fetchone()[6]
    newTotalGamesPlayed = int(totalGamesPlayed) + 1
    # executing the sql code to update the record in database and committing the changes
    cur.execute("UPDATE users SET totalGamesPlayed = '{tgp}' WHERE username = '{un}'".format(tgp = newTotalGamesPlayed,un=username))
    conn.commit()

def getGamesWon(username):
    # connecting to a database
    conn = sqlite3.connect('user.db')
    # creating a cursor
    cur = conn.cursor()
    # this is SQL code to find the username in the database
    cur.execute("SELECT * FROM users WHERE username = '{un}'".format(un=username))
    # fetches the games won and returns it
    gamesWon = cur.fetchone()[5]
    return gamesWon

def getTotalGamesPlayed(username):
    # connecting to a database
    conn = sqlite3.connect('user.db')
    # creating a cursor
    cur = conn.cursor()
    # this is SQL code to find the username in the database
    cur.execute("SELECT * FROM users WHERE username = '{un}'".format(un=username))
    # fetches the total games and returns it
    totalGamesPlayed = cur.fetchone()[6]
    return totalGamesPlayed
