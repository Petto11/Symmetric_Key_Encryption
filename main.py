# importare i file
import frequency
import Bigram
import argparse

parser = argparse.ArgumentParser(description='Decrypts the text given as input')
parser.add_argument("-text", type=argparse.FileType('r'), help="Encrypted text to be decrypted")
parser.add_argument("--length", type=int, help=" N° of characters in the plaintext to be displayed")
parser.add_argument("--brute", type=str, help="USe or not brute force")
args = parser.parse_args() #prima era vars(parser.parse_args())


length=args.length
corpus_file = "resources/corpus-war-and-peace-anna-karienina.txt"
digest= "resources/sha256sum.txt"
#added the .lower case beacuse we do not care about the size
with open (corpus_file, 'r') as f:
    corpus_text = f.read().lower()
with open (digest, 'r') as f:
    digest_text = f.read().lower()

cipher_text = args.text.read()

# let's see with this approach what we get
first_key,first_plaintext=frequency.frequency_approach(corpus_text,cipher_text)
#print(first_plaintext[:100])

if args.brute == 'Y':
    print(Bigram.brute_force(cipher_text,first_key, Bigram.bigram_freq(corpus_text), args.length,digest_text))
else:
    print(first_plaintext[:args.length])
