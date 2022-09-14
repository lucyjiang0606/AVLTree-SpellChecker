#!/usr/local/bin/python3

# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.

# Lucy Jiang

import cgi, cgitb
cgitb.enable()
from avl_tree import AVLTreeMap

print("Content-type: text/html\n")

aform = cgi.FieldStorage()
text = aform.getvalue('textbox')

# read in professor's dictionary
dict = open("/home/staff/kurban/public/lists/web2.txt")
dict_words = dict.read().split("\n")
dict.close()
avl_dict = AVLTreeMap()

# populate the AVL tree
for i in range(len(dict_words)):
    # i just made both the key and the value the word in the dictionary because i don't need two different things
    # this was my original code, but it felt weird calling __setitem__ directly even though it works
    # avl_dict.__setitem__(dict_words[i].lower(), dict_words[i].lower())
    # technically called __setitem__ for binary_search_tree here, but since it's a magic method, this syntax works
    avl_dict[dict_words[i].lower()] = dict_words[i].lower()

# turn the user's text into a list of words
text_words = text.split()
# this list will be populated with misspelled words in the next step
misspelled = []
# loop through user's list of words
for i in range(len(text_words)):
    # for each word, check to see if it is in the AVl dictionary
    lower_word = text_words[i].lower()
    # similar as above, I technically called __getitem__ here, but since it's a magic method, this syntax works
    dict_search = avl_dict[lower_word]
    # I added the __getitem__ method from binary_search_tree to avl_tree and edited it to fit my needs for the project (deeper explanation in the analysis)
    # if after calling __getitem__, the key doesn't exist in the dictionary and the method returns none, append the word to misspelled
    if (dict_search == None):
        misspelled.append(text_words[i])
if len(misspelled) == 0:
    print("None of the words are misspelled.")
else:
    print("Here are the list of misspelled words.<br>")
    print(misspelled)

