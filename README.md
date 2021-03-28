# LT2222 V21 Assignment 3

Your name: Anna Page 

## Part 1

Function a:

f = input file (data to be processed)
l = a line of the data in the input file
[c for c in l] = adds characters in line to mm (a list of every character, including spaces and new line characters)
adds two start and two end tags to the list
returns the full list of characters as well as a list of the unique characters as a tuple which is assigned to q

Function b:

Takes two arguments: u - the full list of characters, and p - the list of unique characters (the tuple output by a)

For each element in the list of all characters (given enough space on the sides to not be out of range (hence the addition of the start and end tokens)), when the current iteration (v+2) comes to a vowel, the code retrives the index of that vowel in the list of vowels and appends it to a list named 'gt', which is later turned into a numpy array. Next, the code considers the character at the present index (two before the vowel), the next item (one before the vowel) and the two items after the vowel (u[v+3] and u[v+4]). For each of these, the code makes a numpy array the lenghth of the ordered list of the set of characters and puts a 1 at the index of the relevent character. It then concatenates these four numpy arrays (vectors) into one single 1D numpy array. This long numpy array is then appended to the list gr. Finally, the list of numpy arrays is turned into a matrix where each row represents one of the numpy arrays in gr. Similarly, 'gt' (the list of vowel indices) is converted to a 1D numpy array.

Function g:

This function is used by function b. It receives two arguments: a character and the list of unique characters. It creates a numpy array equal in length to the length of the unique character list. It then sets the value of that array to 1 at the index of that character in the list of unique characters.

Argument k:

This is an optional argument with a default value of 200. It represents the number of nodes in the hidden layers of the model. 

Argument r:

This is an optional argument with a default value of 100. It represeents the number of epochs in the model, which is the number of full training passes of the data that are used in the training. 

Argument m:

This is a required argument which constitutes the input file name. This file is loaded by a and is then processed by a and b into the input and target data which is then used to train a model.

Argument h:

This is a required argument and is used as the save path for the model which, once training has completed, dumps a pickle to this file path.

## Part 2

## Part 3

## Bonuses

## Other notes
