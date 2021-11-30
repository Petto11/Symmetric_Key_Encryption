# importare i file
import frequency

corpus_file = "resources/corpus-war-and-peace-anna-karienina.txt"
coded_file = "resources/ciphertext.txt"

#added the .lower case beacuse we do not care about the size

with open (corpus_file, 'r') as f:
    corpus_text = f.read().lower()
with open (coded_file, 'r') as c:
    coded_text = c.read().lower()

# trynna see if decryption works
fake_key = 'qwertyuiopasdfghjklzxcvbnm'
try1 = frequency.decryption (coded_text, fake_key)
print(try1)
