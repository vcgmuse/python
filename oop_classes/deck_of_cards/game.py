from classes.deck import Deck

class Game:
    def __init__(self):
        self.player_playing = True
        self.deck = Deck()
        self.score = 0
        self.total_guess = 0
        self.card = None
        self.player_card = None
        self.previous_cards = []
    def display_pervious_cards(self):
        self.previous_cards.append(self.card)
        for card in self.previous_cards:
            card.show_info()
    def compare_card(self):
        if self.card == None:
            self.card = self.deck.draw_random_card()
        print(f"Dealer card: ")
        self.card.show_info()
        print(f"Player Card: ")
        self.player_card.show_info()
        valid = self.card.compare_card(self.player_card)
        if valid == True:
            self.increment_score()
        return valid

    def grab_card(self):
        self.card = self.deck.draw_random_card()

    def prompt_guess(self):
        print("Try your luck and guess the card: ")
        suits = int(self.prompt_suits())
        suits = self.deck.suits[suits-1]
        value = self.prompt_value()
        self.player_card = self.deck.create_card(suits, value)
        self.increment_guess_count()

    def prompt_value(self):
        valid = False
        while not valid:
            print("1:Ace 11:Jack 12:Queen 13:King")
            value_input = input("What value from 1 - 13?\n")
            valid = self.verify_value(value_input)

            if not valid:
                print("Please enter a valid response: ")
            else:
                if value_input in self.deck.face_cards:
                    print(self.deck.face_cards)
                    return self.deck.face_cards[value_input]
                return int(value_input)

    def verify_value(self, value):
        if value.isdigit():
            return int(value) in range(1, 14)
        else:
            return False

    def prompt_suits(self):
        valid = False
        suits = 0
        while not valid:
            suits = input("Which Suits?\n 1:Spades 2:Clubs 3:Hearts 4:Diamonds\n")
            valid = self.verify_suits(suits)
            if not valid:
                print("Please enter a valid response: ")
        return suits

    def verify_suits(self, suit):
        if suit.isdigit():
            return int(suit) in range(1, 5)
        else:
            return False

    def increment_score(self):
        self.score += 1

    def increment_guess_count(self):
        self.total_guess += 1
    def print_guess_rate(self):
        percentage = self.score / self.total_guess
        print(f"Correct Guess Rate: {percentage * 100}%\n")
        print("Cards Already Played: ")
        self.display_pervious_cards()

    def get_final_score(self):
        if self.total_guess == 0:
            print("No guesses made yet.")
        else:
            self.print_guess_rate()
            self.player_playing = False

