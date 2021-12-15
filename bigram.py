# importing frequency module
import frequency
# importing math module for mathematical computing
import math
# module to work with complex iterators
import itertools
# importing hashlib module to hash messages 
import hashlib
# importing random module to be able to generate random numbers
import random


# Bigrams

def present_bigrams(text):

    '''
    The Present_bigram function, given as input a text, 
    it returns a list containing all the bigrams of the text
    as outputs.

    present_bigrams("hello") --> [he, el, ll, lo]
    '''

    # correcting the text
    words = frequency.clean(text).split()
    # creating the list
    bigrams = [ ]

    for word in words:
        for index in range(0,len(word)-1):

            bigram = word[index : index+2]

            if bigram not in bigrams:
                  bigrams+=[bigram]

    return bigrams


def bigram_freq(text_file):

    '''
    The bigram_freq function takes as input a text and 
    returns as output a dictionary containing as keys 
    all the bigrams contained in the text, and as 
    values a score assigned to each bigram.

    bigram_freq("hello") --> {he:score0, el:score1, ll:score2, lo:score3}
    '''

    # correcting the text
    words = frequency.clean(text_file).split() # creating the dictionary
    bigram_freq_dict = {}
    for word in words:

        for index in range(0,len(word)-1):

            bigram = word[index : index+2]

            if bigram not in bigram_freq_dict:
                bigram_freq_dict[bigram]=1

            else:
                bigram_freq_dict[bigram]+=1
    # calculating the score of bigrams
    tot = sum(bigram_freq_dict.values())

    for bg,count in bigram_freq_dict.items():
        bigram_freq_dict[bg]=math.log10(count/tot)
    # sorting
    bigram_freq_dict = dict(sorted( bigram_freq_dict.items(), key=lambda x:x[1] , reverse=True))
    return bigram_freq_dict


# Score function

def scoring(text,corpus_bg):

    '''
    The scoring function, given as input a text and the
    “scoring board” built with the bigram_freq, puts back
    as output the score of the text.
    '''

    bg=present_bigrams(text)
    score=0
    for bigram in bg:
        if bigram in corpus_bg.keys():
            score+=corpus_bg[bigram]
        else:
            score+=min(corpus_bg.values())
    return score


# Swapping characters

def swap (string, first_char, second_char):

    '''
    We use the swap function to return, as an output
    a swapped string of characters, starting from 2 
    input: the initial string and the 2 characters 
    that need to be exchangend
    '''
    first_pos = None
    second_pos = None

    for idx, char in enumerate(string):

        if char==first_char:
            first_pos=idx
        if char==second_char:
            second_pos=idx

    res = ''

    for idx,char in enumerate(string):

        if idx==first_pos:
            res+=second_char
        elif idx==second_pos:
            res+=first_char
        else:
            res+=char

    return res


# Permutations

def Permute(key):
    
    '''
    The Permute function, specified as input a key 
    (a string containing the 26 characters of the 
    alphabet), returns a list containing 325 
    different versions of this key.
    '''
    keys = []
    while(len(keys)<325):
        i = random.randrange(0, 26, 1)
        j = random.randrange(0, 26, 1)
        if (i==j):
            continue
        else:
            temp_key = key
            temp_key = swap(key, key[i], key[j])
            if temp_key not in keys:
                keys+=[temp_key]
    return keys


# Brute Froce Attack

def brute_force(ciphertext, starting_key, corpus_bg, length, digest):

    '''
    The brute_force function is a function aiming to send back
    the right decrypted text (the candidate plaintext), through 
    the exploitation of 5 inputs: an initial key, a ciphertext,
    a specified number of attempts (length), a digest and the 
    scoring board built with the bigram_freq function. 
    '''

    candidate_plaintext = frequency.decryption(ciphertext, starting_key)
    max_score = scoring(candidate_plaintext, corpus_bg)

    best_key = starting_key
    all_keys=[]

    for i in range(15):

        list_keys = Permute(best_key)
        best_candidate = candidate_plaintext

        for idx, key in enumerate(list_keys):
            if key in all_keys:
                continue

            candidate_plaintext = frequency.decryption(ciphertext, key)
            score = scoring(candidate_plaintext, corpus_bg)
            #attribuisco ai bigram del nuovo candidate i benchmark score


            #if we find a better score, then we reassign three variables:
            # the key, the score and the plaintext
            if score > max_score:
                print('Score of the attempt number', i+1, ':', score)
                best_key = key
                max_score=score
                best_candidate = candidate_plaintext

                actual_digest = hashlib.sha256(best_candidate.encode('utf-8')).hexdigest()

                if digest==actual_digest:
                    print("\nFound! Here's the original text:\n")
                    return best_candidate[:length]
                break

                #in the lucky case in which we find the real digest, we return the
                # current result

    return best_key, best_candidate[:length]
