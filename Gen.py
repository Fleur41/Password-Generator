'''
Password Generator
-------------------------------------------------------------
'''

import secrets
import string

def create_pw(pw_length = 12):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars