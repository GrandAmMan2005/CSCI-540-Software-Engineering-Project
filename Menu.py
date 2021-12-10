"""Imports"""
from random import randint
from tkinter import *
from tkinter import ttk
import tkinter
import Database
import Slots
import BlackJack
from PIL import Image, ImageTk


class Log_In:
    """
    Class - Log In
    This class handles the User Interface and User Experience
    For the log in page and its family of windows.  That will
    include windows such as create new account, log in to account,
    and password reset windows.
    """

    def __init__(self, root):
        """
        Initialization Method - Takes in self & root.  Root represents
        the master window of the application.
        """
        # Root Configuration
        self.root = root
        self.root.title('Card-Holders Login')
        # self.root.iconbitmap("Cardholders Logo - Icon.ico")

        # Exit button
        kill = Button(root, text='Exit', font='Sans 10', command=root.destroy)
        kill.config(anchor="e")
        kill.pack(side=TOP, anchor="ne", padx=5, pady=5)

        # Title Label
        t = Label(text='Card-Holders Virtual Casino', font='Sans 20')
        # Subtitle Label
        l = Label(text='Log In', font='Sans 10')
        # Label Configuration
        t.config(anchor="center")
        t.pack()
        l.config(anchor="center")
        l.pack()

        # Login
        # username label and text entry box
        usernameLabel = Label(root, text="User Name", font="Sans 12").pack()
        global username_g
        username = StringVar()
        username_g = username
        username_g.set('')
        usernameEntry = Entry(root, textvariable=username).pack()

        # password label and password entry box
        passwordLabel = Label(root, text="Password", font="Sans 12").pack()
        password = StringVar()
        passwordEntry = Entry(root, textvariable=password, show='*').pack()

        def validate_login(result):
            if result == "Fails":
                bad_result = Label(root, text="You have incorrectly entered your password")
                bad_result.pack(anchor="center")
            else:
                good_result = Label(root, text="You have successfully logged in!")
                good_result.pack(anchor="center")
                master = Tk()
                w = 1024
                h = 720
                w_width = master.winfo_screenwidth()
                w_height = master.winfo_screenheight()
                position_right = int(w_width/2 - w/2)
                position_down = int(w_height/2 - h/2)
                master.geometry(f"{w}x{h}+{position_right}+{position_down}")
                master_application = Main_Menu(master)
                root.destroy()

        # login button
        loginButton = Button(root, text="Login", font='Sans 10',
                             command=lambda: [validate_login(Database.login(username.get(), password.get()))])
        loginButton.pack()
        # Bind Enter Key to Log in
        root.bind('<Return>',
                  lambda x: [validate_login(Database.login(username.get(), password.get()))])
        # New Profile Button
        # new_profile = Button(root, text="Click here to create a new profile", command=self.Open_New_User)
        new_profile = Button(root, text="New User", font='Sans 10', command=self.Open_New_User)
        new_profile.pack(anchor="s", pady="40")
        # new_profile.pack(anchor="s", pady=75)

    def Open_New_User(self):
        # Window Creation & Configuration
        top = Toplevel()
        top.title('Card-Holders - New User Creation')
        # top.iconbitmap("Cardholders Logo - Icon.ico")
        top.geometry("600x400")
        top.resizable(width=False, height=False)

        # User Name entry
        new_user_label = Label(top, text='New Username', font="Sans 12").pack(anchor="center")
        new_user = StringVar()
        new_user_entry = Entry(top, textvariable=new_user).pack()

        # Password entry
        password_label = Label(top, text='New Password', font="Sans 12").pack(anchor="center")
        new_password = StringVar()
        # print(new_password.get())
        password_entry = Entry(top, textvariable=new_password, show='*').pack()

        password_label_2 = Label(top, text='RE-Enter your Password', font="Sans 12").pack(anchor="center")
        new_password_2 = StringVar()
        password_2_entry = Entry(top, textvariable=new_password_2, show='*').pack()

        # Security Questions
        sec_label = Label(top, text='What is your favorite color', font="Sans 12").pack()
        sec_question_1 = StringVar()
        sec_entry = Entry(top, textvariable=sec_question_1).pack()

        sec_label = Label(top, text='What city were you born in', font="Sans 12").pack()
        sec_question_2 = StringVar()
        sec_entry = Entry(top, textvariable=sec_question_2).pack()

        def print_success():
            create_success = Label(root, text='You have successfully created your account!', font="Sans 12")
            create_success.pack(anchor="center")

        # Create Button
        create = Button(top, text='Create your Account!', font="Sans 10", padx=2.5, pady=2.5,
                        command=lambda: [Database.creatingAccount(new_user.get(), new_password.get(),
                                                                  new_password_2.get(), sec_question_1.get(),
                                                                  sec_question_2.get()), print_success(),
                                         top.destroy()])
        # User needs feedback to know that account has been created.
        create.pack(anchor="center")

        # Cancel Button
        cancel = Button(top, text='Cancel', font="Sans 12", command=top.destroy).pack()


