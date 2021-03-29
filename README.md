# LT2222 V21 Assignment 3

Your name: Anna Page 

## Part 1

This function takes a file containing the data to be processed as it's input and reads is as 'q'. For each line in the input file it adds each character (including spaces, punctuation and new line characters) in the line to an empty list initialised as 'mm'. It then adds two start characters to the begining of the list and two end characters to the end of the list. Finally, the function returns two things as the tuple 'q': i) the full list of characters with start and end tags, and ii) a list containing the unique characters in the data

Function b:

Takes two arguments: u - the full list of characters, and p - the list of unique characters (the tuple output by a)

For each element in the list of all characters (given enough space on the sides to not be out of range (hence the addition of the start and end tokens)), when the current iteration (v+2) comes to a vowel, the code retrives the index of that vowel in the list of vowels and appends it to a list named 'gt', which is later turned into a numpy array. Next, the code considers the character at the present index (two before the vowel), the next item (one before the vowel) and the two items after the vowel (u[v+3] and u[v+4]). For each of these, the code makes a numpy array the lenghth of the ordered list of the set of characters and puts a 1 at the index of the relevent character. It then concatenates these four numpy arrays (vectors) into one single 1D numpy array. This long numpy array is then appended to the list gr. Finally, the list of numpy arrays is turned into a matrix where each row represents one of the numpy arrays in gr. Similarly, 'gt' (the list of vowel indices) is converted to a 1D numpy array.

Function g:

This function is used by function b. It receives two arguments: a character and the list of unique characters. It creates a numpy array equal in length to the length of the unique character list. It then sets the value of that array to 1 at the index of that character in the list of unique characters.

Argument k:

This is an optional argument with a default value of 200. It represents the number of nodes in the hidden layers of the model. 

Argument r:

This is an optional argument with a default value of 100. It represents the number of epochs in the model, which is the number of full training passes of the data that are used in the training. 

Argument m:

This is a required argument which constitutes the input file name. This file is loaded by a and is then processed by a and b into the input and target data which is then used to train a model.

Argument h:

This is a required argument and is used as the save path for the model which, once training has completed, dumps a pickle to this file path.

## Part 2

To run eval.py from the command line you need 3 arguments: the name of the file containing the testing data, the model, and the name of a file you want to write the re-written text to.

In this case you would call it like so:

python3 eval.py /home/xsayas@GU.GU.SE/scratch/lt2222-v21-resources/svtest.lower.txt output rewritten_test.txt

## Part 3

With no optional arguments I get accuracy scores between 13% and 40% when I run train.py on the training data and then eval.py on the testing data.

Trials with alterned size of hidden layers/epochs. 

1. Size of hidden layer: 5, epochs unchanged
Accuracy: 20.33%

2. Size of hidden layer: 100, epochs unchanged
Accuracy: 38.61%

3. Size of hidden layer: 300, epochs unchanged
Accuracy: 41.36%

4. Size of hidden layer: 400, epochs unchanged
Accuracy: 30.14%

5. Size of hidden layer: 500, epochs unchanged
Accuracy: 50.31%

6. Size of hidden layer unchanged, epochs: 5
Accuracy: 27.05%

7. Size of hidden layer unchanged, epochs: 50
Accuracy: 38.56%

8. Size of hidden layer unchanged, epochs: 150
Accuracy: 22.08%

9. Size of hidden layer unchanged, epochs: 200
Accuracy: 28.83%

10. Size of hidden layer unchanged, epochs: 250
Accuracy: 54.77%

Best of both (hidden layer: 500, epochs: 250): 
Accuracy: 27.61%

Using the best settings for each of the parameeters together did not improve the performance. This may be because of the random element in the model. This is also what will be responsible for the variation in performance. Even without changing the parameter settins, the model's performance in terms of accuracy differed up to about 25% in the trials that I ran. This makes it very difficult to say which changes to the parameter setting actually improved the performance, and when it just 'got lucky'. This could have been controlled for by adding a random seed to the train.py file, but that was out of the scope of the test I ran here. 

In general however, there does seeem to be a trend towards improved performance when the number of nodes in the hidden layers of the model are increased. The lack of perfect linearity is likely attribuatable to the random element of the model. Changing the number of epochs did not have as clear an effect on performance. There does seem to be some upward trend in improvement with increased epochs (the best performance was when there were 250), but there were also cases with 150 and 200 epochs where the accurracy was only 22.08% and 28.83% respectively, which is a worse performance than the apparent average. 

To get a clearer picture of the effect of altering the parameter settings  one would need to run lots of models with lots of different parameter settings to estimate the distribution of each of these. I.e. one would want to know what the average performance for a given parameter setting is. 

I have included a run of the model using the parameteer setting that gave the best results above, however, as I ran other trials since originally running it with this parameter setting, this time the performance has dropped to 44.27% accuracy. This is a lower score than before by about 10%, but it still higher than average compared to other trials with other parameter settings. 

## Bonuses

## Other notes
