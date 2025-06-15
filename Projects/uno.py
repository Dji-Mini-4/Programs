import random
import os
import time

# Constants
COLORS = ['Red', 'Yellow', 'Green', 'Blue']
VALUES = [str(n) for n in range(0, 10)] + ['Skip', 'Reverse', 'Draw Two']
SPECIAL_CARDS = ['Wild', 'Wild Draw Four']

# Helper functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nPress Enter to continue...")

def generate_deck():
    deck = []
    for color in COLORS:
        for value in VALUES:
            deck.extend([(color, value)] * (2 if value != '0' else 1))
    for special in SPECIAL_CARDS:
        deck.extend([(None, special)] * 4)
    random.shuffle(deck)
    return deck

def format_card_value(color, value):
    if value == 'Draw Two':
        return f"{color} +2"
    elif value == 'Wild Draw Four':
        return "Wild d4"
    return value

def display_card(card):
    color, value = card
    display_color = color if color else "Wild"
    display_value = format_card_value(display_color, value)
    lines = [
        " _________ ",
        f"|         |",
        f"|{display_color:<9}|",
        f"|  {display_value:^7}|",
        f"|{display_color:>9}|",
        f"|_________|"
    ]
    return '\n'.join(lines)

def display_hand(hand):
    # Display each card vertically with index label above
    indexes = [f"   {i:^9}   " for i in range(len(hand))]
    cards = [display_card(card).split('\n') for card in hand]
    lines = [' '.join(part[i] for part in cards) for i in range(6)]
    return '\n'.join(indexes) + '\n' + '\n'.join(lines)

def is_playable(card, top_card):
    return (
        card[0] == top_card[0] or
        card[1] == top_card[1] or
        card[1] in SPECIAL_CARDS
    )

def ai_choose_card(hand, top_card):
    for card in hand:
        if is_playable(card, top_card):
            return card
    return None

# Game logic
class UNOGame:
    def __init__(self, player_count=3):
        self.deck = generate_deck()
        self.hands = {f"Player {i}": [self.deck.pop() for _ in range(7)] for i in range(player_count)}
        self.players = list(self.hands.keys())
        self.current_index = 0
        self.direction = 1
        self.pile = [self.deck.pop()]

    def draw_card(self, player):
        if not self.deck:
            self.reshuffle_discard()
        self.hands[player].append(self.deck.pop())

    def reshuffle_discard(self):
        top = self.pile.pop()
        self.deck = self.pile
        random.shuffle(self.deck)
        self.pile = [top]

    def play_turn(self):
        player = self.players[self.current_index]
        top_card = self.pile[-1]

        print(f"\nTop card:\n{display_card(top_card)}")
        print(f"\n{player}'s turn")

        if player == "Player 0":  # human
            print(f"\nYour hand:\n{display_hand(self.hands[player])}")
            valid_moves = [i for i, card in enumerate(self.hands[player]) if is_playable(card, top_card)]

            if not valid_moves:
                print("\nNo valid moves. Drawing a card...")
                self.draw_card(player)
            else:
                while True:
                    try:
                        choice = int(input("Choose a card to play: "))
                        if choice in valid_moves:
                            card = self.hands[player].pop(choice)
                            self.pile.append(card)
                            self.apply_card_effect(card)
                            break
                        else:
                            print("Invalid choice. Try again.")
                    except ValueError:
                        print("Invalid input. Enter a number.")
        else:
            time.sleep(1)
            card = ai_choose_card(self.hands[player], top_card)
            if card:
                self.hands[player].remove(card)
                self.pile.append(card)
                print(f"{player} played:\n{display_card(card)}")
                self.apply_card_effect(card)
            else:
                self.draw_card(player)
                print(f"{player} drew a card.")

        if len(self.hands[player]) == 0:
            print(f"\n{player} wins!")
            return True

        self.current_index = (self.current_index + self.direction) % len(self.players)
        pause()
        return False

    def apply_card_effect(self, card):
        _, value = card
        if value == 'Skip':
            self.current_index = (self.current_index + self.direction) % len(self.players)
        elif value == 'Reverse':
            self.direction *= -1
        elif value == 'Draw Two':
            target = (self.current_index + self.direction) % len(self.players)
            for _ in range(2):
                self.draw_card(self.players[target])
        elif value == 'Wild Draw Four':
            target = (self.current_index + self.direction) % len(self.players)
            for _ in range(4):
                self.draw_card(self.players[target])

# Start game
def main():
    game = UNOGame()
    while True:
        clear_screen()
        if game.play_turn():
            break

if __name__ == '__main__':
    main()
