from game import Game
class Guess(Game):
    def __init__(self):
        super().__init__()
test_game = Guess()
while test_game.player_playing == True:    
    test_game.grab_card()
    test_game.prompt_guess()
    print(f"Your guess was: {test_game.compare_card()}")
    test_game.print_guess_rate()
    print("\n")
test_game.get_final_score()