class Main_Menu:
    """I'm being lazy today about writing comments, come back to this at another time."""

    def __init__(self, root):
        """I'll write the documentation at another time."""
        self.root = root
        self.root.title('Card-Holders Main Menu')
        # self.root.iconbitmap("Cardholders Logo - Icon.ico")
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.after_idle(self.root.attributes, '-topmost', False)
        # Balance Label
        global username_g
        bal = Database.getBalance(username_g.get())
        balance = Label(root, text=f'Account Balance: {bal}', font='Sans 16')
        balance.config(anchor="e")
        balance.pack(side=TOP, anchor="e", padx=5, pady=5)
        # Exit button
        kill = Button(root, text='Log Out', command=lambda: [root.destroy(), return_to_login(self)])
        kill.config(anchor="w")
        kill.pack(side=TOP, anchor="nw", padx=5, pady=5)

        # Settings button
        settings = Button(root, text='Settings', command=lambda: settings_menu(self))
        settings.config(anchor="w")
        settings.pack(side=TOP, anchor="w", padx=5, pady=5)

        # Profile button
        profile = Button(root, text='Profile & Statistics', command=lambda: profile_menu(self))
        profile.config(anchor="n")
        profile.pack(side=TOP, anchor="w", padx=5, pady=5)

        # Title
        title = Label(root, text='Card-Holders: Virtual Casino', font='Sans 32')
        title.pack()

        # User label
        # user_label = Label(root, text=)

        # Blackjack
        blackjack_button = Button(root, text='Play Blackjack', command=lambda: blackjack_start(self), height=5,
                                  width=15, padx=5, pady=5, font="Sans 16")
        blackjack_button.config(anchor="center")
        blackjack_button.pack(side=TOP)

        # Slots
        slots_button = Button(root, text='Play Slots', command=lambda: slots_start(self), height=5, width=15, padx=5,
                              pady=5, font="Sans 16")
        slots_button.config(anchor="center")
        slots_button.pack()

        # Roulette

        def return_to_login(self):
            widget = Tk()
            w = 500
            h = 400
            w_width = widget.winfo_screenwidth()
            w_height = widget.winfo_screenheight()
            position_right = int(w_width/2 - w/2)
            position_down = int(w_height/2 - h/2)
            widget.geometry(f"{w}x{h}+{position_right}+{position_down}")
            widget_application = Log_In(widget)

        def settings_menu(self):
            sett = Tk()
            w = 500
            h = 400
            w_width = sett.winfo_screenwidth()
            w_height = sett.winfo_screenheight()
            position_right = int(w_width/2 - w/2)
            position_down = int(w_height/2 - h/2)
            sett.geometry(f"{w}x{h}+{position_right}+{position_down}")
            sett.title('Card-Holders - User Settings')
           #  sett.iconbitmap("Cardholders Logo - Icon.ico")

        def profile_menu(self):
            prof = Tk()
            w = 500
            h = 400
            w_width = prof.winfo_screenwidth()
            w_height = prof.winfo_screenheight()
            position_right = int(w_width/2 - w/2)
            position_down = int(w_height/2 - h/2)
            prof.geometry(f"{w}x{h}+{position_right}+{position_down}")
            prof.title('Card-Holders - User Profile')
            # prof.iconbitmap("Cardholders Logo - Icon.ico")

            welcome_label = Label(prof, text='Welcome ' + username_g.get(), font='Sans 16')
            welcome_label.config(anchor="center")
            welcome_label.pack()

            # Database.depositBalance(username_g, 300)
            balance_label = Label(prof, text='Your Balance is: ' + str(Database.getBalance(username_g.get())), font='Sans 12')
            balance_label.config(anchor="center")
            balance_label.pack()

            games_won_label = Label(prof, text='You have won ' + str(Database.getGamesWon(username_g.get())) + ' games', font='Sans 12')
            games_won_label.config(anchor="center")
            games_won_label.pack()

            games_played_label = Label(prof,
                                       text='You have played a total of ' + str(Database.getTotalGamesPlayed(username_g.get())) + ' games',
                                       font='Sans 12')
            games_played_label.config(anchor="center")
            games_played_label.pack()

            if Database.getTotalGamesPlayed(username_g.get()) == 0:
                l_ratio = Label(prof, text='You have not played any games!', font='Sans 12')
            else:
                winrate = Database.getGamesWon(username_g.get())/Database.getTotalGamesPlayed(username_g.get())
                l_ratio = Label(prof, text='Your win rate is ' + str(round(winrate, 3)*100) + '%', font='Sans 12')
            l_ratio.config(anchor="center")
            l_ratio.pack()

            # Use plt.show to get *a* chart
            '''
            data = [Database.getGamesWon(username_g.get()), Database.getTotalGamesPlayed(username_g.get()) - Database.getGamesWon(username_g.get())]
            labels = ['Wins', 'Losses']
            pie = plt.pie(x=data, labels=labels, autopct='%1.1f%%')
            plt.pie(x=data, labels=labels, autopct='%1.1f%%')
            plt.title('Wins and Losses')
            plt.show()

            pie = Figure(figsize=(5, 5))
            a = pie.add_subplot(111)
            a.pie([Database.getGamesWon(username_g.get()), Database.getTotalGamesPlayed(username_g.get()) - Database.getGamesWon(username_g.get())])
            a.legend([Database.getTotalGamesPlayed(username_g.get()) - Database.getGamesWon(username_g.get())])
            '''

        def play_blackjack(self,bet):
            # Window Configuration
            root.destroy()
            global play_blackjack
            play_blackjack = Tk()
            w = 650
            h = 500
            w_width = play_blackjack.winfo_screenwidth()
            w_height = play_blackjack.winfo_screenheight()
            position_right = int(w_width/2 - w/2)
            position_down = int(w_height/2 - h/2)
            play_blackjack.geometry(f"{w}x{h}+{position_right}+{position_down}")
            play_blackjack.title('Card-Holders - Blackjack')
          #   play_blackjack.iconbitmap("Cardholders Logo - Icon.ico")

            # Title Screen
            title = Label(play_blackjack, text='Welcome to Blackjack!', font='Sans 16')
            title.grid(row=0,column=4)

            

            def pass_hand(deck, dealer, player, bet):
                dealer = BlackJack.dealerHandComputation(dealer,deck)
                game(deck,dealer,player,"",bet)
                result = BlackJack.passTurn(dealer, player)
                result_screen(self,result,bet)

            def hit_hand(player, deck, dealer, bet):
                (player, deck, result) = BlackJack.hit(player, deck)

                if result == '':
                    game(deck=deck,dealer=dealer,player=player,result=result, bet=bet)
                else:
                    game(deck=deck,dealer=dealer,player=player,result="Bust", bet=bet)
                    result_screen(self,"Bust",bet)

            def begin_game(bet):
                global username_g
                Database.withdrawBalance(username_g.get(),bet)
                (deck, dealer, player) = BlackJack.createGame()
                game(deck=deck,dealer=dealer,player=player,result="",bet=bet)

            def game(deck,dealer,player,result,bet):
                d_label = Label(play_blackjack, text='Dealers Hand: ')
                d_label.grid(row=3, column=8)
                player_label = Label(play_blackjack, text='Your Hand: ')
                player_label.grid(row=3, column=2)
                # show dealer hand

                # show player cards

                dealer_cards = []
                for card in dealer.getCards():
                    image = Image.open("images/"+card+".png")
                    image = image.resize((100,153),Image.ANTIALIAS)
                    dealer_cards.append(image)

                if len(dealer_cards) >= 1:
                    dealer_card1 = ImageTk.PhotoImage(dealer_cards[0])
                    dc1l = tkinter.Label(justify="right", image=dealer_card1)
                    dc1l.image = dealer_card1
                    dc1l.grid(row=5,column=8)
                    if len(dealer_cards) >= 2:
                        dealer_card2 = ImageTk.PhotoImage(dealer_cards[1])
                        dc2l = tkinter.Label(justify="right", image=dealer_card2)
                        dc2l.image = dealer_card2
                        dc2l.grid(row=5,column=9)
                        if len(dealer_cards) >= 3:
                            dealer_card3 = ImageTk.PhotoImage(dealer_cards[2])
                            dc3l = tkinter.Label(justify="right", image=dealer_card3)
                            dc3l.image = dealer_card3
                            dc3l.grid(row=6,column=8)
                            if len(dealer_cards) >= 4:
                                dealer_card4 = ImageTk.PhotoImage(dealer_cards[3])
                                dc4l = tkinter.Label(justify="right", image=dealer_card4)
                                dc4l.image = dealer_card4
                                dc4l.grid(row=6,column=9)
                                if len(dealer_cards) >= 5:
                                    dealer_card5 = ImageTk.PhotoImage(dealer_cards[4])
                                    dc5l = tkinter.Label(justify="right", image=dealer_card5)
                                    dc5l.image = dealer_card5
                                    dc5l.grid(row=7,column=8)
                                    if len(dealer_cards) >= 6:
                                        dealer_card6 = ImageTk.PhotoImage(dealer_cards[5])
                                        dc6l = tkinter.Label(justify="right", image=dealer_card6)
                                        dc6l.image = dealer_card6
                                        dc6l.grid(row=7,column=9)
                                        if len(dealer_cards) >= 7:
                                            dealer_card7 = ImageTk.PhotoImage(dealer_cards[6])
                                            dc7l = tkinter.Label(justify="right", image=dealer_card7)
                                            dc7l.image = dealer_card7
                                            dc7l.grid(row=8,column=8)
                                            if len(dealer_cards) >= 8:
                                                dealer_card8 = ImageTk.PhotoImage(dealer_cards[7])
                                                dc8l = tkinter.Label(justify="right", image=dealer_card8)
                                                dc8l.image = dealer_card8
                                                dc8l.grid(row=8,column=9)
            
                
                player_cards = []
                for card in player.getCards():
                    image = Image.open("images/" + card + ".png")
                    image = image.resize((100, 153), Image.ANTIALIAS)
                    player_cards.append(image)

                if len(player_cards) >= 1:
                    player_card1 = ImageTk.PhotoImage(player_cards[0])
                    pc1l = tkinter.Label(justify="right", image=player_card1)
                    pc1l.image = player_card1
                    pc1l.grid(row=5,column=2)
                    if len(player_cards) >= 2:
                        player_card2 = ImageTk.PhotoImage(player_cards[1])
                        pc2l = tkinter.Label(justify="right", image=player_card2)
                        pc2l.image = player_card2
                        pc2l.grid(row=5,column=3)
                        if len(player_cards) >= 3:
                            player_card3 = ImageTk.PhotoImage(player_cards[2])
                            pc3l = tkinter.Label(justify="right", image=player_card3)
                            pc3l.image = player_card3
                            pc3l.grid(row=6,column=2)
                            if len(player_cards) >= 4:
                                player_card4 = ImageTk.PhotoImage(player_cards[3])
                                pc4l = tkinter.Label(justify="right", image=player_card4)
                                pc4l.image = player_card4
                                pc4l.grid(row=6,column=3)
                                if len(player_cards) >= 5:
                                    player_card5 = ImageTk.PhotoImage(player_cards[4])
                                    pc5l = tkinter.Label(justify="right", image=player_card5)
                                    pc5l.image = player_card5
                                    pc5l.grid(row=7,column=2)
                                    if len(player_cards) >= 6:
                                        player_card6 = ImageTk.PhotoImage(player_cards[5])
                                        pc6l = tkinter.Label(justify="right", image=player_card6)
                                        pc6l.image = player_card6
                                        pc6l.grid(row=7,column=3)
                                        if len(player_cards) >= 7:
                                            player_card7 = ImageTk.PhotoImage(player_cards[6])
                                            pc7l = tkinter.Label(justify="right", image=player_card7)
                                            pc7l.image = player_card7
                                            pc7l.grid(row=8,column=2)
                                            if len(player_cards) >= 8:
                                                player_card8 = ImageTk.PhotoImage(player_cards[7])
                                                pc8l = tkinter.Label(justify="right", image=player_card8)
                                                pc8l.image = player_card8
                                                pc8l.grid(row=8,column=3)


                # Pass Button
                if result != "Bust":
                    pass_button = Button(play_blackjack, text='Pass', command=lambda: [pass_button.destroy(),hit_button.destroy(),pass_hand(deck, dealer, player, bet)])
                    pass_button.grid(row=2,column=4)

                    # Hit Button
                    hit_button = Button(play_blackjack, text='Hit', command=lambda: [hit_button.destroy(),pass_button.destroy(),hit_hand(player, deck, dealer, bet)])
                    hit_button.grid(row=1,column=4,rowspan=1)


            # New Game 
            begin_game(bet)
        
        def blackjack_start(self):
            blackjack_start = Tk()
            w = 200
            h = 126
            w_width = blackjack_start.winfo_screenwidth()
            w_height = blackjack_start.winfo_screenheight()
            position_right = int(w_width/2 - w/2)
            position_down = int(w_height/2 - h/2)
            blackjack_start.geometry(f"{w}x{h}+{position_right}+{position_down}")
            blackjack_start.title('BJ-Start')
         #    blackjack_start.iconbitmap("Cardholders Logo - Icon.ico")
            title = Label(blackjack_start, text='Welcome to Blackjack!\nPlace your bet!', font='Sans 12')
            title.pack()

            bets = [5,10,25,50,100,500,1000]
            
            default_bet = IntVar()
            default_bet.set(bets[3])

            bet_option = OptionMenu(blackjack_start,default_bet,*bets)
            bet_option.config(font="Sans 10")
            bet_option.pack()

            def check_bal(bet):
                global username_g
                balance = Database.getBalance(username_g.get())
                if bet > balance:
                    error(self)
                else:
                    blackjack_start.destroy()
                    play_blackjack(self,bet)

            new_game = Button(blackjack_start, text='Start Game', padx=5, pady=5, command=lambda: check_bal(default_bet.get()))
            new_game.pack()
        
        def error(self):
            error = Tk()
            w = 235
            h = 85
            w_width = error.winfo_screenwidth()
            w_height = error.winfo_screenheight()
            position_right = int(w_width/2 - w/2)
            position_down = int(w_height/2 - h/2)
            error.geometry(f"{w}x{h}+{position_right}+{position_down}")
            error.title('Card-Holders - Error')
         #   error.iconbitmap("Cardholders Logo - Icon.ico")
            title = Label(error, text='Error!\nYou dont have enough credits', font='Sans 12')
            title.pack()
            close = Button(error, text='Close', padx=5, pady=5, command=lambda:error.destroy())
            close.pack()


        def result_screen(self,result,bet):
            result_screen = Tk()
            w = 250
            h = 100
            w_width = result_screen.winfo_screenwidth()
            w_height = result_screen.winfo_screenheight()
            position_right = int(w_width/2 - w/2)
            position_down = int(w_height/2 - h/2)
            result_screen.geometry(f"{w}x{h}+{position_right}+{position_down}")
            result_screen.title('Card-Holders - Result')
         #   result_screen.iconbitmap("Cardholders Logo - Icon.ico")
            global username_g
            Database.addToTotalGamesPlayed(username_g.get())
            if result == "Win":
                bet = bet*2
                Database.depositBalance(username_g.get(),bet)
                Database.addToGamesWon(username_g.get())
                title = Label(result_screen, text=f'You Won!\nCongrats!\nYou have won {bet} credits', font='Sans 12')
                title.pack()
            elif result == "Tie":
                Database.depositBalance(username_g.get(),bet)
                title = Label(result_screen, text=f'You Tied!\nTry Again!\nYou got back {bet} credits', font='Sans 12')
                title.pack()
            elif result == "Bust":
                title = Label(result_screen, text=f'You went over 21!\nBetter luck next time!\nYou lost {bet} credits', font='Sans 12')
                title.pack()
            else:
                title = Label(result_screen, text=f'Oh no!\nYou lost {bet} credits\nBetter luck next time!', font='Sans 12')
                title.pack()
            hit_button = Button(result_screen, text='Return', command=lambda: back())
            hit_button.pack()
            def back():
                master = Tk()
                w = 1024
                h = 720
                w_width = master.winfo_screenwidth()
                w_height = master.winfo_screenheight()
                position_right = int(w_width/2 - w/2)
                position_down = int(w_height/2 - h/2)
                master.geometry(f"{w}x{h}+{position_right}+{position_down}")
                master_application = Main_Menu(master)
                result_screen.destroy()
                global play_blackjack
                play_blackjack.destroy()
        
        def play_roulette(self):
            play_roulette = Tk()
            w = 800
            h = 600
            w_width = play_roulette.winfo_screenwidth()
            w_height = play_roulette.winfo_screenheight()
            position_right = int(w_width/2 - w/2)
            position_down = int(w_height/2 - h/2)
            play_roulette.geometry(f"{w}x{h}+{position_right}+{position_down}")
            play_roulette.title('Card-Holders - Roulette')
          #  play_roulette.iconbitmap("Cardholders Logo - Icon.ico")
            play_roulette.resizeable(width=False, height=False)

        def slots_start(self):
            slots_start = Tk()
            w = 200
            h = 126
            w_width = slots_start.winfo_screenwidth()
            w_height = slots_start.winfo_screenheight()
            position_right = int(w_width/2 - w/2)
            position_down = int(w_height/2 - h/2)
            slots_start.geometry(f"{w}x{h}+{position_right}+{position_down}")
            slots_start.title('Card-Holders - Slots')
         #   slots_start.iconbitmap("Cardholders Logo - Icon.ico")
            title = Label(slots_start, text='Welcome to Slots!\nPlace your bet!', font='Sans 12')
            title.pack()

            bets = [5,10,25,50,100,500,1000]
            
            default_bet = IntVar()
            default_bet.set(bets[3])

            bet_option = OptionMenu(slots_start,default_bet,*bets)
            bet_option.config(font="Sans 10")
            bet_option.pack()

            def check_bal(bet):
                global username_g
                balance = Database.getBalance(username_g.get())
                if bet > balance:
                    error(self)
                else:
                    slots_start.destroy()
                    play_slots(self,bet)

            new_game = Button(slots_start, text='Start Game', padx=5, pady=5, command=lambda: check_bal(default_bet.get()))
            new_game.pack()

        def play_slots(self, bet):
            root.destroy()
            global play_slots
            play_slots = Tk()
            w = 610
            h = 400
            w_width = play_slots.winfo_screenwidth()
            w_height = play_slots.winfo_screenheight()
            position_right = int(w_width/2 - w/2)
            position_down = int(w_height/2 - h/2)
            play_slots.geometry(f"{w}x{h}+{position_right}+{position_down}")
            play_slots.title('Card-Holders - Slots')
    #        play_slots.iconbitmap("Cardholders Logo - Icon.ico")
            
            welcome = Label(play_slots, text='Welcome to Slots!', font="Sans 16")
            welcome.config(anchor="center")
            welcome.grid(row=0,column=2)
            start_button = Button(play_slots, text='Play', command=lambda: [start_button.destroy(),get_results(c1,c2,c3,bet)], font="Sans 16")
            start_button.grid(row=3,column=2)
            color_combos = []
            colors = ['red','blue','yellow','green','gray','purple']
            for color in colors:
                temp = []
                card = Image.open(f"images/{color}_back.png")
                card = card.resize((200,305),Image.ANTIALIAS)
                card = ImageTk.PhotoImage(card)
                temp.append(card)
                card1 = Image.open(f"images/{color}_back_blur.png")
                card1 = card1.resize((200,305),Image.ANTIALIAS)
                card1 = ImageTk.PhotoImage(card1)
                temp.append(card1)
                color_combos.append(temp)

            c1 = color_combos[randint(0,5)]
            c2 = color_combos[randint(0,5)]
            c3 = color_combos[randint(0,5)]

            sc1 = tkinter.Label(image=c1[0])
            sc1.image = c1[0]
            sc1.grid(row=2,column=1)

            sc1 = tkinter.Label(image=c2[0])
            sc1.image = c2[0]
            sc1.grid(row=2,column=2)

            sc1 = tkinter.Label(image=c3[0])
            sc1.image = c3[0]
            sc1.grid(row=2,column=3)    
            
            
            def get_results(c1,c2,c3,bet):

                (result, first_result, second_result, third_result, modifier) = Slots.play()
                result_cards = [first_result,second_result,third_result]

                cards = []
                for card in result_cards:
                    image = Image.open("images/"+card+".png")
                    image = image.resize((200,305),Image.ANTIALIAS)
                    image = ImageTk.PhotoImage(image)
                    cards.append(image)

                sc1 = tkinter.Label(image=c1[1])
                sc1.image = c1[1]
                sc1.grid(row=2,column=1)
                
                sc1 = tkinter.Label(image=c2[1])
                sc1.image = c2[1]
                sc1.grid(row=2,column=2)

                sc1 = tkinter.Label(image=c3[1])
                sc1.image = c3[1]
                sc1.grid(row=2,column=3)
                
                global c
                c = 0

                b1 = Button(play_slots, text='Stop', command=lambda: [b1.destroy(),solve(1,cards[0]),check(result, modifier, bet)])
                b1.grid(row=3,column=1)

                b2 = Button(play_slots, text='Stop', command=lambda: [b2.destroy(),solve(2,cards[1]),check(result, modifier, bet)])
                b2.grid(row=3,column=2)

                b3 = Button(play_slots, text='Stop', command=lambda: [b3.destroy(),solve(3,cards[2]),check(result, modifier, bet)])
                b3.grid(row=3,column=3)

            def check(result, modifier, bet):
                global c
                if c == 2:
                    slots_result(self,result, bet, modifier)
                else:
                    c+=1
                    print(c)

            def solve(x,cards):
                sc1 = tkinter.Label(image=cards)
                sc1.image = cards
                sc1.grid(row=2,column=x)
        
        def slots_result(self, result, bet, modifier):
            result_screen = Tk()
            w = 250
            h = 100
            w_width = result_screen.winfo_screenwidth()
            w_height = result_screen.winfo_screenheight()
            position_right = int(w_width/2 - w/2)
            position_down = int(w_height/2 - h/2)
            result_screen.geometry(f"{w}x{h}+{position_right}+{position_down}")
            result_screen.title('Card-Holders - Result')
          #  result_screen.iconbitmap("Cardholders Logo - Icon.ico")
            global username_g
            Database.addToTotalGamesPlayed(username_g.get())
            if result == "Win":
                bet = bet*modifier
                Database.depositBalance(username_g.get(),bet)
                Database.addToGamesWon(username_g.get())
                title = Label(result_screen, text=f'You Won!\nCongrats!\nYou have won {bet} credits', font='Sans 12')
                title.pack()
            else:
                title = Label(result_screen, text=f'Oh no!\nYou did not win anything\nBetter luck next time!', font='Sans 12')
                title.pack()
            hit_button = Button(result_screen, text='Return', command=lambda: back())
            hit_button.pack()
            def back():
                master = Tk()
                w = 1024
                h = 720
                w_width = master.winfo_screenwidth()
                w_height = master.winfo_screenheight()
                position_right = int(w_width/2 - w/2)
                position_down = int(w_height/2 - h/2)
                master.geometry(f"{w}x{h}+{position_right}+{position_down}")
                master_application = Main_Menu(master)
                result_screen.destroy()
                global play_slots
                play_slots.destroy()
            
        

if __name__ == '__main__':
    # I'll come back around to write up documentation for this LATER!!!!!!!
    root = Tk()
    w = 500
    h = 400
    w_width = root.winfo_screenwidth()
    w_height = root.winfo_screenheight()
    position_right = int(w_width/2 - w/2)
    position_down = int(w_height/2 - h/2)
    root.geometry(f"{w}x{h}+{position_right}+{position_down}")
    application = Log_In(root)
    root.mainloop()
