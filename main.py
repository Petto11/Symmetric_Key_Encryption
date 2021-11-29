# importare i file

corpus_file = "resources/corpus-war-and-peace-anna-karienina.txt"
coded_file = "resources/ciphertext.txt"

with open (corpus_file, 'r') as f:
    corpus_text = f.read()
with open (coded_file, 'r') as c:
    coded_text = c.read()
