# INST326_TheBackRow
Our final project


This project is a guessing game. Here's how it works:

1) Read in a text file with many lines of strings. Each line will end with "Key=x"
   where Key determines how the string will be shifted.
   We will create a list of dictionaries to hold the original text, the altered text,
   the letter shift amount, and the shift direction. Each line will be read and added
   into this list.

2) The program will use the key 'x' as a cipher to shift the letters of the string
   accordingly.

   For example:

   String in file: "Fire! Key=3"
   The string will be read into the game as "These Nuts!"
   The key will be "3", which will shift the characters 3 to the left
   altered string: "Cfob!"

3) The user will be prompted to type a string to try and match the original text
   Due to high margins of error, they'll be graded on a percentage of how much
   they typed correctly, rather than a binary right or wrong.

4) This process will repeat until all strings have been guessed. The program will
   then grade the user based on the average percentage of each string they have
   correctly deciphered.

This could probably have an easier explanation, so let me know if I need to clarify anything

important links to read:
https://en.wikipedia.org/wiki/ROT13
https://en.wikipedia.org/wiki/Caesar_cipher
