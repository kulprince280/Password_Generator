import random
import string

def generate_password(length):
    if length < 6:
        print("Password length should be at least 6 characters.")
        return None

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        password = generate_password(length)
        if password:
            print(f"Generated password: {password}")
    except ValueError:
        print("Please enter a valid number.")