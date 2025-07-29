from card import Card

def main():
    print("Welcome to Blackjack! \n")

    card = Card("Ace", "Spade")
    print(card.display_card())


if __name__ == '__main__':
    main()