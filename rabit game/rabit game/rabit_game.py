lis_herbs=[["🍀","🍀","🍀"],["🍀","🍀","🍀"],["🍀","🍀","🍀"]]

print("welcome to place the rabit")
print(lis_herbs[0])
print(lis_herbs[1])
print(lis_herbs[2])

print("wher should rabit go? 🐇")
row_columan=input("please choose row and column")

row=int(row_columan[0])-1
columan=int(row_columan[1])-1
lis_herbs[row][columan]="🐇"

print(lis_herbs[0])
print(lis_herbs[1])
print(lis_herbs[2])


