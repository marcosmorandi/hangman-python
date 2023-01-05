import random  # Importação do módulo random (aleatório).
from words import words  # Do arquivo "words.py" importa a variável "words".
from hangman_visual import lives_visual_dict
import string  # Importação do módulo string, atualmente desnecessário segundo alguns, mas vai que né!

# Função para escolher uma palavra aleatória válida, ou seja, sem hífen ou espaço em branco.


def get_valid_word(words):
    word = random.choice(words)  # Aleatoriamente escolhe uma palavra da lista.
    # Enquanto for escolhida uma palavra com hífen ou espaço em branco, executa o comando abaixo.
    while '-' in word or ' ' in word:
        # Escolhe novamente caso caia no while de cima.
        word = random.choice(words)

    # Retorna a palavra válida escolhida. O ".upper" é para colocar as letras em maiúsculas.
    return word.upper()


def hangman():  # Função para iniciar o jogo.
    word = get_valid_word(words)  # Escolhe uma palavra válida.
    word_letters = set(word)  # Letras na palavra.
    # Python é case sensitive, "a" é diferente de "A". Por isso colocar tudo em maiúsculas com o "upercase".
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # O que o usuário advinhou.

    lives = 7  # Quantidade de vidas.

    # Coletando digitação do usuário.
    while len(word_letters) > 0 and lives > 0:
        # Letras usadas.
        # ' '.join(['a', 'b', 'cd'] --> a b cd
        print('Você tem', lives, 'vidas restantes e você usou estas letras: ',
              ' '.join(used_letters))

        # Qual é a palavra atual(ou seja, W - R D)
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Palavra atual: ', ' '.join(word_list))

    # Independente se ele digitar maiúscula ou minúscula, o ".upper" deixa maiúscula.
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
