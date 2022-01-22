Frequency part
The process starts with a  message encrypted with a substitution algorithm as input. To discover the content of the plaintext, we will perform statistical analysis on the character frequency and then, if this doesn’t work, pass to a brute force approach. Since the corpus used in this program is written in English, the encrypted plaintext must be written in English.
We start by picking a corpus of English text, as could be a collection of books , and counts the number of occurrences of each character in the text, finding the corpus characters distribution  . We then will repeat this process for the ciphertext and obtain a cipher characters distribution 
Assumptions: By analyzing a long-enough corpus, we can compare it to the whole English alphabet, and infer that the frequency obtained from the corpus is actually the frequency of characters in the English language. If the ciphered message is long enough, we can infer that the ranking of characters frequency in the ciphertext is actually equal to the one of the English alphabet. We then can suppose that the most frequent letter of the cipher corresponds, in plain, to the most frequent letter of the English alphabet, so the most frequent letter of the corpus. 
At this point, we will match the most frequent letter of the corpus with the most frequent letter of the ciphertext, and so on until all letters are matched. When the process is completed, we will obtain an initial decryption key that we can use to decrypt the text. 
The plaintext we will obtain might not be 100% correct since the assumption we are relying on in this initial part of the attack are very strong. At this stage of the process, we can manually adjust the key and correct the errors made by the frequency analysis or pass to a brute force approach. 

Bigram part
A possible approach could be trying to decrypt the message with every possible permutation of a 26-letter string (the key), but this would take a while (and for a while, I mean trying almost 4,03*10^26 possible permutations). 
To complete the process in a useful timespan we can analyze, instead of the frequency of characters, the frequency of bigrams. To do this we start again from the corpus and finds the occurrences of all the bigrams in the text. At this point, instead of swapping the most frequent bigrams in the corpus with the most frequent in the cipher, we build different keys and test their performance. 
Since we don’t know the correct key, we apply a Brute Force approach: guessing possible combinations of a targeted input, until the correct one is discovered
We build a scoring function, to have a quantitative comparator between different solutions (keys). We assign to each bigram in the corpus a relative score calculated as log10(Bigram frequency). In this way a bigram that is largely diffused in the English alphabet (ex. “th”) will have a high score, while a less diffused bigram (ex. “bf”) will have a significantly lower score. In this way we penalize non-frequent bigrams in the candidate plaintext. 
The score for each candidate plaintext is calculated by finding all the bigrams present in the text, checking the score assigned to each bigram in the “scoring board” built on the plaintext and summing them. 
We then swap 2 letters at random in the candidate key, calculate the score of the new candidate plaintext, and check if it’s higher than the previous one. If this is true, we start to swap random letters on the new key, while if the score is lower we swap 2 other random letters in the initial key.



<img width="508" alt="Schermata 2022-01-22 alle 15 53 16" src="https://user-images.githubusercontent.com/78164372/150643516-6a2a4e88-8b56-47c9-bb92-342ab92cf70c.png">




#Students
Diana Lorenzo 878664
Scatto Giacomo 878819
Volpato Pietro 879528
Cortesia Leonardo 879875
Vian Nicolo' 879914
