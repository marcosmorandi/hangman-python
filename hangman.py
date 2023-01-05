import random # Importação do módulo random (aleatório).
from words import words # Do arquivo "words.py" importa a variável "words".
from visual import lives_visual_dict # Importa o "gráfico" do jogo. Do "visual.py" importa a variável "lives_visual_dict" responsável pelo gráfico.
import string # Importação do módulo string, não é consenso sua utilidade na versão atual do Python, mas por via das dúvidas não custa colocar.

def get_valid_word(words): # "def" cria a função "get_valid_word" com a variável "words", ou seja, palavra válida, que no caso é sem hífen ou espaço.
    word = random.choice(words)  # Aleatóriamente escolhe uma palavra da lista.
    while '-' in word or ' ' in word: # Enquanto for escolhida palavra com hífens ou espaço...
        word = random.choice(words) # Repete o comando de escolha de palavra aleatória.

    return word.upper() # Retorna uma palavra e o ".upper()" converte em maiúscula. Pois o Python é case sensitive, "A" =/= "a".


def hangman(): # Cria a função do jogo.
    word = get_valid_word(words) # Recebe uma palavra válida.
    word_letters = set(word)  # Define letras na palavra.
    alphabet = set(string.ascii_uppercase) # Fornece as letras de A a Z em maiúsculas (ASCII é americano e diferente de ABNT).
    used_letters = set()  # O que o usuário já advinhou.

    lives = 7 # Define a quantidade de vidas como 7 através da variável "lives".

    # Obtendo entrada do usuário.
    while len(word_letters) > 0 and lives > 0: # Enquanto as letras da palavra e as vidas forem maior que 0:
        print('Você tem', lives, 'vidas restantes e já usou essas letras: ', ' '.join(used_letters)) # Imprime quantas vidas restam e junta, ".join", as letras já usadas.

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

            else: # Senão:
                lives = lives - 1  # Tira uma vida por errar.
                print('\nA letra,', user_letter, 'não está na palavra.') # Imprime a mensagem e mostra que a letra escolhida não está na palavra.

        elif user_letter in used_letters: # Senão se repetir uma letra.
            print('\nVocê já usou essa letra. Tente outra.') # Imprime mensagem. "\n" quebra a linha, deixando um espaço na linha de cima.

        else: # Senão:
            print('\nLetra ou caracter inválido.') # Imprime mensagem.

    # Chega aqui quando as letras que faltam advinhar ou as vidas forem 0.
    if lives == 0: # Se vidas 0:
        print(lives_visual_dict[lives]) # Imprime imagem final da forca.
        print('Você morreu! A palavra era', word, "!") # Imprime mensagem e qual era a palavra.
    else: # Senão:
        print('Você sobreviveu! A palavra era', word, '!') # Imprime mensagem e qual era a palavra.


if __name__ == '__main__':
    hangman()