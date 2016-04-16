# Demo
# Alphabets and their relative Morse Symbols
# Assigning all this in a Python Dictionary : Code_Symbol
Code_Symbol = {'A': '.-', 'B': '-...', 'C': '-.-.', 
 'D': '-..', 'E': '.', 'F': '..-.',
 'G': '--.', 'H': '....', 'I': '..',
 'J': '.---', 'K': '-.-', 'L': '.-..',
 'M': '--', 'N': '-.', 'O': '---',
 'P': '.--.', 'Q': '--.-', 'R': '.-.',
 'S': '...', 'T': '-', 'U': '..-',
 'V': '...-', 'W': '.--', 'X': '-..-',
 'Y': '-.--', 'Z': '--..',
 
 '0': '-----', '1': '.----', '2': '..---',
 '3': '...--', '4': '....-', '5': '.....',
 '6': '-....', '7': '--...', '8': '---..',
 '9': '----.' 
 }
 
 # A main function 
# Taking USER Input as : input_msg
def main():
  input_msg = raw_input('Enter your Message: ')
# Reading input message
# Converting and Printing accordingly
  for char in input_msg:
    print (Code_Symbol[char.upper()]),
# The Condition
# Calling the main function 
    if __name__ == "__main__":
    main()
