import random
from words import words
from hangman_visual import lives_visual_dict
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('Você tem', lives, 'vidas restantes e você usou estas letras: ', ' '.join(used_letters))

        # Qual é a palavra atual(ou seja, W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Palavra atual: ', ' '.join(word_list))

        user_letter = input('Advinhe a letra: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # Tira uma vida se errar.
                print('\nYour letter,', user_letter, 'não está na palavra.')

        elif user_letter in used_letters:
            print('\nVocê já usou essa letra, tente de novo.')

        else:
            print('\nNão é uma letra válida, tente de novo.')

    # Chegar aqui quando len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('Você morreu! A palavra era', word)
    else:
        print('Você advinhou a palavra, que era', word, '!')


if __name__ == '__main__':
    hangman()