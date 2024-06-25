import unittest
from Hangman import check_the_word, hang_man, getting_word, gues_the_word, check_chance, print_the_gues, remove_char_after_single_quote,  Main, Random_word, lost_game, continue_playing, game_won
from unittest.mock import patch, MagicMock, mock_open, call
import builtins
import sys

class TestHangMan(unittest.TestCase):

    @patch('builtins.print')
    @patch('Hangman.game_won')
    @patch('Hangman.print_the_gues')
    def test_hangman_game_won(self, mock_print_the_gues, mock_game_won, mock_print):
       
        hang_man(0, ['h', 'a', 'n', 'g', 'm', 'a', 'n'], ['h', 'a', 'n', 'g', 'm', 'a', 'n'], 3, "hangman", "hangman")
        
       
        mock_game_won.assert_called_once_with("hangman")
        
       
        mock_print.assert_not_called()
        
        
        mock_print_the_gues.assert_not_called()
    @patch('builtins.print')
    @patch('Hangman.game_won')
    @patch('Hangman.print_the_gues')
    def test_hangman_incorrect_guess(self, mock_print_the_gues, mock_game_won, mock_print):
       
        hang_man(3, ['h', 'a', 'n', 'g', 'm', 'a', 'n'], ['h', '_', 'n', '_', 'm', '_', 'n'], 3, "hangman", "h_n_m_n")
        
       
        mock_print.assert_any_call(
            """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """
        )
        
       
        mock_game_won.assert_not_called()
        
       
        mock_print_the_gues.assert_called_once_with(['h', 'a', 'n', 'g', 'm', 'a', 'n'], ['h', '_', 'n', '_', 'm', '_', 'n'], 3)
    
    @patch('builtins.print')
    @patch('Hangman.game_won')
    @patch('Hangman.print_the_gues')
    def test_hangman_no_errors(self, mock_print_the_gues, mock_game_won, mock_print):
       
        hang_man(0, ['h', 'a', 'n', 'g', 'm', 'a', 'n'], ['h', 'a', 'n', 'g', 'm', 'a', 'n'], 6, "hangman", "h_ngm_n")
        
        
        mock_print.assert_any_call(
            """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """
        )
        
       
        mock_game_won.assert_not_called()
        
        
        mock_print_the_gues.assert_called_once_with(['h', 'a', 'n', 'g', 'm', 'a', 'n'], ['h', 'a', 'n', 'g', 'm', 'a', 'n'], 6)
    
    @patch('builtins.print')
    @patch('Hangman.game_won')
    @patch('Hangman.print_the_gues')
    def test_hangman_max_errors(self, mock_print_the_gues, mock_game_won, mock_print):
        
        hang_man(6, ['h', 'a', 'n', 'g', 'm', 'a', 'n'], ['_', '_', '_', '_', '_', '_', '_'], 0, "hangman", "_ _ _ _ _ _ _")
        
        
        mock_print.assert_any_call(
            """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """
        )
        
       
        mock_game_won.assert_not_called()
        
        
        mock_print_the_gues.assert_called_once_with(['h', 'a', 'n', 'g', 'm', 'a', 'n'], ['_', '_', '_', '_', '_', '_', '_'], 0)



class TestGameWon(unittest.TestCase):

    @patch('builtins.print')
    @patch('Hangman.continue_playing')
    def test_game_won(self, mocked_continue_playing, mock_print):
        
        game_won("victory")

        
        mock_print.assert_any_call("--------------------")
        mock_print.assert_any_call("The word: victory")
        mock_print.assert_any_call("You have won the game")

        
        mocked_continue_playing.assert_called_once()
    
    @patch('builtins.print')
    @patch('Hangman.continue_playing')
    def test_game_won_with_different_word(self, mock_continue_playing, mock_print):
        
        game_won("champion")

        
        mock_print.assert_any_call("--------------------")
        mock_print.assert_any_call("The word: champion")
        mock_print.assert_any_call("You have won the game")

        
        mock_continue_playing.assert_called_once()


