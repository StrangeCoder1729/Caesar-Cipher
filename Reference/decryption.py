
"""
This python file is not used !!
This is just for pure reference
 
"""
import alphabets
lst_of_alphabets = alphabets.lst_alphabet
 
def decrypt(type,shiftNumber):
    
    new_type = ""
    for letter in type:
         
        if letter == " ":
            new_type+=letter
        
        else:
            index = lst_of_alphabets.index(letter)
            letter1 = lst_of_alphabets[index-shiftNumber]
            new_type += letter1
         
        
    
    print(f"Decoded Message : {new_type}")
