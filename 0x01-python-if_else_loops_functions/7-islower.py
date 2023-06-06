#!/usr/bin/python3

def islower(c):
        if len(c) != 1:
            raise ValueError("Input must be a single character")        
# Check if the ASCII value of the character is within the range of lowercase letters
        if ord(c) >= 97 and ord(c) <= 122:
            return True
        else:
            return False
