def file_type(stringa):

    '''
    This function analyses the type of a file and returns True if the fyle is a .txt.
    It extracts the name of the file from the standard framework
    used by the Argparse.fyletype input type.
    '''
    pos=0
    new_str=""
    for idx,char in enumerate(stringa):
        if char == "n":
            pos=idx+6
            break
    for char in range(pos,len(stringa)):
        if stringa[char]!="'":
            new_str+=stringa[char]
        else:
            stringa[char]=="'"
            break
    if new_str.endswith('.txt'):
        return True
    else:
        return False