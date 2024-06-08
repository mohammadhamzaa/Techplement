import random
import string
import argparse

def generate_password(length=10, uppercase=True, lowercase=True, digits=True,special=True):
    # Combine all selected character sets
    selected_chars = ''
    if uppercase:
        selected_chars += string.ascii_uppercase
    if lowercase:
        selected_chars += string.ascii_lowercase
    if digits:
        selected_chars += string.digits
    if special:
        selected_chars += string.punctuation

    # Generate the password
    password = ''.join(random.choice(selected_chars) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Random Password Generator")
    parser.add_argument('-length', '--length',type=int, default=10)
    parser.add_argument('-uppercase', '--uppercase', action='store_true')
    parser.add_argument('-lowercase', '--lowercase', action='store_true')
    parser.add_argument('-digits', '--digits', action='store_true')
    parser.add_argument('-special', '--special', action='store_true')
    
    args = parser.parse_args()

    # Check if at least one character type is selected
    if not (args.uppercase or args.lowercase or args.digits or args.special):
        print("At least one character set must be specified: 1> -uppercase,2> -lowercase, 3> -digits, 4> -special")
        return
    
    # Generate and print the password
    password = generate_password(
        length=args.length,
        uppercase=args.uppercase,
        lowercase=args.lowercase,
        digits=args.digits,
        special=args.special
    )
    print("Random Generated password ---->> ", password)

if __name__ == "__main__":
    main()
