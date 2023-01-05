import random # Importação do módulo random (aleatório).
from words import words # Do arquivo "words.py" importa a variável "words".
from hangman_visual import lives_visual_dict # Importa o "gráfico" do jogo. Do "hangman_visual.py" importa a variável "lives_visual_dict" responsável pelo gráfico.
import string # Importação do módulo string, não é consenso sua utilidade na versão atual do Python, mas por via das dúvidas não custa colocar.

def get_valid_word(words): # "def" cria a função "get_valid_word" na variável "word", ou seja, palavra válida, que no caso é sem espaço ou hífen.
    word = random.choice(words)  # Aleatóriamente escolhe uma palavra da lista.
    while '-' in word or ' ' in word: # Enquanto for escolhida palavra com hífens ou espaço ¬
        word = random.choice(words) # Repete o comando de escolha de palavra aleatória.

    return word.upper() # Retorna uma palavra e o ".upper()" converte em maiúscula. Pois o Python é case sensitive, "A" =/= "a".


def hangman(): # Cria a função do jogo.
    word = get_valid_word(words) # Recebe uma palavra válida.
    word_letters = set(word)  # Letras na palavra.
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # O que o usuário já advinhou.

    lives = 7 # Define a quantidade de vidas como 7 através da variável "lives".

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('Você tem', lives, 'vidas restantes e já usou essas letras: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Palavra atual: ', ' '.join(word_list))

        user_letter = input('Advinhe uma letra: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # Se errar tira uma vida.
                print('\nA letra,', user_letter, 'não está na palavra.')

        elif user_letter in used_letters:
            print('\nVocê já usou essa letra. Tente outra.')

        else:
            print('\nLetra ou caracter inválido.')

    # Chega aqui quando as palavras que faltam advinhar ou as vidas forem 0.
    if lives == 0: # Se vidas 0:
        print(lives_visual_dict[lives]) # Imagem final da forca.
        print('Você morreu! A palavra era', word, "!") # Mensagem.
    else: # Se não:
        print('Você sobreviveu! A palavra era', word, '!') # Mensagem


if __name__ == '__main__':
    hangman()