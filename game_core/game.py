from wordle_logic import *
from magic_variables import *
from answers import ANSWERS
from copy import deepcopy
import random



def make_player_list():
    return random.sample(ANSWERS, ANSWERS_COUNT)

def word_transition(guessed_word, new_word):
    transition_tiles = check_guess(new_word, guessed_word)
    game_keyboard = deepcopy(KEYBOARD)
    update_keyboard(game_keyboard, guessed_word, transition_tiles)
    print(f"{guessed_word} gives you {transition_tiles}")
    return game_keyboard


def game():
    game_words = make_player_list()
    #game_words = ["hello", "smile", "acorn", "twist"]
    guesses_left = GUESSES_ALLOWED
    words_solved = 0
    print("Welcome to Wordle: the last stand")

    i = 0
    game_keyboard = deepcopy(KEYBOARD)

    while guesses_left and i < ANSWERS_COUNT:
        current_word = game_words[i]
        user_guess = get_user_guess()
        guesses_left -= 1
        guess_response = check_guess(current_word, user_guess)
        print(f"{user_guess}: {guess_response}")
        
        update_keyboard(game_keyboard, user_guess, guess_response)

        if guess_response == ["g"] * 5:
            print("Word Guessed!")
            words_solved += 1
            if guesses_left:
                game_keyboard = word_transition(game_words[i], game_words[i+1])
                i += 1

        print(f"Guesses remaining: {guesses_left}")
        print(f"Keyboard: {game_keyboard}")
    print(f"Out of guesses! You solved {words_solved} words.")
    return None

game()