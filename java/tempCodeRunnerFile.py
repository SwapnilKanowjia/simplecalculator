import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special=True):
    lowercase = string.ascii_lowercase