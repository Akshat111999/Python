import random

wordsarray=[]  #empty array
print("Please enter the words\n")
for i in range(0,15):
    word=input()
    wordsarray.append(word)  #appending user input into the array

random.shuffle(wordsarray) # for giving the random order to the array

wordsarray.sort() # sorting the array in alphabetical order

print("\nSorted words in alphabetical order")
# printing array elements on new line using sep.
print(*wordsarray, sep = "\n")

#Output
'''
happy
you
a
jack
queen
set
map
lion
king
trade
no
long
integer
mouse
laptop

Sorted words in alphabetical order
a
happy
integer
jack
king
laptop
lion
long
map
mouse
no
queen
set
trade
you
'''
