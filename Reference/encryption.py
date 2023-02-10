

"""
This python file is not used !!
This is just for pure reference
 
"""

import alphabets
lst_of_alphabets = alphabets.lst_alphabet

def encrypt(type,shiftNumber):
    new_type = ""
    for letter in type:
            
        if ((letter >= 'a' and letter <= 'z' ) or (letter >= 'A' and letter <= 'Z')):
            index = lst_of_alphabets.index(letter)
            letter1 = lst_of_alphabets[index+shiftNumber]
            new_type += letter1
        else :
            new_type +=letter

    print(f"Encoded Message : {new_type}")