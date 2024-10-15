import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special=True):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    special = string.punctuation if use_special else ''
    all_characters = lowercase + uppercase + numbers + special
    if use_uppercase:
        all_characters += random.choice(uppercase)
    if use_numbers:
        all_characters += random.choice(numbers)
    if use_special:
        all_characters += random.choice(special)
    password = ''.join(random.choices(all_characters, k=length - len(all_characters)))
    password += ''.join(random.sample(all_characters, k=len(all_characters)))  

    return ''.join(random.sample(password, len(password)))  

def main():
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    password = generate_password(length, use_uppercase, use_numbers, use_special)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
