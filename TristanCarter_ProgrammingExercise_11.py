import random
#Tristan Carter
#This program will deal 5 cards and prompt the user to keep or replace them

class Deck():
    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        random.shuffle(self.card_list)
        self.current_card = 0
        self.size = size

    def deal(self):
        if self.size - self.current_card < 1:
            random.shuffle(self.card_list)
            self.current_card = 0
            print('Reshuffling...!!!')
        self.current_card += 1
        return self.card_list[self.current_card - 1]


ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['clubs', 'diamonds', 'hearts', 'spades']

#Convert card index to rank and suit
def get_card_name(card_index):
    r = card_index % 13
    s = card_index // 13
    return f"{ranks[r]} of {suits[s]}"

#Deals cards
def deal_hand(deck, num_cards=5):
    hand = []
    for _ in range(num_cards):
        hand.append(deck.deal())
    return hand

#Display user cards and prompt them to replace or keep their cards
def main():
    my_deck = Deck(52)

    print("Your hand:")
    hand = deal_hand(my_deck)
    for i, card in enumerate(hand):
        print(f"{i + 1}: {get_card_name(card)}")

    while True:
        try:
            replace_input = input("Enter card numbers to replace (1, 3, 5), or 'keep' to keep your hand: ")
            if replace_input.lower() == 'keep':
                break

            replace_indices = [int(x.strip()) - 1 for x in replace_input.split(',')]

            for index in replace_indices:
                if 0 <= index < len(hand):
                    hand[index] = my_deck.deal()
                else:
                    print(f"Invalid number: {index + 1}.")
            break
        except ValueError:
            print("Error. Please enter numbers separated by commas or 'keep'.")

    print("\nCurrent hand:")
    for i, card in enumerate(hand):
        print(f"{i + 1}: {get_card_name(card)}")


if __name__ == "__main__":
    main()