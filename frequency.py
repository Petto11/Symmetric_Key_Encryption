import re
# this module allows us to make computations with text
# add documentation
import string
# add documentation

# CLEANING TEXT
def clean(text_file):

    #just for the test - to be changed
    if len(text_file)==0:
         return None

    #the first thing that we'll remove is the pattern '\n'
    first_tbr = "\n"

    '''this refers to each non alphabetical character (the ^ stands for a negation)'''
    second_tbr = "[^a-z]"

    text_file = re.sub(first_tbr, " ", text_file)
    text_file = re.sub(second_tbr, " ", text_file)

    return text_file

# COUNTING THE FREQUENCIES
def frequencies(text_file):
    '''
    This function, given as input a string, returns a dictionary which has as keys the different characters in the string and as values the number of time the character appears in the text(frequency of characters).
    
    frequencies("hello") --> {l:2,e:1,l:1,h:1}
    '''

    freq_dict = {}
    text_file = clean(text_file)

    for character in text_file:

        if character == ' ':
            continue

        if character not in freq_dict:
            freq_dict[character] = 1

        else:
            freq_dict[character]+= 1
    
    freq_dict = dict(sorted(freq_dict.items(),key=lambda x:x[1],reverse=True))

    return freq_dict

# COMPUTING THE KEY
def keys(sorted_freq_corpus, sorted_freq_cipher):
    
    '''
    
    This function builds a key starting from the frequency of the corpus and of the cipher. It takes as input 2 lists, matches them in a dictionary and alphabetically orders keys to obtain the candidate decryption key of the encrypted text
    
    '''

    if len(sorted_freq_corpus) >26 | len(sorted_freq_cipher) > 26:
        return None

    alphabet= string.ascii_lowercase
    dec_key = ''

    for alpha in alphabet:

        for i,j in zip(sorted_freq_cipher, sorted_freq_corpus):

            if alpha==i:

                dec_key+=j

    return dec_key

# DECRYPTION
def decryption(cipher_text, key):
    
    '''
    
    The decryption function takes as input the encrypted text and the decryption key built above, returning the candidate plaintext.
    
    '''

    #I initialize an empty plaintext as base
    plaintext = ''

    alphabet = string.ascii_lowercase

    # I associate to each alphabet character the corresponding
    # 'decodification character'
    dict = {i:j for i,j in zip (alphabet, key)}

    for char in cipher_text:

        # if the character is not in the alphabet there's no
        # need to substitute it
        if char not in dict.keys():
            plaintext +=char
            continue

        for i,j in dict.items():

            if char == i:
                plaintext +=j
                break

    return plaintext
