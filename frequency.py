import re
# this module allows us to make computations with text
# add link documentation

def clean(text_file):
    
    to_be_removed = "[^a-z]" #this refers to each non alphabetical character (the ^ stands for a negation)
    second_tbr = "\n" 

    text_file = re.sub(to_be_removed, " ", text_file)
    text_file = re.sub(second_tbr, " ", text_file) #removes the \n and replace them it with a blank space. 

    return text_file