class TestLostGame(unittest.TestCase):

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['no'])
    @patch('sys.exit')
    def test_lost_game_loss(self, mock_exit, mock_input, mock_print):
        lost_game(0, ['h', 'e', 'l', 'l', 'o'])
        
       
        mock_print.assert_any_call("The word: hello")
        mock_print.assert_any_call("You lost the game")
        
        
        mock_print.assert_any_call("Continue playing the game... yes or no")
        
       
        mock_exit.assert_called_once_with(0)
    
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['yes'])
    @patch('sys.exit')
    @patch('Hangman.Main')
    def test_lost_game_continue(self, mocked_Main, mock_exit, mock_input, mock_print):
        with patch('Hangman.Main') as mock_main:
            lost_game(0, ['w', 'o', 'r', 'l', 'd'])
            
            
            mock_print.assert_any_call("The word: world")
            mock_print.assert_any_call("You lost the game")
            
            
            mock_print.assert_any_call("Continue playing the game... yes or no")
            
            
            mock_exit.assert_not_called()
            
            
            mock_main.assert_called_once()


class TestContinuePlaying(unittest.TestCase):
    
    @patch('builtins.print')
    @patch('builtins.input', return_value='yes')
    @patch('Hangman.Main')
    def test_continue_playing_yes(self, mocked_Main, mocked_input, mocked_print):
        continue_playing()
        mocked_print.assert_called_once_with("Continue playing the game... yes or no")
        mocked_Main.assert_called_once()

    @patch('builtins.print')
    @patch('builtins.input', return_value='no')
    @patch('sys.exit')
    def test_continue_playing_no(self, mocked_exit, mocked_input, mocked_print):
        continue_playing()
        mocked_print.assert_called_once_with("Continue playing the game... yes or no")
        mocked_exit.assert_called_once()

class TestCheckChance(unittest.TestCase):
    
    @patch('builtins.print')
    @patch('Hangman.getting_word')
    def test_chance_greater_than_zero(self, mocked_getting_word, mocked_print):
        word_list = ['c', 'a', 't']
        temporary_list = ['_', '_', '_']
        
        check_chance(2, word_list, temporary_list)
        
        mocked_print.assert_called_once_with("Chances remaining: 2")
        mocked_getting_word.assert_called_once_with(word_list, temporary_list, 2)
    
    @patch('builtins.print')
    @patch('Hangman.lost_game')
    def test_chance_zero(self, mocked_lost_game, mocked_print):
        word_list = ['c', 'a', 't']
        temporary_list = ['_', '_', '_']
        
        check_chance(0, word_list, temporary_list)
        
        mocked_print.assert_called_once_with("Chances remaining: 0")
        mocked_lost_game.assert_called_once_with(0, word_list)
    
    
