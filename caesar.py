import alphabets
lst_of_alphabets = alphabets.lst_alphabet

def caesar_transformation(type,shiftNumber,direction):
    shifting = shiftNumber % 26
    new_type = ""
    for letter in type:
            
        if ((letter >= 'a' and letter <= 'z' ) or (letter >= 'A' and letter <= 'Z')):
            index = lst_of_alphabets.index(letter)
             
            if direction == "encode":
                 
                letter1 = lst_of_alphabets[index+shifting]
                new_type += letter1
            elif direction == "decode":
                letter1 = lst_of_alphabets[index-shifting]
                new_type += letter1            
        else :
            new_type +=letter
    print(f"{direction} Message : {new_type}")
    
    
