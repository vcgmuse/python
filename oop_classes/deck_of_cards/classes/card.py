class Card:
    def __init__( self , suit , point_val , string_val ):        
        self.suit = suit
        self.point_val = point_val
        self.string_val = string_val
    def show_info(self):
        print(f"{self.string_val} of {self.suit} : {self.point_val} points")
    def compare_card(self, card):
        valid_suit = self.suit == card.suit
        valid_value = self.point_val == card.point_val
        valid = valid_suit == True and valid_value == True
        return valid