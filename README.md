# Symmetric_Key_Encryption 

Symmetric Key Encryption is a software development project that allows users to decrypt encrypted text without knowing the relative key.

This is possible exploiting the frequency of the characters in the encrypted text, and actually, with some refinements, pretty accurate. 

In order to be sure of the accuracy of the results, the user of our program must also have the hash of the original message: this is the best way to check that the program is running smoothly. 

Here below you will find a detailed logic of the way we are achieving a solution, and how to actually try the code yourself.

Enjoy! 

## 1 History of Cryptography

From the dawn of time, human beings have had the basic need to communicate and
share information.
In order to satisfy these necessities, writing systems were developed and people were
finally able to share information easily.
However, as civilizations evolved, human beings got organized into tribes, groups, and
kingdoms.
This led to the emergence of ideas such as power, battles, supremacy, and politics: ideas
which further fueled the natural need of people to communicate secretly.
People started to think of techniques to alter messages in such a way that only the
intended people could have access to their actual meaning.
Unauthorized people could not extract any information, even if the scrambled messages
fell in their hands.
This is how cryptography was born.
The word ‘cryptography’ was coined by combining two Greek words, ‘Krypto’ meaning hidden and ‘graphene’ meaning writing, and its roots are mainly found in Roman and
Egyptian civilizations.
One of the first algorithms that permitted the encryption and decryption of text messages was in fact the Caesar algorithm, which basically replaces a letter with the one
in the alphabet given a fixed and decided position.
For example, the letter B, set a “key” of 4, would become F, since if we move four spots
to the right from the second letter of the alphabet, we obtain F, which is the sixth.

## 1.1 How does hashing works?
A hash function is a unidirectional function that, once applied to data, generates a
 digest. It is a fixed size string of 128,160,256 bits. The digest, being in function of data,
 produces different outputs for different inputs given to the hash function.
 Since the output of hashing functions (digest) is fixed, different inputs might produce
the same output. This phenomenon is known as collision. With the computational
power we have today is very unlikely, in an acceptable timespan, that we are able to
find 2 inputs which produce the same output, but still, we must be aware of the
probability that this could happen.
Through hashing we can achieve the integrity security service, since just one changed
 bit in the original text would produce a completely different digest.

## 1.2 How does symmetric encryption works?

Let’s start the analysis of how symmetric key encryption works by examining its most important elements:
- The plaintext: A piece of information which humans can understand and/or relate
to. It can be a simple English sentence, a script, or a Java code.
- The ciphertext: The result of encryption performed on plaintext using an algorithm and a key, called cipher. The ciphertext and the plaintext have the same length.
- The key: a piece of information (usually a string of numbers or letters) that when
passed to a cryptographic algorithm, can encrypt or decrypt data.

Alice and Bob, two people that want to communicate, agree on a shared key and a cipher algorithm to use. When Alice wants to communicate, she uses the cipher algorithm and the key to create an encrypted message starting from the plaintext. Under those circumstances, when Bob receives the message, he will be able to decrypt
it “only” if he uses the same algorithm and the relative key.
The algorithm has the “symmetric” prefix because the algorithm can be used both to decrypt the ciphertext and encrypt the plaintext given the correspondent key.
Encryption is based on two operations, substitution and transposition. The substitution algorithm replaces one symbol with another in a standardized manner, while the transposition one just exchanges the order of the symbols. Both algorithms preserve the frequency of letters present in the plaintext, so the simple version of both can be defeated using statistical analysis.
Disclaimer: The statistical analysis on character frequency can be easily performed only if the attacker knows the alphabet in which the plaintext is written in. Otherwise, the attacker cannot be sure about the corpus’ language to use. 

A significant example of how a simple substitution algorithm can be defeated, and therefore get the ciphered message decrypted, is frequency.

## 1.3 Attack reproduction
Let’s try to grasp how it practically works by reproducing a symmetric key encryption attack!

Eve is able to intercept the message that Alice sent to Bob, but the message is encrypted with a substitution algorithm. To discover the content of the plaintext Eve will perform statistical analysis on the character frequency and then, if this doesn’t work, pass to a brute force approach. In this reproduction the alphabet is known and it’s the English
Eve also intercepted the digest of the original message, so for each trial she makes with each different key she can compute the digest of the candidate plaintext and check if it’s equal to the “stolen” one. If both matches Eve is sure that the decryption key she used is correct. As mentioned above there might be collisions with the digests, but the probability of this happening is close to 0.

