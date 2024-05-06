import string
import random

print("welocme to the password Generator!")

total_char=int(input("Enter the total Number of characters in the pssword:"))
numbers=int(input("Enter the namber of numbers in the password: "))
letters=int(input("Enter the namber of letters in teh password: "))
symbols=int(input("Enter the number of symbols in the password:"))

digits=string.digits
letter=string.ascii_letters
punctuation=string.punctuation

if (numbers+letters+symbols)==total_char:
    
    password_chars=(random.choices(digits,k=numbers)+
    random.choices(letter,k=letters)+
    random.choices(punctuation,k=symbols))
    

    random.shuffle(password_chars)
    password="".join(password_chars)
    print(f"your password is {password}")  
else:
    print("invled choice")

    




