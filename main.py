# importare i file

import frequency
import bigram
import argparse
import type_control

parser = argparse.ArgumentParser(description='Decrypts the text\
                                 given as input')
parser.add_argument("-text", type=argparse.FileType('r'),
                    help="Encrypted text to be decrypted")
parser.add_argument("--length", type=int,
                    help=" N° of characters in the plaintext to be displayed")
parser.add_argument("--brute", type=str,
                    help="USe or not brute force")
parser.add_argument("--digest", type=argparse.FileType('r'),
                    help="If you have the digest of the original\
                    message you can insert it here")

args = parser.parse_args()
length = args.length
corpus_file = "resources/corpus-war-and-peace-anna-karienina.txt"

cipher = str(args.text)
digest = str(args.digest)


# added the .lower case beacuse we do not care about the size
with open(corpus_file, 'r') as f:
    corpus_text = f.read().lower()

if type_control.file_type(cipher) is True:

    cipher_text = args.text.read()
    first_key, first_plaintext = frequency.frequency_approach(corpus_text,
                                                              cipher_text)

    if len(frequency.clean(cipher_text)) < 5000:
        print("Since the analysis made on the encrypted text is based on \
        statystical properties of a language, the program will work only \
        if the text to decrypt is at least 5000 characters long (numbers \
        and punctuation excluded)")

    elif args.brute == 'Y':

        if type_control.file_type(digest) is True:
            digest_text = args.digest.read()
            print(bigram.brute_force(cipher_text, first_key,
                                     bigram.bigram_freq(corpus_text),
                                     args.length, digest_text))

        else:
            print(bigram.brute_force(cipher_text, first_key,
                                     bigram.bigram_freq(corpus_text),
                                     args.length, " "))

    elif args.brute != 'Y':
        print(first_plaintext)

else:
    print('You must insert a .txt file, other formats are not accepted')
