library=[]
wish_list=[]


own_book1=input("Enter the name of a book you own")
own_book2=input("Enter the name of another book you own(or press 'Enter'to skip):")
library.append(own_book1)
if own_book2:
    library.append(own_book2)    
print(f"your library:{library}")


wish_book1=input("Enter the name of a book you wish to have in the future:")
wish_book2=input("Enter the name of another book you wish to have( or press enter to skipe)")
wish_list.append(wish_book1)
if wish_book2:
    wish_list.append(wish_book2)    
print(f"now your wishlist:{wish_list}")


wish_quired=input("Enter the name of a book from your wihslist that you've already got it (or press enter to skip)")
if wish_quired in wish_list:
    wish_list.remove(wish_quired)
    library.append(wish_quired)
       
print(f"your library is{library}")
print(f"your wish list is {wish_list}")

      
donate=input("enter the book of your library you want to donate (or press enter to skip)")
if donate in library:
    library.remove(donate)
    

    
print(f"your library in the finaly is {library}")