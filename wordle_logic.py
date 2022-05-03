from allowed_guesses import ALLOWED_GUESS_SET
ALLOWED_GUESSES_COUNT = 10657

def validate_guess(guess):
    if len(guess) == 5 and guess.isalpha():
        guess = guess.lower()
        if guess in ALLOWED_GUESS_SET:
            return guess
    else:
        return False

def build_target_dict(target):
    target_dict = {}
    for letter in target:
        if letter in target_dict:
            target_dict[letter] += 1
        else:
            target_dict[letter] = 1
    return target_dict

def check_guess(target, guess):
    target_dict = build_target_dict(target)

    check_result = ["r"] * 5
    for index, letter in enumerate(guess):
        if letter == target[index]:
            check_result[index] = "g"
            target_dict[letter] -= 1
    
    for index, letter in enumerate(guess):
        if check_result[index] == "g":
            continue
        elif letter in target_dict and target_dict[letter] > 0:
            check_result[index] = "y"
            target_dict[letter] -= 1

    return check_result

def get_user_guess():
    user_guess = None
    while not user_guess:
        print("Guess a 5-letter word.")
        user_input = input("Guess: ")
        user_guess = validate_guess(user_input)
    return user_guess

def update_keyboard(keyboard_dict, guess, guess_response):
    for i in range(len(guess)):
        if keyboard_dict[guess[i]] == "grey":
            keyboard_dict[guess[i]] = guess_response[i]
        elif guess_response[i] == 'g':
            if keyboard_dict[guess[i]] == "y" or keyboard_dict[guess[i]] == "r":
                keyboard_dict[guess[i]] = guess_response[i]
    return None






# print(check_guess("words", "sword"))
# print(check_guess("words", "twirl"))
# print(check_guess("words","hells"))
# print(check_guess("words", "words"))
# print(check_guess("words", "alamo"))

#print(get_target_word())