class TestCheckTheWord(unittest.TestCase):
    def test_correct_guess(self):
        input_letter = 'a'
        word_list = ['h', 'a', 'n', 'g', 'm', 'a', 'n']
        temporary_list = ['h', '_', '_', '_', '_', '_', '_']
        chance = 5

        
        expected_temporary_list = ['h', 'a', '_', '_', '_', 'a', '_']  
        expected_chance = 5 
        expected_temporary_list_word = 'ha___a_'

        updated_temporary_list, updated_chance, _, updated_temporary_list_word= check_the_word(
            input_letter, word_list, temporary_list, chance
        )

        self.assertEqual(updated_temporary_list, expected_temporary_list, "The temporary list did not update correctly.")
        self.assertEqual(updated_chance, expected_chance, "The chance should not decrease for a correct guess.")
        self.assertEqual(updated_temporary_list_word, expected_temporary_list_word, "The temporary word view is incorrect.")

    def test_incorrect_guess(self):
        input_letter = 'z'
        word_list = ['h', 'a', 'n', 'g', 'm', 'a', 'n']
        temporary_list = ['h', '_', '_', '_', '_', '_', '_']
        chance = 5

        
        expected_temporary_list = ['h', '_', '_', '_', '_', '_', '_']  
        expected_chance = 4  
        expected_temporary_list_word = 'h______'

        updated_temporary_list, updated_chance, _, updated_temporary_list_word,  = check_the_word(
            input_letter, word_list, temporary_list, chance
        )

        self.assertEqual(updated_temporary_list, expected_temporary_list, "The temporary list should remain unchanged.")
        self.assertEqual(updated_chance, expected_chance, "The chance should decrease for an incorrect guess.")
        self.assertEqual(updated_temporary_list_word, expected_temporary_list_word, "The temporary word view is incorrect.")
        
        
    def test_already_guessed_letter(self):
        input_letter = 'a'
        word_list = ['h', 'a', 'n', 'g', 'm', 'a', 'n']
        temporary_list = ['h', 'a', '_', '_', '_', 'a', '_']
        chance = 5

        expected_temporary_list = ['h', 'a', '_', '_', '_', 'a', '_']  
        expected_chance = 5  

        updated_temporary_list, updated_chance, _, _= check_the_word(
        input_letter, word_list, temporary_list, chance
    )

        self.assertEqual(updated_temporary_list, expected_temporary_list, "The temporary list should remain unchanged.")
        self.assertEqual(updated_chance, expected_chance, "The chance should not decrease after the letter was already fully guessed.")


    def test_partial_correct_guess(self):
        input_letter = 'g'
        word_list = ['h', 'a', 'n', 'g', 'm', 'a', 'n']
        temporary_list = ['h', 'a', '_', '_', '_', 'a', '_']
        chance = 4

        
        expected_temporary_list = ['h', 'a', '_', 'g', '_', 'a', '_'] 
        expected_chance = 4  
        expected_temporary_list_word = 'ha_g_a_'

        updated_temporary_list, updated_chance, _, updated_temporary_list_word = check_the_word(
            input_letter, word_list, temporary_list, chance
        )
        self.assertEqual(updated_temporary_list, expected_temporary_list, "The temporary list did not update correctly.")
        self.assertEqual(updated_chance, expected_chance, "The chance should not decrease for a correct guess.")
        self.assertEqual(updated_temporary_list_word, expected_temporary_list_word, "The temporary word view is incorrect.")
    
class TestGettingWord(unittest.TestCase):

    @patch('Hangman.input', return_value='a')
    @patch('Hangman.check_the_word')
    @patch('Hangman.hang_man')
    def test_correct_guess_flow(self, mock_hang_man, mock_check_the_word, mock_input):
        word_list = ['h', 'a', 'n', 'g', 'm', 'a', 'n']
        temporary_list = ['h', '_', '_', '_', '_', '_', '_']
        chance = 5

       
        mock_check_the_word.return_value = (['h', 'a', '_', '_', '_', '_', '_'], 5, 'hangman', 'ha_____')

       
        getting_word(word_list, temporary_list, chance)

        
        mock_input.assert_called_once()

        
        mock_check_the_word.assert_called_once_with('a', word_list, temporary_list, chance)

       
        mock_hang_man.assert_called_once_with(1, word_list, ['h', 'a', '_', '_', '_', '_', '_'], 5, 'hangman', 'ha_____')

    @patch('Hangman.input', return_value='z')
    @patch('Hangman.check_the_word')
    @patch('Hangman.hang_man')
    def test_incorrect_guess_flow(self, mock_hang_man, mock_check_the_word, mock_input):
        word_list = ['h', 'a', 'n', 'g', 'm', 'a', 'n']
        temporary_list = ['h', '_', '_', '_', '_', '_', '_']
        chance = 5

        
        mock_check_the_word.return_value = (['h', '_', '_', '_', '_', '_', '_'], 4, 'hangman', 'h______')

      
        getting_word(word_list, temporary_list, chance)

        
        mock_input.assert_called_once()

        
        mock_check_the_word.assert_called_once_with('z', word_list, temporary_list, chance)

        
        mock_hang_man.assert_called_once_with(2, word_list, ['h', '_', '_', '_', '_', '_', '_'], 4, 'hangman', 'h______')

    @patch('Hangman.input', return_value='n')
    @patch('Hangman.check_the_word')
    @patch('Hangman.hang_man')
    def test_partial_correct_guess_flow(self, mock_hang_man, mock_check_the_word, mock_input):
        word_list = ['h', 'a', 'n', 'g', 'm', 'a', 'n']
        temporary_list = ['h', 'a', '_', '_', '_', 'a', '_']
        chance = 4

        
        mock_check_the_word.return_value = (['h', 'a', 'n', '_', '_', 'a', 'n'], 4, 'hangman', 'han__an')

        
        getting_word(word_list, temporary_list, chance)

        
        mock_input.assert_called_once()

        
        mock_check_the_word.assert_called_once_with('n', word_list, temporary_list, chance)

       
        mock_hang_man.assert_called_once_with(2, word_list, ['h', 'a', 'n', '_', '_', 'a', 'n'], 4, 'hangman', 'han__an')

    @patch('Hangman.input', return_value='g')
    @patch('Hangman.check_the_word')
    @patch('Hangman.hang_man')
    def test_full_word_guess_flow(self, mock_hang_man, mock_check_the_word, mock_input):
        word_list = ['h', 'a', 'n', 'g', 'm', 'a', 'n']
        temporary_list = ['h', 'a', '_', '_', '_', 'a', '_']
        chance = 3

        
        mock_check_the_word.return_value = (['h', 'a', '_', 'g', '_', 'a', '_'], 3, 'hangman', 'ha_g_a_')

       
        getting_word(word_list, temporary_list, chance)

        
        mock_input.assert_called_once()

        
        mock_check_the_word.assert_called_once_with('g', word_list, temporary_list, chance)

        
        mock_hang_man.assert_called_once_with(3, word_list, ['h', 'a', '_', 'g', '_', 'a', '_'], 3, 'hangman', 'ha_g_a_')

