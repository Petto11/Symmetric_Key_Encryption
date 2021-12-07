import frequency

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
    words = cleaning(text_file).split() # creating the dictionary bigram_freq_dict = {}
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
    Bg=present_bigrams(text)
    Score=0
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

    permutations = list(itertools.permutations(key[::-1],2))
    keys = []

    #transforming the key intro string for simplicity
    str_key = ''
    for i in key:
        str_key+=i

    for one,two in permutations:
        temp = str_key
        temp = swap(temp,one,two)
        if temp not in keys:
            keys += [temp]

    return keys

def brute_force(ciphertext, starting_key, corpus_bg, attempts, n_char):

    max_score=-2000
    all_keys = []
    candidate_plaintext = decryption(ciphertext, starting_key)

    best_key = starting_key

    for i in range(attempts):

        list_keys = Permute(best_key)
        best_candidate = candidate_plaintext

        for idx, key in enumerate(list_keys):


            candidate_plaintext = decryption(ciphertext, key)
            new_bg = bigram_freq(candidate_plaintext)

            #attribuisco ai bigram del nuovo candidate i benchmark score
            score=0
            for bigram in new_bg:
                if bigram in corpus_bg.keys():
                    score+= corpus_bg[bigram]
                else:
                    score+=min(corpus_bg.values())

            #if we find a better score, then we reassign three variables:
            # the key, the score and the plaintext
            if score > max_score:

                best_key = key
                max_score=score
                best_candidate = candidate_plaintext

    return best_key, best_candidate[:n_char]
