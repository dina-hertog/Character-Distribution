"""
distribution.py
Author: Dina
Credit: none

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
text = input("Please enter a string of text (the bigger the better):")
text = text.lower()
length = len(text)
letter = 0

while letter < length:
    b = text[letter]
    used = [letter]
    if b == used:
        letter = int(letter)+1
    else:
        a = text.count(b)
        print(a + b)
        letter = int(letter)+1

#b = text.count(text[1])
#print(b)
#c = text.count(text[2])
#print(c)







