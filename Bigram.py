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

def scoring(text,coprus_bg):
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
