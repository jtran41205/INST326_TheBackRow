"""A guessing game which is based on the Caesar Cipher."""

from argparse import ArgumentParser
import re
import sys

# Dictionaries
# POSITION and ALPHABET built by Jill
# HINTS built by Kassian

# each letter of the alphabet has an index. Accounts for upper/lowercase
POSITION = {
    0: ["A","a"],
    1: ["B","b"],
    2: ["C","c"],
    3: ["D","d"],
    4: ["E","e"],
    5: ["F","f"],
    6: ["G","g"],
    7: ["H","h"],
    8: ["I","i"],
    9: ["J","j"],
    10: ["K","k"],
    11: ["L","l"],
    12: ["M","m"],
    13: ["N","n"],
    14: ["O","o"],
    15: ["P","p"],
    16: ["Q","q"],
    17: ["R","r"],
    18: ["S","s"],
    19: ["T","t"],
    20: ["U","u"],
    21: ["V","v"],
    22: ["W","w"],
    23: ["X","x"],
    24: ["Y","y"],
    25: ["Z","z"]
}

# Each letter of the alphabet (upper and lower case) corresponds to an index
ALPHABET = {
    "A": 0, "a": 0,
    "B": 1, "b": 1,
    "C": 2, "c": 2,
    "D": 3, "d": 3,
    "E": 4, "e": 4,
    "F": 5, "f": 5,
    "G": 6, "g": 6,
    "H": 7, "h": 7,
    "I": 8, "i": 8,
    "J": 9, "j": 9,
    "K": 10, "k": 10,
    "L": 11, "l": 11,
    "M": 12, "m": 12,
    "N": 13, "n": 13,
    "O": 14, "o": 14,
    "P": 15, "p": 15,
    "Q": 16, "q": 16,
    "R": 17, "r": 17,
    "S": 18, "s": 18,
    "T": 19, "t": 19,
    "U": 20, "u": 20,
    "V": 21, "v": 21,
    "W": 22, "w": 22,
    "X": 23, "x": 23,
    "Y": 24, "y": 24,
    "Z": 25, "z": 25
}

# This provides a hint to to the key used to shift the original string
HINTS = {
    1: "6 - 5 = ?",
    2: "3 - 1 = ?",
    3: "9 - 6 = ?",
    4: "8 - 4 = ?",
    5: "10 - 5 = ?",
    6: "12 - 6 = ?",
    7: "8 - 1 = ?",
    8: "16 - 8 = ?",
    9: "5 + 4 = ?",
    10: "7 + 3 = ?",
    11: "3 + 8 = ?",
    12: "6 + 6 = ?",
    13: "8 + 5 = ?",
    14: "7 + 7 = ?",
    15: "10 + 5 = ?",
    16: "5 + 11 = ?",
    17: "10 + 7 = ?",
    18: "9 + 9 = ?",
    19: "6 + 13 = ?",
    20: "10 + 10 = ?",
    21: "13 + 8 = ?",
    22: "11 + 11 = ?",
    23: "13 + 10 = ?",
    24: "12 + 12 = ?",
    25: "10 + 15 = ?",
    26: "13 + 13 = ?"
}

class Game:
    """
    Creating a Game class to keep track of all the game instances.
    
    Attributes: a list of Cipher objects. These Cipher objects will contain several strings detailing important parts of the game
    """
    lines = list()
    def __init__(self, file):
        """
        Author: Kassian
        
        Kassian demonstrated use of with statements.
        
        This will take in a file path to a text file containing various sentences. 
        Each sentence will have a "key=x" at the end
        
        Side effects: reads lines from a file and uses them to create an instance of a Cipher object to add to a list.
        
        Args:
            file (String): a file path
        
        Returns: none
        """
        with open(file,"r",encoding = "utf-8") as f:
            for line in f:
                self.lines.append(Cipher(line))
            
    def total_score(self):
        """
        Author: Prince
        
        I demonstrated the total score.
        
        This will take the average score from each of the Cipher objects and return that value
        
        Args:
            none
        
        Returns: the total score (float)
        """
        scores = list()
        for x in self.lines:
            scores.append(x.score) 
        total = sum(scores)/len(scores) 
        return total
        
        # iterate through self.lines
        # take the total score of every cipher object in self.lines
        # divide it by the number of terms in the list 
    
    def play(self):
        """
        Author: Kassian
        Kassian demonstrated use of for loops and f-strings
                
        Loop through the list. For each Cipher object, display the encrypted string 
            and prompt the user to try and write the original string. 
            The score for each guess will be displayed after the input (displayed as a percent score out of 100)
            it will calculate score at the end using each cipher object's individual set_score methods
        
        Side effects: loops through the list and displays things for user input
        
        Args: none
        
        Returns: none
        """
        
        # for each cipher object in self.lines, print the ENCRYPTED string
        # print the hint associated with that cipher object's key
        # prompt the user for input
        # take the user input, and run the current cipher object's set_score method
        for x in self.lines:
            print (f"Encrypted string: {x.encryption}")
            print (f"Hint: {HINTS[x.key]}")
            user_input = input("Enter your answer: ")
            x.set_score(user_input)
            print ("--------------")
        
        
    def demo(self):
        """
        Author: Jill
        this is a method that exists purely to demo the project as presentation. 
        It exists for archival, but has no bearing on the final project
        """
        for line in self.lines:
            print(line.encryption)
    def cipher_sort(self, length = 10):
        """
        Author: Kobe
        Demonstrates use of list sorting and optional parameters and use of keyword arguments
        
        Removes cipher objects from the list whose lengths are less than the given amount.
        Sorts each cipher in order of length
        """        
        pass
        
        
