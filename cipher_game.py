from argparse import ArgumentParser
import sys
# import whatever allows us to read user input

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
                 line.split("\t")
            
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
        key (dict): this contains the direction and amount to shift the original string.
        score (int)
    """
    def __init__(self, line):
        """ Because each string is assumed to end with a "key=x" at the end, those will be separated at the beginning
            initialize answer based on that. Take 
        
        Side effects: initializes the answer string and a dictionary object for the key to encrypt the string
        
        runs the encrypt method to initialize the encrypted string
        """
        pass
    def encrypt(self, answer, key):
        """ an encryption method that takes the key dictionary object and shifts the answer string
        
        Side effects: initializes the encryption string using the key.
        """
        pass
    def set_score(self, answer):
        """ Reads in the player's score and returns the percentage they got correct rounded down and displayed as an int
        
        Args: 
            answer (String): the player's input
        Side effects: 
            initializes score
        Returns:
            none
        """
 
def main(file):
    """
    
    Side effects: instantiates the Game object, which instantiates a list of Cipher objects
                    run the object's play() method

    Args: file (String): the filepath
            
    """
    with open(file,"r",encoding = "utf-8") as f:
         for line in f:
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
