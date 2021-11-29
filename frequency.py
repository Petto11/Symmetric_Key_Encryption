import re
# this module allows us to make computations with text
# add link documentation

def clean(text_file):
    
    to_be_removed = "[^a-z]" #this refers to each non alphabetical character (the ^ stands for a negation)

    text_file = re.sub(to_be_removed, " ", text_file)

    return text_file