class Cipher:
    """
    Attributes:
        answer (String): A string containing the original string without the "key=x", an encrypted version of the string
        encryption (String): the encrypted String
        key (int): this contains the amount to shift the original string.
        score (float): displayed as a percentage
    """
    def __init__(self, line):
        """ 
        Author: Jill, Prince
        Jill set up the basic structure of the program
        Prince demonstrated knowledge of regular expressions
        Prince helped Jill in person, so Jill's commits contains knowledge from Prince.
        
        Because each string is assumed to end with a "key=x" at the end, those will be separated at the beginning
            initialize answer based on that. Take 
        
        Side effects: initializes the answer string and a int object for the key to encrypt the string
        
        runs the encrypt method to initialize the encrypted string
        """
        # save the string up to the "Key=" part of the string as the answer
        self.answer = re.search(r"(.+)Key=\b([1-9]|1[0-9]|2[0-6])\b", line).group(1)
        # save the number at the end as an int
        temp = re.search(r"(.+)Key=\b([1-9]|1[0-9]|2[0-6])\b", line).group(2)
        self.key = int(temp)
        # this is built upon later as part of the encrypt method
        self.encryption = ""
        self.encrypt()
        self.score = 0.0
        
    def encrypt(self):
        """
        Author: Jill
        Assistance: Prince
        Jill demonstrated sequence unpacking for the purposes of the cipher
        Prince demonstrated proper use of conditional expressions in person.
        
        an encryption method that takes the key int  and shifts the answer string
        
        Side effects: initializes the encrypted string using the key.
        
        Returns: none
        """
        #loop through the entire string of the answer
        for character in range(0, len(self.answer)):
            #This is a check to match the case of the original string to the encryption
            case = 0
            if self.answer[character].islower() == True:
                case = 1
                
            #check if the character is alphabetical before doing encryption
            #shifts characters to the left. If the position ends up negative, add 26 as a means of looping around the alphabet
            if self.answer[character].isalpha() == True:
                original = ALPHABET[self.answer[character]] 
                shift = original - self.key
                if shift < 0:
                    shift += 26
            
                self.encryption += POSITION[shift][case]
            # non alphabetical characters do not need to be shifted    
            else:
                self.encryption += self.answer[character]
            
    def set_score(self, answer):
        """
        Author: Jill
        Assitance: Prince assisted Jill with conditional expressions
        Prince fixed logical and type errors in Jill's code. 
        Jill created the skeleton and Prince fleshed it out
        
        Reads in the player's score and returns the percentage they got correct rounded down and displayed as an int
        
        Args: 
            answer (String): the player's input
        Side effects: 
            initializes score
        Returns:
            none
        """
        #checks the number of characters entered
        attempt = 0
        temp = str(answer)
        total = len(self.answer)
        #if the user does not enter the correct length, they did not get it correct
        if len(self.answer) != len(temp):
            self.score = 0
            print("incorrect length")
        #for each character the user got correct, add 1 to attempt
        else:
            for character in range(0, len(temp)):
                if self.answer[character].lower() == temp[character].lower():
                    attempt += 1
            # displayed as a percentage
            self.score = (attempt/total) * 100

def main(file):
    """
    Author: Kassian
    Assistnce: Prince assisted with fixing the main method
    Kassian demonstrated f-strings.
    Jill fixed a rounding error
    
    Side effects: instantiates the Game object, which instantiates a list of Cipher objects
                    run the object's play() method

    Args: file (String): the filepath
            
    """
    game = Game(file)
    game.play()
    total = game.total_score()
    rounded_total = round(total, 1)
    print (f"The total score is {rounded_total}. Thanks for playing!")
    
                


def parse_args(arglist):
    """
    Author:Jill
    Demonstrated use of ArgumentParser to read in a file as an input.
    
    Parse command line arguments.
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.

    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file containing strings to encrypt, for the player to decipher")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)
