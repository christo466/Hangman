import random  
import sys     

def hang_man(error, word_list, temporary_list, chance, random_word, temporary_list_word):
    """
    Display the current hangman stage based on the number of errors and check if the player has won.

    Parameters:
    - error: Number of incorrect guesses
    - word_list: The list of characters in the target word
    - temporary_list: The list of guessed characters (with underscores for unguessed letters)
    - chance: The number of remaining chances
    - random_word: The word the player is trying to guess
    - temporary_list_word: The current guessed word as a string
    """
    
    hangman_stages = [
        r"""
           -----
           |   |
               |
               |
               |
               |
        ---------
        """,
        r"""
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        r"""
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        r"""
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        r"""
           -----
           |   |
           O   |
          /|\  |
               |
               |
        ---------
        """,
        r"""
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        ---------
        """,
        r"""
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        ---------
        """,
    ]

    
    if random_word == temporary_list_word:
        game_won(temporary_list_word)  
    elif random_word != temporary_list_word:
        print(hangman_stages[error])  
        
        print_the_gues(word_list, temporary_list, chance)

def game_won(temporary_list_word):
    """
    Handle the scenario when the player wins the game.

    Parameters:
    - temporary_list_word: The correctly guessed word
    """
    print("--------------------")
    print(f"The word: {temporary_list_word}")
    print("You have won the game")
    continue_playing()  

def lost_game(chance, word_list):
    """
    Handle the scenario when the player loses the game.

    Parameters:
    - chance: The number of remaining chances
    """
    original_word = "".join(word_list) 
    if chance <= 0:
        print(f"The word: {original_word}")
        print("You lost the game")
    print("Continue playing the game... yes or no")
    yes_or_no = input("> ")  
    if yes_or_no == "yes":
        Main()  
    else:
        sys.exit(0)  

def continue_playing():
    """
    Prompt the player to continue playing the game and handle their response.
    """
    print("Continue playing the game... yes or no")
    yes_or_no = input("> ").lower()  
    if yes_or_no == "yes":
        Main()  
    else:
        sys.exit() 

def check_chance(chance, word_list, temporary_list):
    """
    Check the remaining chances and proceed accordingly.

    Parameters:
    - chance: The number of remaining chances
    - word_list: The list of characters in the target word
    - temporary_list: The list of guessed characters (with underscores for unguessed letters)
    """
    print(f"Chances remaining: {chance}")
    if chance > 0:
        getting_word(word_list, temporary_list, chance)  
    else:
        lost_game(chance, word_list)  

def check_the_word(input_letter, word_list, temporary_list, chance):
    """
    Check if the guessed letter is in the word and update the state accordingly.

    Parameters:
    - input_letter: The letter guessed by the player
    - word_list: The list of characters in the target word
    - temporary_list: The list of guessed characters (with underscores for unguessed letters)
    - chance: The number of remaining chances

    Returns:
    - updated temporary_list, updated chance, random_word, updated temporary_list_word
    """
    length_of_word_list = len(word_list) 
    random_word = "".join(word_list)     
    temporary_list_word = "".join(temporary_list) 
    
   
    letter_found = False
    try:
        int_value = int(input_letter)
    except:
        pass
    
    if chance > 0:
          
        for i in range(length_of_word_list):
            if input_letter == word_list[i]:
                temporary_list[i] = input_letter 
                letter_found = True
        
        
        temporary_list_word = "".join(temporary_list)
        
        if letter_found:
            
            if random_word == temporary_list_word:
                game_won(random_word)  
        elif input_letter.isdigit():
            print("enter proper input")
         
        else:
               
               chance -= 1

    return temporary_list, chance, random_word, temporary_list_word


def getting_word(word_list, temporary_list, chance):
    """
    Prompt the user to guess a letter and proceed with the game.

    Parameters:
    - word_list: The list of characters in the target word
    - temporary_list: The list of guessed characters (with underscores for unguessed letters)
    - chance: The number of remaining chances
    """
    input_letter = input("Enter the letter: ")  
    lower_letter = input_letter.lower()  
    temporary_list, chance, random_word, temporary_list_word = check_the_word(lower_letter, word_list, temporary_list, chance)
    hang_man(6 - chance, word_list, temporary_list, chance, random_word, temporary_list_word)  

def gues_the_word(word):
    """
    Initialize the game state for a new word and start the game.

    Parameters:
    - word: The word the player is trying to guess
    """
    length_of_word = len(word)
    chance = 6  
    word_list = list(word.lower()) 
    temporary_list = ["_"] * length_of_word  
    temporary_list_word = "".join(temporary_list)  
    hang_man(6 - chance, word_list, temporary_list, chance, word, temporary_list_word)  
    getting_word(word_list, temporary_list, chance)  

def print_the_gues(word_list, temporary_list, chance):
    """
    Display the current guessed state of the word and proceed with the game.

    Parameters:
    - word_list: The list of characters in the target word
    - temporary_list: The list of guessed characters (with underscores for unguessed letters)
    - chance: The number of remaining chances
    """
    print(f"Guess the word: {' '.join(temporary_list)}") 
    check_chance(chance, word_list, temporary_list)  

def Random_word(words_list):
    """
    Select a random word from the list based on the chosen difficulty level.

    Parameters:
    - words_list: The list of words to choose from
    """
    level = input("> Choose the level: Easy = 1,  Medium = 2, Hard = 3: ")  
    if level in ["1", "2", "3"]:
        if level == "1":
            length_of_word = random.randint(1, 4)   
        elif level == "2":
            length_of_word = random.randint(5, 8)  
        elif level == "3":
            length_of_word = random.randint(9, 14)  

        filtered_words = [word for word in words_list if len(word) == length_of_word] 
        random_word = random.choice(filtered_words) 
        print(random_word) 
        gues_the_word(random_word)  
    else:
        print("Give proper input")  
        Random_word(words_list) 

def remove_char_after_single_quote(words):
    """
    Remove characters following a single quote in the word list.

    Parameters:
    - words: The list of words to be cleaned
    """
    modified_words = []
    for word in words:
        if "'" in word:
            parts = word.split("'")
            modified_word = parts[0]  
            modified_words.append(modified_word)
        else:
            modified_words.append(word)
    Random_word(modified_words)  

def Main():
    """
    Main function to start the Hangman game. Reads words from a file and initializes the game.
    """
    file_path = "dictionary.txt"  
    try:
        with open(file_path, 'r') as open_file:  
            read_file = open_file.read()  
            words_list = read_file.split()  
        remove_char_after_single_quote(words_list)  
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    Main()  
