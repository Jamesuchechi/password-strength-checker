import string

def check_password_strength(password):
    strength = 0
    errors = []


    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")
        strength += 1
        
    if not any(char.isdigit() for char in password):
        strength += 1
    else:
        errors.append("Password must contain at least one digit.")
    if any(char.islower() for char in password):
        strength += 1
    else:
        errors.append("Password must contain at least one lowercase letter.")
    if any(char.isupper() for char in password):
        strength += 1
    else:
        errors.append("Password must contain at least one uppercase letter.")
    if any(char in string.punctuation for char in password):
        strength += 1
    else:
        errors.append("Password must contain at least one special character.")

    if strength == 5:
        print("Password is strong.")
    elif strength >= 3:
        print("Password is medium.")
    else:
        print("Password is weak. Please consider using a stronger password.")

def main():
    print("Welcome to the password strength checker!")
    print("Please enter your password:")
    while True:
        password = input("Password: ")
        result = check_password_strength(password)
        if isinstance(result, tuple):
            print(result[0])
            print("suggestions:")
            for error in result[1]:
                print(f"* {error}")
        else:
            print(result)
            cont = input("Do you want to check another password? (yes/no): ")
            if cont.lower() != "yes":
                break

if __name__ == "__main__":
    main()
