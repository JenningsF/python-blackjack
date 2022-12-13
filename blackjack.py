import random
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10, "Ace":11}

playing = True

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:

    def __init__(self):
        self.deck = [] # start as an empty list
        for suit in suits:
            for rank in ranks:
                # Creating Card object
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []  # start as an empty list with no cards
        self.value = 0  # start with a zero value
        self.aces = 0   # start with zero aces in hand

    # A single card passed in from Deck.deal()
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        # Tracks aces
        if card.rank == "Ace":
            self.aces += 1
    
    # Tracks Aces 
    def adjust_for_ace(self):
        # If total value > 21 and Aces are in hand,
        # then change Ace to be 1 instead of 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
    
    def new_hand(self):
        # resets to an empty list with no cards
        while len(self.cards) > 0:
            self.cards.pop()
        self.value = 0  # resets to zero value
        self.aces = 0   # resets to zero aces in hand

class Chips:
    def __init__(self, total = 100):
        self.total = total  # This can be set to either default of 100 or passed value
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            print(f"You have {chips.total} chips")
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Sorry please provide an integer")
        else:
            if chips.bet > chips.total:
                print(f"Sorry, you do not have enough chips! You have {chips.total} chips")
            else:
                break

def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    while True:
        x = input("Hit or Stand? Enter h or s: ")

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn")
            global playing
            playing = False
        else:
            print("Sorry, I did not understand that, please enter h or s only")
            continue
        break

def show_some(player, dealer):
    # Show only one of the dealer's cards
    print("\nDealer's Hand: ")
    print("First card hidden!")
    print(dealer.cards[1])

    # Show all (2 cards) of the player's hand/cards
    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(card)

def show_all(player, dealer):
    # Show all of the dealer's cards
    print("\nDealer's Hand: ",*dealer.cards,sep='\n')
    # Calculate and display value
    print(f"Value of dealer's hand is: {dealer.value}")

    # Show all of the player's cards
    print("\nPlayer's Hand: ",*player.cards,sep='\n')
    # Calculate and display value
    print(f"Value of player's hand is: {player.value}")

def player_busts(player, dealer, chips):
    print("PLAYER BUSTED!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("PLAYER WINS! DEALER BUSTED!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("DEALER WINS!")
    chips.lose_bet()

def push(player, dealer, chips):
    print("Dealer and player tie! PUSH")

# Shuffle the deck and deals two cards to each player
def deal_cards(deck, player,dealer):
    # Shuffle deck
    deck.shuffle()

    # Deals two cards to player
    player.add_card(deck.deal())
    player.add_card(deck.deal())

    # Deals two cards to dealer
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())

def round_finish(player, dealer, chips):
    # Dealer busts
    if dealer.value > 21:
        dealer_busts(player,dealer,chips)
    # Dealer's hands is greater than player's hand
    elif dealer.value > player.value:
        dealer_wins(player,dealer,chips)
    # Player's hands is greater than dealer's hand
    elif dealer.value < player.value:
        player_wins(player,dealer,chips)
    # Player and dealer tie, so no one wins or loses chips
    else:
        push(player,dealer,chips)

def player_turn(deck, player, dealer, chips):
    while playing:     
        # Prompt for player to hit or stands
        hit_or_stand(deck,player)

        # Show cards (but keep one dealer card hidden)
        show_some(player,dealer)

        # Check if player's hand exceeds 21
        if player_hand.value > 21:
            player_busts(player,dealer,chips)
            break

def dealer_turn(deck, player, dealer, chips):
    if player.value <= 21:
        # Show all cards
        show_all(player,dealer)

        # Dealer hits until 17 or higher
        while dealer.value < 17:
            print("\nDealer Hits!")
            hit(deck,dealer)
            show_all(player,dealer)

        # Run different winning scenarios based on hand values
        round_finish(player,dealer,chips)

def play_round(deck, player, dealer, chips):
    # Reset both player and dealer hands to before dealing new cards
    player.new_hand()
    dealer.new_hand()
    
    # Deal cards to player and dealer
    deal_cards(deck,player,dealer)
    
    # Prompt player for their bet
    take_bet(chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player,dealer)

    # Player's turn to hit or stand
    player_turn(deck,player,dealer,chips)

    # After player stands, it becomes the dealer's turn
    dealer_turn(deck,player,dealer,chips)

    # Inform player of their chips total
    print("\nPlayer total chips are at: {}".format(chips.total))

print("WELCOME TO BLACKJACK")
# Set up player's chips
deck = Deck()
player_chips = Chips()
player_hand = Hand()
dealer_hand = Hand()

while playing:
    # Begin Blackjack new round
    play_round(deck, player_hand, dealer_hand, player_chips)

    # Check if player still has chips
    # If not, then end the games
    if player_chips.total <= 0:
        print("Sorry, you're all out of chips")
        print("Thanks for playing!")
        break
    
    # If there are still chips, then ask to play again
    while True:
        new_game = input("Would you like to play another hand? (y/n) ")
        if new_game[0].lower() == 'y':
            playing = True
        elif new_game[0].lower() == 'n':
            playing = False
            print("Thanks for playing!")
        else:
            print("Sorry, I did not understand that, please enter y or n only")
            continue
        break