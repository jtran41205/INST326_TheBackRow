##### INST326_TheBackRow
### Our final project


# This project is a guessing game. Here's how it works:

1) Read in a text file with many lines of strings. Each line will end with "Key=x"
   where Key determines how the string will be shifted.
   We will create a list of dictionaries to hold the original text, the altered text,
   the letter shift amount, and the shift direction. Each line will be read and added
   into this list.

2) The program will use the key 'x' as a cipher to shift the letters of the string
   accordingly.

   For example:

   String in file: "Fire! Key=3"
   The string will be read into the game as "Fire!"
   The key will be "3", which will shift the characters 3 to the left
   altered string: "Cfob!"

3) The user will be prompted to type a string to try and match the original text. 
   Due to high margins of error, they'll be graded on a percentage of how much
   they typed correctly, rather than a binary right or wrong.

4) This process will repeat until all strings have been guessed. The program will
   then grade the user based on the average percentage of each string they have
   correctly deciphered.


important links to read:

1. https://en.wikipedia.org/wiki/ROT13

2. https://en.wikipedia.org/wiki/Caesar_cipher

#### Overview of each Class and their methods:

### Cipher() class

## Attributes

- answer: A string that contains the answer the user must guess

- encryption: the answer string, encrypted and shown to the user

- key: the number of characters to shift the string

- score: the percent of the string the user has guessed correctly

## Methods

- \_\_init\_\_(): takes in a string. Each string will have a "Key=x" at the end, where x is some number
   everything BEFORE Key= will be saved into answer. Everything AFTER Key= will be saved to key as an int
   encryption is initialized as an empty string. This is important for the encrypt() method.


score is initialized to 0

- encrypt(): takes in no arguments. It's called as part of the init method
   for each character in the answer string, it checks if the character is an alphabetical character. 
   If the character is NOT an alphabetical character, it is added to encryption as normal.
   
   If yes, it will use that character and the key to find the shifted version, and add that new letter to encryption

- set_score(): takes in an outside answer string as an argument
   If outside answer is not the same length as self.answer, score is zero and print "incorrect length"
   (Yes this is punishing, check the grammar closely)
   
   This is a running total problem. Iterate through each character. If outside answer at that index is equal to self.answer at that index, add a point. The score will equal (total points/string length)*100



### Game() class

## Attributes

- lines: A list of Cipher objects. These represent different strings and their associated keys to encrypt the string

## Methods

- \_\_init\_\_(): this reads in a file path. Each line will be used to create an individual Cipher object, and add it to the list.

- total_score(): this will iterate through self.lines. Takes no arguments. This adds every score from each cipher object,
   and divides it by the number of cipher objects in the list. This is the total score that is returned.

### How to run the program

- This program runs from the command line. It takes a single argument, a filepath
   ```
   python cipher_game.py demo.txt
   ```
   This program has multiple demo files, 
   because it can take a very long time to figure out a single question,
   especially depending on the length of the string and the size of the key
