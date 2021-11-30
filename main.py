# importare i file
import frequency

corpus_file = "resources/corpus-war-and-peace-anna-karienina.txt"
coded_file = "resources/ciphertext.txt"

#added the .lower case beacuse we do not care about the size

with open (corpus_file, 'r') as f:
    corpus_text = f.read().lower()
with open (coded_file, 'r') as c:
    coded_text = c.read().lower()

# let's see with this approach what we get
real_freq = frequency.frequencies(corpus_text)
c_freq = frequency.frequencies(coded_text)

first_key = frequency.keys(real_freq, c_freq)
first_plaintext = frequency.decryption(coded_text, first_key)

print(first_plaintext[:100])