class TestGuesTheWord(unittest.TestCase):
    
    @patch('Hangman.hang_man')
    @patch('Hangman.getting_word')
    def test_initialization_short_word(self, mock_getting_word, mock_hang_man):
        word = "cat"
        
        gues_the_word(word)
        
        expected_word_list = list(word.lower())
        expected_temporary_list = ["_"] * len(word)
        expected_chance = 6
        
        mock_hang_man.assert_called_once_with(
            6 - expected_chance, 
            expected_word_list, 
            expected_temporary_list, 
            expected_chance, 
            word, 
            "".join(expected_temporary_list)
        )
        
        mock_getting_word.assert_called_once_with(
            expected_word_list, 
            expected_temporary_list, 
            expected_chance
        )
    
    @patch('Hangman.hang_man')
    @patch('Hangman.getting_word')
    def test_initialization_long_word(self, mock_getting_word, mock_hang_man):
        word = "hangman"
        
        gues_the_word(word)
        
        expected_word_list = list(word.lower())
        expected_temporary_list = ["_"] * len(word)
        expected_chance = 6
        
        mock_hang_man.assert_called_once_with(
            6 - expected_chance, 
            expected_word_list, 
            expected_temporary_list, 
            expected_chance, 
            word, 
            "".join(expected_temporary_list)
        )
        
        mock_getting_word.assert_called_once_with(
            expected_word_list, 
            expected_temporary_list, 
            expected_chance
        )
    
    @patch('Hangman.hang_man')
    @patch('Hangman.getting_word')
    def test_initialization_mixed_case(self, mock_getting_word, mock_hang_man):
        word = "CaT"
        
        gues_the_word(word)
        
        expected_word_list = list(word.lower())
        expected_temporary_list = ["_"] * len(word)
        expected_chance = 6
        
        mock_hang_man.assert_called_once_with(
            6 - expected_chance, 
            expected_word_list, 
            expected_temporary_list, 
            expected_chance, 
            word, 
            "".join(expected_temporary_list)
        )
        
        mock_getting_word.assert_called_once_with(
            expected_word_list, 
            expected_temporary_list, 
            expected_chance
        )

