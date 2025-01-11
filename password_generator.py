import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    # Create a pool of characters based on user preferences
    character_pool = ''
    
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    # Ensure the pool is not empty
    if not character_pool:
        raise ValueError("At least one character type must be selected.")
    
    # Generate a random password
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

# Example usage
if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    password = generate_password(length=password_length)
    print(f"Generated Password: {password}")