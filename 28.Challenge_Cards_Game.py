"""
This challenge is to make a simple card game where two players draw cards from a standard 52 card deck, and the player with the highest score wins. The score is calculated based on the cards' values with number cards (2-10) 
worth their face value, face cards (Jack, Queen, King) worth 10, and Aces worth 11. 
Requirements:
    - Create a Card class to create card objects with a suit (heart, spade, 
    club, diamond) and rank (2-10, Jack, Queen, King, Ace)
    - Create a Deck class that holds, shuffles, and deals the cards
    - Output each player's hand and its score
    - Output the winner
The rest of the implementation, which includes things like how many cards are drawn and how to handle players/hands, is entirely up to user! The main goals are to create the two required classes, two players are dealt cards from a deck, the players' hands are output with their scores, and the player with the highest scoring hand is declared.
HINT: Read about the methods available in the `random` module to find one that 
will help you with your deck.
"""

## Import the `random` module to shuffle the deck
import random


## Define the Card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        if rank in ["J", "Q", "K"]:
            self.value = 10
        elif rank == "A":
            self.value = 11
        else:
            self.value = int(rank)

    def __str__(self):
        return f"{self.rank}{self.suit}"


"""
The Card class is designed to represent individual playing cards, and it has a constructor `__init__` method and a string representation method `__str__`.
In the constructor method `__init__`, the class initializes the attributes of each card object. These attributes include suit (♥, ♦, ♣, ♠), rank (2-10, Jack, Queen, King, Ace), and the value of the card based on its rank. If the rank is a face card (J, Q, K), the value is set to 10. If the rank is an Ace (A), the value is set to 11. For numerical ranks, the value is directly set to the integer value of the rank.
The `__str__` method provides a string representation of the card. It combines the rank and suit attributes to form a string that represents the card, like "2♥" for the 2 of Hearts, "J♦" for the Jack of Diamonds.
"""


## Define the Deck class
class Deck:
    def __init__(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["♥", "♦", "♣", "♠"]
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


"""
The Deck class is designed to represent a deck of playing cards. It has the `__init__`, `shuffle`, and `deal_card` methods. 
In the constructor `__init__` method, `ranks` and `suits` lists are defined to hold the ranks and suits of playing cards. `self.cards` is an instance variable list that will hold the cards in the deck. Nested loops iterate over each suit and rank to create all possible combinations of cards. Each combination is used 
to create a new Card object using the Card class, and this card is added to the `self.cards` list. This way, it populates the deck with 52 playing cards.
The `shuffle` method uses the `random` module's `shuffle` method to shuffle the list of cards that make up the deck in place.
The `deal_card` method pops the last card from the cards list, removing it from the deck and returning it to the caller.
"""


## Define the Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, deck):
        self.hand.append(deck.deal_card())

    def get_hand(self):
        cards = [str(card) for card in self.hand]
        hand = " | ".join(cards)
        return hand

    def calculate_score(self):
        score = 0
        for card in self.hand:
            score += card.value
        return score


"""
The Player class is designed to represent a player. It has the `__init__`, `draw_card`, `get_hand`, and `calculate_score` methods.
In the `__init__` method, `self.name` is an instance variable to hold the player's name, and `self.hand` is an instance variable to hold the player's list of cards.
The `draw_card` method takes a deck as an argument and appends the player's hand with the card that is returned by the deck's `deal_card` method.
The `get_hand` method uses list comprehension to create a list of card string representations from the player's hand. Then, a string is formatted using the pipe character '|' to separate each card and stored in the `hand` variable. 
Finally, the `hand` variable is returned to the caller.
The `calculate_score` method uses a for loop to add all the values of the cards in the player's hand to the `score` variable and returns the score to the caller.
"""


def play_game():
    ## Shuffle the deck
    deck = Deck()
    deck.shuffle()

    ## players1, player2
    player1 = Player("Saadi")
    player2 = Player("Ane")

    ## Both Players draw 5 cards
    for i in range(5):
        player1.draw_card(deck)
        player2.draw_card(deck)

    ## Calculate and display scores
    score1 = player1.calculate_score()
    score2 = player2.calculate_score()

    ## Show players' hands
    print(f"{player1.name}'s hand:", player1.get_hand())
    print("Score:", score1)

    print(f"\n{player2.name}'s hand:", player2.get_hand())
    print("Score:", score2)

    ## Call out winner
    if score1 > score2:
        print("\nPlayer 1 wins!")
    elif score2 > score1:
        print("\nPlayer 2 wins!")
    else:
        print("\nIt's a tie!")


"""
The `play_game` function handles the game logic by creating the deck and player objects, calling the appropriate methods to deal cards and calculate the players' scores, and determining the winner.
"""
# Game start
play_game()
