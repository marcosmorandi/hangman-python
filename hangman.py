import random # Importação do módulo random (aleatório).
from palavras import words # Do arquivo "palavras.py", importa a variável "words".
from visual import lives_visual # Do arquivo "visual.py", importa a variável "lives_visual", responsável pelo "gráfico".
import string # Importação do módulo string, sem ele o "alphabet" ou outras strings podem não funcionar corretamente.

# Depois que tirei manualmente hifens, numeros e espaços em branco das palavras, a função abaixo ficou obsoleta. Não quis mexer para não quebrar o código e pelo prazo de entrega.
def get_valid_word(words): # "def" cria a função "get_valid_word" com a variável "words", ou seja, palavra válida, que no caso é sem hífen ou espaço.
    word = random.choice(words)  # Aleatóriamente escolhe uma palavra da lista.
    while '-' in word or ' ' in word: # Enquanto for escolhida palavra com hifens ou espaço:
        word = random.choice(words) # Repete o comando de escolha de palavra aleatória.

    return word.upper() # Retorna uma palavra e o ".upper()" converte em maiúscula. No Python "A" é diferente de "a".

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
    word = get_valid_word(words) # Variável que recebe uma palavra válida da variável importada "words".
    word_letters = set(word)  # "set()" é usado para armazenar múltiplos itens em uma única variável. Criada a variável "word_letters" ou letras_na_palavra.
    alphabet = set(string.ascii_uppercase) # Importa alfabeto no código padrão americano (ASCII), em maiúsculas, "set(string.ascii_uppercase)". Python é casesensitive, "A" difere de "a".
    used_letters = set()  # Variável que armazena letras já acertadas.

    lives = 7 # Define a quantidade de vidas como 7 através da variável "lives recebe 7".

    # Obtendo entrada do usuário. Usando o loop enquanto "while", até o jogo acabar.
    while len(word_letters) > 0 and lives > 0: # Enquanto as letras da palavra e as vidas forem maior que 0:
        print('\nVocê tem', lives, 'vidas restantes e já usou essas letras: ', ' '.join(used_letters)) # Imprime quantas vidas restam e junta pelo ".join", as letras já usadas.

        word_list = [letter if letter in used_letters else '-' for letter in word] # Armazena letras corretas ou "-" na variável "word_list".
        print(lives_visual[lives]) # Imprime o gráfico referente a quantidade de vidas restantes.
        print('Palavra atual: ', ' '.join(word_list)) # Imprime as letras corretas já digitadas ou "-" para as que faltam.

        user_letter = input('\nAdvinhe uma letra: ').upper() # Recebe pelo "input" e transforma a letra digitada pelo usuário em maiúscula pelo ".upper()". No Python "A" é diferente de "a".
        if user_letter in alphabet - used_letters: # Se for uma letra válida do alfabeto, não usada ainda:
            used_letters.add(user_letter) # .add() adiciona um elemento se ele não já estiver presente. No caso ao "used_letters" ou letras_usadas.
            if user_letter in word_letters: # Se a letra recebida estiver nas letras da palavra a ser advinhada:
                word_letters.remove(user_letter) # .remove() remove a letra digitada pelo usuário da palavra a ser advinhada. Remove do "word_letters".
                print('') # Foi a solução para deixar espaço entre linhas ao acertar a ultima letra.

            else: # Senão:
                lives = lives - 1  # Tira uma vida por errar.
                print('\nA letra,', user_letter, 'não está na palavra.') # Imprime a mensagem e mostra que a letra escolhida não está na palavra. "\n" deixa espaço na linha acima.

        elif user_letter in used_letters: # Senãose repetir uma letra:
            print('\nVocê já usou essa letra. Tente outra.') # Imprime mensagem. "\n" quebra a linha, deixando um espaço na linha acima.

        else: # Senão:
            print('\nLetra ou caracter inválido.') # Imprime mensagem.

    # Chega aqui quando as letras que falta advinhar ou as vidas forem 0.
    if lives == 0: # Se vidas igual 0:
        print(lives_visual[lives]) # Imprime imagem final da forca.
        print('Você morreu! A palavra era', word, '!\n') # Imprime mensagem e qual era a palavra.
        print('Leia mais sobre a linguagem em https://en.wikipedia.org/wiki/List_of_programming_languages \n') # Um link com mais informações sobre a linguagem.
    else: # Senão:
        print('Você sobreviveu! A palavra era', word, '!\n') # Imprime mensagem e qual era a palavra. Nesse caso o "\n" deixa espaço na linha abaixo.
        print('Leia mais sobre a linguagem em https://en.wikipedia.org/wiki/List_of_programming_languages \n') # Um link com mais informações sobre a linguagem.

hangman() # Chama a função que inicia o jogo. Importante!!! Se o código no Python estiver indentado de maneira incorreta, ele não funciona.