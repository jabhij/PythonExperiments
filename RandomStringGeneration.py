# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 19:24:38 2016

@author: abhi
"""

""" Method1 """

# Import UUID
import uuid

# Decalaring a Function
def random_string(string_len):
    
    # Convert UUID format to a Python string.
    random = str(uuid.uuid4()) 
    # Converting characters to UpperCase
    random = random.upper()
    # random = random.replace("-","")
    # Return the random string.
    return random[0:string_len] 

print (random_string(6))

#-----------------------------------------------------

""" Method2 """

# Import random and string 
import random
import string

# Converting characters to UpperCase plus adding digits
char = (string.ascii_uppercase + string.digits)

# Using JOIN functionality to combine Char and Digits
print (''.join(random.sample(char*6, 6)))

#-----------------------------------------------------

""" Method 3 """

# Combining Functionality of Method 1 and 2
# Imoprt urandom, islice, imap, repeat, string
from os import urandom
from itertools import islice, imap, repeat
import string

# Decalaring a Function
def random_string(string_len):
    
    # Converting characters to UpperCase plus adding digits
    char = set(string.ascii_uppercase + string.digits)
    char_gen = (c for c in imap(urandom, repeat(1)) if c in char)
    
    # Using JOIN functionality to combine Char and Digits
    return ''.join(islice(char_gen, None, string_len))

print (random_string(6))

#-----------------------------------------------------

""" Method 4 """

# Import string, choice
from random import choice
import string

# Converting characters to UpperCase plus adding digits
string_length = ascii_uppercase + string.digits

# Using JOIN functionality to combine Char and Digits
print (''.join(choice(string_length) for char in range(6)))
