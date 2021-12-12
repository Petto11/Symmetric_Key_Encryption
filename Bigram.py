import frequency
import math
import itertools
import hashlib
import random

def present_bigrams(text):

    words = frequency.clean(text).split()
    bigrams = [ ]

    for word in words:
        for index in range(0,len(word)-1):

            bigram = word[index : index+2]

            if bigram not in bigrams:
                  bigrams+=[bigram]

    return bigrams

def bigram_freq(text_file):
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

def scoring(text,corpus_bg):
    bg=present_bigrams(text)
    score=0
    for bigram in bg:
        if bigram in corpus_bg.keys():
            score+=corpus_bg[bigram]
        else:
            score+=min(corpus_bg.values())
    return score

def swap (string, first_char, second_char):
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

def Permute(key):
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

#    permutations = list(itertools.permutations(key[::-1],2))
 #   permutations = random.sample(permutations, len(permutations))
  #  keys = []

    #transforming the key intro string for simplicity
   # str_key = ''
#    for i in key:
 #       str_key+=i

  #  for one,two in permutations:
   #     temp = str_key
    #    temp = swap(temp,one,two)
     #   if temp not in keys:
    #       keys += [temp]

    #return keys

def brute_force(ciphertext, starting_key, corpus_bg, length,digest):

    candidate_plaintext = ciphertext
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
                print(score)
                best_key = key
                max_score=score
                best_candidate = candidate_plaintext

                actual_digest = hashlib.sha256(best_candidate.encode('utf-8')).hexdigest()
                
                if digest==actual_digest:
                    print("cassa")
                    return best_candidate[:1000]
                break
                
                #in the lucky case in which we find the real digest, we return the
                # current result
                
                break

    return best_key, best_candidate[:length]

