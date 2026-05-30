import string


def remove_punctuation (text): 
    """retire la ponctuation
    
    Args:
        text (str): le texte sans ponctuation

    Returns:
        text (str): texte nettoyé
    """
    
    for p in string.punctuation:
        if p in text:
            text = text.replace(p, '')

    return text


clean_text = lambda text: remove_punctuation(text).lower()


def count_words (*args):
    
    """compte le nombre total de mots
    
    Args:
        *args (tuple) : texte(s) à examiner

    Returns:
        sorted_counts (dict): compte de tous les mots présents (les espaces vides ont été retiré) rangés par ordre décroissant
    """
    text = ''
    for arg in args:
        text += ' ' + arg
    
    #print(text)
    words = text.split() # sans arguments dans la fonction split(), python gère automatiquement les espaces, tabulations et retours ligne 
    
    counts = {}
    for w in words:
        try :
            counts[w] += 1  #increment everytime the word is encounter in the list
            
        except KeyError:
            counts[w] = 1  #set count for this word to 1
            
    #print(counts)
    
    sorted_counts = {}
    
    while len(counts) > 0:
    
        max_freq = 0
        index = -1
        for word in counts.keys():
            if max_freq < counts[word]:
                max_freq = counts[word]
                index = word
                
        sorted_counts[index] = max_freq
        del counts[index]
        
    return sorted_counts

# ceci est un exemple d'utilisation de la fonction count_words avec plusieurs arguments positionnels
#count_words('salut le monde !', 'coucou', 'tout le monde')


def most_frequent(sorted_freq):
    
    """affiche le(s) mot(s) le(s) plus fréquent(s)
    
    Args:
        sorted_freq (dict) : fréquences de mots rangés dans l'ordre croissant. Ex: {'bonjour': 2, 'monde': 2, 'salut': 1}
        
    Returns:
        most_frequent (tuple): 
            [0] => liste de tous les mots avec les plus fréquents mais ayant exactement le même nombre d'apparition. Ex: ['bonjour', 'monde'],
            [1] => frequency
    """
    
    most_frequent = ""  #variable used to store the words with highest frequency
    for word in sorted_freq.keys():

        try :
            if max_freq == sorted_freq[word]:
                most_frequent += ", " + word + ', ' # max_freq has been iniatiated then we can add now the other words with same frequency
                
            else:  # in the case there are no more word with max_freq
                most_frequent = most_frequent[:-2] # we are removing the last ', '
                return (most_frequent, max_freq)
        
        except NameError: # this statment will be executed at first cause max_freq has not been initiated at this point (soulevant une NameError)
            max_freq = sorted_freq[word] # initiating max_freq (fréquence maximale)
            most_frequent = word # storing the first word
                


def show_top(sorted_freq, top=3):
    
    """affiche les mots les plus fréquents (3 par défaut)
    
    Args:
        sorted_freq (dict) : fréquences de mots rangés dans l'ordre croissant
    """
    print(f'Top {top} :')
    
    for w in sorted_freq.items(): #.items() return all the items in a list of tuples
        print(f'{w[0]} -> {w[1]}') # w[0] stand for word and w[1] stand for frequency
        top -= 1
        
        if top == 0:
            break



text = input('Ecrivez votre texte: ')

frequencies = count_words(clean_text(text))
#print(frequencies)

print('Nombre total de mots : ', sum(frequencies.values()), '\n')

most_list = most_frequent(frequencies)
if len(most_list[0]) > 1 :
    print(f"Les mots les plus fréquents : {most_list[0]} ({most_list[1]} fois chacun)")
else:
    print(f'Mot le plus fréquent : {most_list[0]} ({most_list[1]} fois)')

print()
show_top(frequencies)