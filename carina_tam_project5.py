#Carina Tam and Kinza Ali Project 5 Part 1
print("This program will print a diamond shaped array of a word")
x=input("Enter a 1-10-letter word: ")
y=len(x)
if(len(x)>10): #if length of the string is more than 10, only include the first 10 letters
    y=10
for i in range(0,y):#prints first half of diamond
    for j in range (y-1, i, -1):#number of spaces depends on the number of letters printed
        print(" ", end="")
    for k in range(0,i+1):#prints left half of top diamond
        print(x[k],end="")
    for l in range(k-1,-1,-1):#prints right half of top diamond
        print(x[l],end="")
    print()

for m in range(y-1,0,-1):#prints bottom half of diamond, -1 because it is decreasing
    for n in range (y,m,-1):#number of spaces depends on how long the input is
        print(" ", end="")
    for o in range(0,m): #prints left bottom half of diamond
        print(x[o],end="")
    for p in range(o-1,-1,-1):#prints right bottom half of diamond
        print(x[p],end="")
    print()
#when the last letter is printed, it exits the program
