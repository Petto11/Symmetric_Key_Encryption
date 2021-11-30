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
