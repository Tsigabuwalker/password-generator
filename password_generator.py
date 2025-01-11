import random
import string
import mysql.connector
from mysql.connector import Error

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

def save_password_to_db(password, cursor):
    try:
        cursor.execute("INSERT INTO passwords (password) VALUES (%s)", (password,))
        print("Password saved to database.")
    except Error as e:
        print(f"Error occurred: {e}")

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',  # Change if your DB is hosted elsewhere
            database='your_database_name',  # Replace with your database name
            user='your_username',  # Replace with your MySQL username
            password='your_password'  # Replace with your MySQL password
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Example usage
if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    num_passwords = int(input("How many passwords would you like to generate? "))
    
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    # Connect to the database
    connection = connect_to_database()
    if connection is not None:
        cursor = connection.cursor()

        for _ in range(num_passwords):
            password = generate_password(length=password_length, use_upper=use_upper, 
                                          use_lower=use_lower, use_digits=use_digits, 
                                          use_special=use_special)
            print(f"Generated Password: {password}")
            
            save_option = input("Would you like to save this password to the database? (y/n): ").lower()
            if save_option == 'y':
                save_password_to_db(password, cursor)

        # Commit the transaction
        connection.commit()
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")