# importare i file
import frequency
import argparse

parser = argparse.ArgumentParser(description='Decrypts the text given as input')
arser.add_argument("text", type=argparse.FileType('r'), help="Encrypted text to be decrypted")
args = parser.parse_args() #prima era vars(parser.parse_args())



corpus_file = "resources/corpus-war-and-peace-anna-karienina.txt"
#coded_file = "resources/ciphertext.txt"

#added the .lower case beacuse we do not care about the size

with open (corpus_file, 'r') as f:
    corpus_text = f.read().lower()

with open (args, 'r') as f:
    cipher_text = f.read().lower()


# let's see with this approach what we get
real_freq = frequency.frequencies(corpus_text)
c_freq = frequency.frequencies(cipher_text)

first_key = frequency.keys(real_freq, c_freq)
first_plaintext = frequency.decryption(coded_text, first_key)

print(first_plaintext[:100])