class TestPrintTheGues(unittest.TestCase):
    @patch('builtins.print')
    @patch('Hangman.check_chance')
    def test_print_the_gues(self, mock_check_chance, mock_print):
        word_list = ['h', 'a', 'n', 'g', 'm', 'a', 'n']
        temporary_list = ['h', '_', '_', '_', '_', 'a', '_']
        chance = 4

        print_the_gues(word_list, temporary_list, chance)

        
        mock_print.assert_called_once_with(f"Guess the word: {' '.join(temporary_list)}")

       
        mock_check_chance.assert_called_once_with(chance, word_list, temporary_list)

    @patch('builtins.print')
    @patch('Hangman.check_chance')
    def test_print_the_gues_no_chances_left(self, mock_check_chance, mock_print):
        word_list = ['p', 'y', 't', 'h', 'o', 'n']
        temporary_list = ['p', 'y', '_', 'h', '_', 'n']
        chance = 0

        print_the_gues(word_list, temporary_list, chance)

        
        mock_print.assert_called_once_with(f"Guess the word: {' '.join(temporary_list)}")

        
        mock_check_chance.assert_called_once_with(chance, word_list, temporary_list)

    @patch('builtins.print')
    @patch('Hangman.check_chance')
    def test_print_the_gues_all_letters_guessed(self, mock_check_chance, mock_print):
        word_list = ['w', 'o', 'r', 'd']
        temporary_list = ['w', 'o', 'r', 'd']
        chance = 2

        print_the_gues(word_list, temporary_list, chance)

        
        mock_print.assert_called_once_with(f"Guess the word: {' '.join(temporary_list)}")

        
        mock_check_chance.assert_called_once_with(chance, word_list, temporary_list)
              
class TestRandomWord(unittest.TestCase):

    @patch('builtins.input', return_value='2')
    @patch('builtins.print')
    @patch('random.randint', return_value=6)
    @patch('random.choice', return_value='planet')
    @patch('Hangman.gues_the_word') 
    def test_random_word_medium_level(self, mock_gues_the_word, mock_choice, mock_randint, mock_print, mock_input):
        words_list = ['apple', 'planet', 'elephant']
        
        Random_word(words_list)

        mock_input.assert_called_once_with("> Choose the level: Easy = 1,  Medium = 2, Hard = 3: ")
        mock_randint.assert_called_once_with(5, 8)
        mock_choice.assert_called_once_with(['planet'])
        mock_print.assert_called_once_with('planet')
        mock_gues_the_word.assert_called_once_with('planet')

    @patch('builtins.input', return_value='1')
    @patch('random.randint', return_value=4)
    @patch('random.choice', return_value='word')
    @patch('builtins.print')
    @patch('Hangman.gues_the_word') 
    def test_random_word_easy_level(self, mock_gues_the_word, mock_print, mock_choice, mock_randint, mock_input):
        words_list = ['cat', 'dog', 'word', 'plane']
        
        Random_word(words_list)

        mock_input.assert_called_once_with("> Choose the level: Easy = 1,  Medium = 2, Hard = 3: ")
        mock_randint.assert_called_once_with(1, 4)
        mock_choice.assert_called_once_with(['word'])
        mock_print.assert_called_once_with('word')
        mock_gues_the_word.assert_called_once_with('word')

    @patch('builtins.input', side_effect=['5', '2'])  
    @patch('builtins.print')
    @patch('random.randint', return_value=6)
    @patch('random.choice', return_value='planet')
    @patch('Hangman.gues_the_word')  
    @patch('sys.exit')  
    def test_random_word_invalid_input(self, mock_sys_exit, mock_gues_the_word, mock_choice, mock_randint, mock_print, mock_input):
        words_list = ['apple', 'planet', 'elephant','banana']
        
        Random_word(words_list)

        
        expected_print_calls = [call("Give proper input"), call('planet')]
        mock_print.assert_has_calls(expected_print_calls)
        
        
        expected_input_calls = [
            call("> Choose the level: Easy = 1,  Medium = 2, Hard = 3: "),
            call("> Choose the level: Easy = 1,  Medium = 2, Hard = 3: ")
        ]
        mock_input.assert_has_calls(expected_input_calls)

        
        mock_randint.assert_called_once_with(5, 8)

       
        mock_choice.assert_called_once_with(['planet','banana'])

       
        mock_gues_the_word.assert_called_once_with('planet')

    @patch('builtins.input', side_effect=['1', '2', '3'])
    @patch('builtins.print')
    @patch('random.randint', side_effect=[4, 8, 10]) 
    @patch('random.choice', side_effect=['word', 'elephant', 'biomedical'])
    @patch('Hangman.gues_the_word')  
    def test_random_word_all_levels(self, mock_gues_the_word, mock_choice, mock_randint, mock_print, mock_input):
        words_list = [
            'cat', 'dog', 'word', 'plane', 'elephant', 
            'biomedical', 'philosophy', 'banana'
        ]
        
        for _ in range(3):  
            Random_word(words_list)

        
        expected_input_calls = [
            call("> Choose the level: Easy = 1,  Medium = 2, Hard = 3: "),
            call("> Choose the level: Easy = 1,  Medium = 2, Hard = 3: "),
            call("> Choose the level: Easy = 1,  Medium = 2, Hard = 3: "),
            
        ]
        mock_input.assert_has_calls(expected_input_calls)

       
        expected_randint_calls = [
            call(1, 4), 
            call(5, 8),  
            call(9, 14), 
            
        ]
        mock_randint.assert_has_calls(expected_randint_calls)

        
        expected_choice_calls = [
            call(['word']),
            call(['elephant']),
            call(['biomedical','philosophy']),
            
        ]
        mock_choice.assert_has_calls(expected_choice_calls)

       
        expected_print_calls = [
            call('word'),
            call('elephant'),
            call('biomedical'),
           
        ]
        mock_print.assert_has_calls(expected_print_calls)

       
        expected_gues_the_word_calls = [
            call('word'),
            call('elephant'),
            call('biomedical'),
            
        ]
        mock_gues_the_word.assert_has_calls(expected_gues_the_word_calls)
 
