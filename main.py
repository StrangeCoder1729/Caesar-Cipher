import alphabets
import caesar
import art

print(art.logo)

lst_of_alphabets = alphabets.lst_alphabet
 
direc = ['encode','decode']

def main():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt : ")
    direction = direction.lower()
    if direction not in direc:
        print("Please type a valid input !!")
        exit()
    type = input("Enter your message : ").lower()
    shiftNumber = int(input("Enter Shift number : "))
    caesar.caesar_transformation(type,shiftNumber,direction)


main()

try_again = True
while(try_again):
    again = input("Type 'yes' if you want to again. Otherwise type 'no' : ").lower()
    if again == 'yes': main()
    else : 
        print("Thanks for using !")
        print(art.dictator)
        break
    


 


