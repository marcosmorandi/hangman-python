import random # Importação do módulo random (aleatório).
from palavras import words # Do arquivo "palavras.py" importa a variável "words".
from visual import lives_visual # Do arquivo "visual.py" importa a variável "lives_visual" responsável pelo "gráfico".
import string # Importação do módulo string, não é consenso sua utilidade na versão atual do Python, mas por via das dúvidas não custa colocar.

# Depois que tirei manualemnte hífens, numeros e espaços em branco das palavras a função abaixo, ficou obsoleta. Teria que mexer em várias partes do código para arrumar tudo.
def get_valid_word(words): # "def" cria a função "get_valid_word" com a variável "words", ou seja, palavra válida, que no caso é sem hífen ou espaço.
    word = random.choice(words)  # Aleatóriamente escolhe uma palavra da lista.
    while '-' in word or ' ' in word: # Enquanto for escolhida palavra com hífens ou espaço...
        word = random.choice(words) # Repete o comando de escolha de palavra aleatória.

    return word.upper() # Retorna uma palavra e o ".upper()" converte em maiúscula.

print('\n============================================================')
print('                       Jogo da Forca                        ') # Título no início do jogo.
print('============================================================')
print(' Tente advinhar o nome de uma das centenas de linguagens    ')
print('de programação listadas no jogo, em uso atual ou histórico. ')
print(' Use somente letras de A a Z, ignore números, espaços em    ') # Descrição e instruções.
print('branco ou caracteres especiais.                             ')
print(' Exemplo: Se achar que a resposta é "C#", digite "csharp",  ')
print('pode digitar maiúscula, minúscula, o programa entende ambas.')
print('============================================================')


def hangman(): # Cria a função do jogo.
    word = get_valid_word(words) # Recebe uma palavra válida.
    word_letters = set(word)  # Define letras na palavra.
    alphabet = set(string.ascii_uppercase) # Fornece as letras de A a Z em maiúsculas (ASCII é americano e diferente de ABNT com Ç etc).
    used_letters = set()  # O que o usuário já advinhou.

    lives = 7 # Define a quantidade de vidas como 7 através da variável "lives recebe 7".

    # Obtendo entrada do usuário.
    while len(word_letters) > 0 and lives > 0: # Enquanto as letras da palavra e as vidas forem maior que 0:
        print('\nVocê tem', lives, 'vidas restantes e já usou essas letras: ', ' '.join(used_letters)) # Imprime quantas vidas restam e junta pelo ".join", as letras já usadas.

        word_list = [letter if letter in used_letters else '-' for letter in word] # Recebe a letra se estiver certa, senão um "-".
        print(lives_visual[lives]) # Imprime o gráfico referente a quantidade de vidas restantes.
        print('Palavra atual: ', ' '.join(word_list)) # Imprime as letras corretas ou "-". 

        user_letter = input('\nAdvinhe uma letra: ').upper() # Recebe e transforma letra digitada pelo usuário em maiúscula.
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else: # Senão:
                lives = lives - 1  # Tira uma vida por errar.
                print('\nA letra,', user_letter, 'não está na palavra.') # Imprime a mensagem e mostra que a letra escolhida não está na palavra.

        elif user_letter in used_letters: # Senão se repetir uma letra.
            print('\nVocê já usou essa letra. Tente outra.') # Imprime mensagem. "\n" quebra a linha, deixando um espaço na linha acima.

        else: # Senão:
            print('\nLetra ou caracter inválido.') # Imprime mensagem.

    # Chega aqui quando as letras que faltam advinhar ou as vidas forem 0.
    if lives == 0: # Se vidas 0:
        print(lives_visual[lives]) # Imprime imagem final da forca.
        print('Você morreu! A palavra era', word, '!\n') # Imprime mensagem e qual era a palavra.
        print('Leia mais sobre a linguagem em https://en.wikipedia.org/wiki/List_of_programming_languages \n') # Um link com mais informações sobre a linguagem.
    else: # Senão:
        print('Você sobreviveu! A palavra era', word, '!\n') # Imprime mensagem e qual era a palavra. Nesse caso o "\n" deixa espaço na linha abaixo.
        print('Leia mais sobre a linguagem em https://en.wikipedia.org/wiki/List_of_programming_languages \n') # Um link com mais informações sobre a linguagem.

hangman() # Chama a função que inicia o jogo. Importante!!! Se o código no Python estiver indentado de maneira incorreta, ele não funciona.