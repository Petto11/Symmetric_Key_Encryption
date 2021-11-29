# importare i file

corpus_file = "resources/corpus-war-and-peace-anna-karienina.txt"
coded_file = "resources/ciphertext.txt"

#added the .lower case beacuse we do not care about the size 

with open (corpus_file, 'r') as f:
    corpus_text = f.read().lower()
with open (coded_file, 'r') as c:
    coded_text = c.read().lower()
