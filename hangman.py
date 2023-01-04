import random # Importação do módulo random (aleatório).
from words import words # Do arquivo "words.py" importar a variavél "words".
import string


def get_valid_word(words): # Função para escolher uma palavra aleatória válida.
    word = random.choice(words) # Aleatoriamente escolhe uma palavra da lista.
    while '-' in word or ' ' in word: # Estrutura de repetição para rodar de novo, caso escolha uma palavra com hífen ou espaço.
        word = random.choice(words) # Escolhe novamente caso caia no while de cima.  

    return word.upper() # Retorna a palavra válida escolhida. O ".upper" é para colocar todas as letras em maiúsculas.
                         

def hangman():
    word = get_valid_word(words) 
    word_letters = set(word) # Letras na palavra.
    alphabet = set(string.ascii_upercase) # Python é case sensitive, "a" é diferente de "A". Por isso colocar tudo em maiúsculas com o "upercase".
    used_letters = set() # O que o usuário advinhou. 

    # Coletando digitação do usuário.
    user_letter = input('Advinhe a letra: ').upper() # Independente se ele digitar maiúscula ou minúscula, o ".upper" deixa maiúscula.
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

    elif user_letter in used_letters:
        print('Você já usou essa letra, Por favor tente de novo.')

    else:
        print('Caracter inválido. Por favor tente de novo.')