class TestRemoveCharAfterSingleQuote(unittest.TestCase):

    @patch('Hangman.Random_word')
    def test_basic_single_quote(self, mock_random_word):
        words = ["can't", "won't", "it's"]
        expected = ["can", "won", "it"]

        remove_char_after_single_quote(words)

        mock_random_word.assert_called_once_with(expected)

    @patch('Hangman.Random_word')
    def test_no_single_quote(self, mock_random_word):
        words = ["cat", "dog", "bird"]
        expected = ["cat", "dog", "bird"]

        remove_char_after_single_quote(words)

        mock_random_word.assert_called_once_with(expected)

    @patch('Hangman.Random_word')
    def test_multiple_single_quotes(self, mock_random_word):
        words = ["don't", "she's", "it's"]
        expected = ["don", "she", "it"]

        remove_char_after_single_quote(words)

        mock_random_word.assert_called_once_with(expected)

    @patch('Hangman.Random_word')
    def test_empty_input(self, mock_random_word):
        words = []
        expected = []

        remove_char_after_single_quote(words)

        mock_random_word.assert_called_once_with(expected)

    @patch('Hangman.Random_word')
    def test_word_with_single_quote_only(self, mock_random_word):
        words = ["don't", "o'clock", "isn't"]
        expected = ["don", "o", "isn"]

        remove_char_after_single_quote(words)

        mock_random_word.assert_called_once_with(expected)
 
 
class TestMainFunction(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data="can't won't it's")
    @patch('Hangman.remove_char_after_single_quote')
    def test_main_normal_case(self, mock_remove_char, mock_file):
       
        Main()

       
        mock_file.assert_called_once_with("dictionary.txt", 'r')

        
        mock_remove_char.assert_called_once_with(["can't", "won't", "it's"])

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_main_file_not_found(self, mock_file):
        with patch('builtins.print') as mock_print:
            Main()

          
            mock_print.assert_called_once_with("Error: The file 'dictionary.txt' was not found.")

    @patch('builtins.open', new_callable=mock_open, read_data="dummy data")
    @patch('Hangman.remove_char_after_single_quote')
    def test_main_unexpected_error(self, mock_remove_char, mock_file):
        
        mock_remove_char.side_effect = ValueError("Unexpected error")

        with patch('builtins.print') as mock_print:
            Main()

            mock_print.assert_called_once_with("An unexpected error occurred: Unexpected error")

 
 
        
        
        
if __name__ == '__main__':
    unittest.main()