The attacker (Eve) picks a corpus of English text, as could be a collection of books , and counts the number of occurrences of each character in the text. At the end she will have the corpus characters distribution (displayed in fig. 2.1). She then will repeat this process for the ciphertext and obtain a cipher characters distribution (displayed in fig. 2.2).

<img width="508" alt="Schermata 2022-01-22 alle 15 53 16" src="https://user-images.githubusercontent.com/78164372/150643516-6a2a4e88-8b56-47c9-bb92-342ab92cf70c.png">

Assumptions: By analyzing a long-enough corpus, Eve can compare it to the whole English alphabet, and infer that the frequency obtained from the corpus is actually the frequency of characters in the English language. If the ciphered message is long enough, Eve can infer that the ranking of characters frequency in the ciphertext is actually equal to the one of the English alphabet. Eve then can suppose that the most frequent letter of the cipher corresponds, in plain, to the most frequent letter of the English alphabet, so the most frequent letter of the corpus.

At this point, Eve will match the most frequent letter of the corpus with the most frequent letter of the ciphertext, and so on until all letters are matched. When the process is completed, Eve will be in possession of an initial decryption key that she can
use to decrypt the ciphered text.
The plaintext Eve will obtain might not be 100% correct since the assumption we are relying on in this initial part of the attack are very strong. At this stage of the process eve can manually adjust the key and correct the errors made by the frequency analysis or pass to a brute force approach.

## 2.1 Brute force attack

What Eve can do if the initial key is not correct is trying to guess it through a Brute Force Attack. 

This kind of attack is also known as an exhaustive search: a cryptographic hack that consists of guessing possible combinations of a targeted input (e.g., a key), until the correct one is discovered. The longer the password, the harder will be the process to discover the key.

A possible approach could be trying to decrypt the message with every possible permutation of a 26-letter string (the key), but this would take a while (and for a while, I mean trying almost 4,03*10^26 possible permutations).

To complete the process in a useful timespan Eve can analyze, instead of the frequency of characters, the frequency of bigrams. To do this eve starts again from the corpus and finds the occurrences of all the bigrams in the text. At this point eve can’t just swap the most frequent bigrams in the cipher with the one in the corpus like before, because she’ll unlikely arrive to the final solution. She has to test multiple keys and compare the performance of each one, to find at each iteration a solution which is better than the previous one.

To do this Eve has to build a scoring function, to have a quantitative comparator between different solutions (keys). She assigns to each bigram in the corpus a relative score calculated as log10(Bigram frequency). In this way a bigram that is largely diffused in the English alphabet (ex. “th”) will have a high score, while a less diffused bigram (ex. “bf”) will have a significantly lower score.

The score for each candidate plaintext is calculated by finding all the bigrams present in the text, checking the score assigned to each bigram in the “scoring board” built on the plaintext and summing them.
Eve then swaps two letters at random in the initial key and produces a new one. She calculates the score of the new candidate plaintext, which is the ciphered text decrypted with the new key and checks if it’s higher than the one of the precedent plaintext. If this is true, eve starts again the process of swapping random letters starting from the new key, but if the score is lower Eve swaps at random other 2 letters in the initial key.
The process is repeated until eve finds the correct solution.
 
## 3 Usage Examples

Understood the full logic behind what we have built, it's now time to try it.
Here below you will find a small guide on how to run it.

### 3.1 Setting Up
The first thing to do in order to develop the main functionalities just described is to clone the remote directory.

To do this, the user can type:

```bash
git clone https://github.com/Petto11/Symmetric_Key_Encryption
```


This will automatically download all the files the user needs to run the program.

### 3.2 Functions

In order to develop a suitable structure for our project according to the intended goals, we created 3 main functions and stored them into different modules:

- frequency.py
- bigram.py
- main.py


We then added one function to check the test file

#### 3.2.1 frequencies.py

This module contains several functions which help us decrypting a text using the frequency approach explained above:

* We start with the **clean** function takes as input a text and outputs the latter cleaned, removing all numbers and punctuations. 

* We then continue with the **frequencies** function, which given as input a text, returns a dictionary which has as keys the different characters in the text and as values the number of time the character appears in the text. 

* Then we created the **keys** function which given as input the frequency of the corpus and the frequency of the cipher text.

* We can finally complete the frequencies approach with the **decryption** function which returns the decrypted text taking as input the ciphertext and the key.

We also added the **frequency_approach** function which takes as input the 2 texts and returns the first plaintext and the decryption key. It basically unifies the *decryption* and *keys* functions.

After matching the frequencies of the corpus with the one of the ciphertext we computed a decrpytion key and hence a partially decoded text, which however was still far from perfection.

To complete the process we must pass to the brute force (or bigram) approach

#### 3.2.2 bigram.py

This module contains several functions which help us decrypting a text using the bigram approach explained above:

* We start with the most basic part of the process and we create the this  **present_bigrams** function, which takes as input a text and returns as outputs a list containing all the bigrams of the text.

* To compare different texts we needed a scoreboard as a reference, so to do this we implemented the **bigram_freq** function, which takes as input a text and returns a dictionary containing as keys all the bigrams contained in the text, and as values a score assigned to each bigram. (The score is calculated by making the logarithm in base 10 of the bigram’s frequency)

* As explained before, we needed a quantitative measure to compare different candidate plaintext. To compute the score of each candidate plaintext we built this function called scoring, which takes as input a text and the “scoring board” built with the bigram_freq function, and returns as output the score of the text.

* To improve the score given by our key, we built this function called random_Permute, which takes as input a key and returns all the possible 325 versions of the latter

* To swap 2 random characters in the key we used the **swap** function which takes as input one string and the two characters that need to be exchanged, and as it is easy to guess, it outputs the new “swapped” string.

Now we can finally complete the process with the **Brute force** function,  in charge of checking all possible keys until it finds the right one. To avoid making too many computations and keep the process pretty easy to run, we limited the amount of attempts to 10.

#### 3.2.3 main.py
In the file to execute we have different argparse parameters:

* Text 

This is a position argument in which the user has to specify the text to be decrypted. The user has to insert the path of the .txt file or simply the name if it's in the same folder of the main.py file
``` bash
python main.py -text "Ciphertext.txt"
``` 
In this example the software will try to decrypt the Ciphertext.txt file

* Length

This is an optional numerical argument through the which the user can decide the number of characters to be printed from the candidate plaintext.

``` bash
python main.py -text "Ciphertext.txt" --length 1000
``` 
In this example the software will try to decrypt the Ciphertext.txt file and will print out the first 1000 of the candidate plaintext.
If the user does not specify anything the software will print out the whole candidate plaintext.

* Brute

This is an optional text argument through which the user can decide if he wants to decrypt the text using only the frequency approach or also using the brute force approach.

If to the parameter is given as input 'Y' the software will use the brute force approach, otherwise it will simply use the frequency one

``` bash
python main.py -text "Ciphertext.txt" --length 1000 --brute 'Y'
``` 

In this example the software will apply the brute force approach to the "Cipertext.txt" file and it will print out the first 1000 characters of the candidate plaintext. 

---

In the executable file we also added a checker for the type of the file given as input to the "text" positional argument. Since our program allows only .txt files, any other fyle-type will make the program stop and return an error message:

```pyhton
"You must insert a .txt file, other formats are not accepted"
```

---

To decrypt a text using statistica properties of character frequency the **cleaned** text (without numbers and punctuations) must be long at least 5000 characters, since those properties are not maintained by short texts. If the text is shorter than 5000 characters, the program will return an error message: 


```pyhton
"Since the analysis made on the encrypted text is based on 
statystical properties of a language, the program will work 
only if the text to decrypt is at least 5000 characters long 
(numbers and punctuation excluded)"
```



## Contributing

If you would like to contribute to the Symmetric Key Encryption, please feel free to submit pull requests. 
Please contact us if you wish to implement significant changes and test them before pulling.

## License

Da mettere il nome della licenza


## Developers
Cortesia Leonardo
Diana Lorenzo 
Scatto Giacomo
Vian Nicolo'
Volpato Pietro  
