import random

class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self):
        self.__cards = []
        self.create_deck()

    def create_deck(self):
        for i in self.SUITS:
            for j in self.RANKS:
                self.__cards.append((j, i))
                

    def shuffle_deck(self):
        random.shuffle(self.__cards)

    def deal_card(self):
        if self.__cards:
            return self.__cards.pop()
        else:
            return None