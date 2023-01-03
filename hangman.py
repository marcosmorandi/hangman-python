import random # Importação do módulo random (aleatório).
from words import words

def get_valid_word(words): # Função para escolher uma palavra aleatória válida.
    word = random.choice(words) # Aleatoriamente escolhe uma palavra da lista.
    while '-' in word or ' ' in word: # Estrutura de repetição para rodar de novo, caso escolha uma palavra com hífen ou espaço.
        word = random.choice(words) # Escolhe novamente caso caia no while de cima.  

    return word.upper() # retorna a palavra válida escolhida. O ".upper" é para colocar todas as letras em maiúsculas.