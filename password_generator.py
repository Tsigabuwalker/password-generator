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

    # Generate a password ensuring at least one of each selected type
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))

    # Fill the rest of the password length with random choices
    password += random.choices(character_pool, k=length - len(password))
    
    # Shuffle the password to ensure randomness
    random.shuffle(password)
    
    return ''.join(password)

def save_password(password, filename='passwords.txt'):
    with open(filename, 'a') as file:
        file.write(password + '\n')
    print(f"Password saved to {filename}")

# Example usage
if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    num_passwords = int(input("How many passwords would you like to generate? "))
    
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    for _ in range(num_passwords):
        password = generate_password(length=password_length, use_upper=use_upper, 
                                      use_lower=use_lower, use_digits=use_digits, 
                                      use_special=use_special)
        print(f"Generated Password: {password}")
        
        save_option = input("Would you like to save this password? (y/n): ").lower()
        if save_option == 'y':
            save_password(password)