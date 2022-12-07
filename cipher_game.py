from argparse import ArgumentParser
import re
import sys
# import whatever allows us to read user input
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
class Game:
    """
    Attributes: a list of Cipher objects. These Cipher objects will contain several strings detailing important parts of the game
    """
    words = list()
    def __init__(self, file):
        """This will take in a file path to a text file containing various sentences. 
        Each sentence will have a "key=x" at the end
        
        Side effects: reads lines from a file and uses them to create an instance of a Cipher object to add to a list.
        
        Args:
            file (String): a file path
        
        Returns: none
        """
        with open(file,"r",encoding = "utf-8") as f:
            for line in f:
                self.words.append(Cipher(line))
            
    def total_score():
        """This will take the average score from each of the Cipher objects and return that value
        
        Args:
            none
        
        Returns: the total score (int)
        """
        pass
    def play():
        """Loop through the list. For each Cipher object, display the encrypted string 
            and prompt the user to try and write the original string. 
            The score for each guess will be displayed after the input (displayed as a percent score out of 100)
            it will calculate score at the end using each cipher object's individual set_score methods
        
        Side effects: loops through the list and displays things for user input
        
        Args: none
        
        Returns: none
        """
        
        
        
class Cipher:
    """
    Attributes:
        answer (String): A string containing the original string without the "key=x", an encrypted version of the string
        encryption (String): the encrypted String
        key (int): this contains the amount to shift the original string.
        score (int): displayed as a percentage
    """
    def __init__(self, line):
        """ Because each string is assumed to end with a "key=x" at the end, those will be separated at the beginning
            initialize answer based on that. Take 
        
        Side effects: initializes the answer string and a int object for the key to encrypt the string
        
        runs the encrypt method to initialize the encrypted string
        """
        self.answer = re.search(r"(.+)Key=\b([1-9]|1[0-9]|2[0-6])\b", line).group(1)
        self.key = re.search(r"(.+)Key=\b([1-9]|1[0-9]|2[0-6])\b", line).group(2)
        self.encryption = ""
        self.score = 0.0
        
    def encrypt(self):
        """ an encryption method that takes the key int  and shifts the answer string
        
        Side effects: initializes the encrypted string using the key.
        """
        case = 0
        for character in range(0, len(self.answer)):
            if self.answer.index(character).islower():
                case = 1
                
            original = ALPHABET[self.answer.index(character)] 
            shift = original - self.key
            if self.key < 0:
                shift += 26
            
            self.encryption += POSITION[shift][case]
            
    def set_score(self, answer):
        """ Reads in the player's score and returns the percentage they got correct rounded down and displayed as an int
        
        Args: 
            answer (String): the player's input
        Side effects: 
            initializes score
        Returns:
            none
        """
        attempt = 0
        total = len(self.answer)
        if len(self.answer) != len(answer):
            self.score = 0
            print("incorrect length")

        for character in range(0, len(answer)):
            if self.answer.lower().index(character) == answer.lower().index(character):
                attempt += 1
        self.score = (attempt/total) * 100

def main(file):
    """
    
    Side effects: instantiates the Game object, which instantiates a list of Cipher objects
                    run the object's play() method

    Args: file (String): the filepath
            
    """
    with open(file,"r",encoding = "utf-8") as f:
         game = Game(file)
         game.play()
         
       
            
    print("")
                


def parse_args(arglist):
    """Parse command line arguments.
    
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
