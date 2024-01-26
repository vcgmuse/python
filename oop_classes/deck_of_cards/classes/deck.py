from .card import Card
from random import randint

class Deck:
    def __init__( self ):
        self.suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.face_cards = {1:"Ace", 11:"Jack", 12:"Queen", 13: "King"}
        self.cards = []
        self.create_deck()
    def create_deck(self):
        for s in self.suits:
            for i in range(1,14):
                card = self.create_card(s, i)
                self.cards.append(card)
    def create_card(self, suit, integer):        
        str_val = ""
        if integer == 1:
            str_val = "Ace"
        elif integer == 11:
            str_val = "Jack"
        elif integer == 12:
            str_val = "Queen"
        elif integer == 13:
            str_val = "King"
        else:
            str_val = str(integer)
        return Card(suit, integer, str_val)
    def show_cards(self):
        for card in self.cards:
            card.card_info()
    def display_card(self, card):
        card.show_info()
    def draw_random_card(self):
        cards_left = len(self.cards)
        if(cards_left > 0):
            random_card_index = randint(0, len(self.cards))
            print(len(self.cards))
            card = self.cards[random_card_index-1]
            self.display_card(card)
            self.cards.remove(card)
            return card
        else:
            print("Reseting card deck, ran out of cards: ")
            self.reset_cards()
            self.draw_random_card()
    def reset_cards(self):
        self.cards.clear()
        self.create_deck()
        