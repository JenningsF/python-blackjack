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
        if card.rank = "Ace":
            self.aces += 1
    
    # Tracks Aces 
    def adjust_for_ace(self):
        # If total value > 21 and Aces are in hand,
        # then change Ace to be 1 instead of 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self, total = 100):
        self.total = total  # This can be set to either default of 100 or passed value
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

test_deck = Deck()
test_deck.shuffle()
test_player = Hand()
pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
test_player.add_card(test_deck.deal())
print(test_player.value)