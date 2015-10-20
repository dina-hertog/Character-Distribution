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
print("The distribution of characters in " + text + " is:")
text = text.lower()
length = len(text)
letter = 0
used = []
dis = []

while letter < length:
    b = text[letter]
    letter = letter+1
    if not( b in used or b == ' ' or b == '-' or b == '.' or b== ','):
        #a= text.count(b)
        #while a > 0:
            #print(b)
            #a = a+1
        dis.append(text.count(b))
        used.append(b)
        
c = list(zip(dis,used))
c.sort()
c = c[::-1]

for l in c:
    if l[0] == l[-1]:
        c.sort()
        print(l[1]*l[0])
    #elif l[o] == l[-1]-1:


