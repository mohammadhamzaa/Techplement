# Documentation

## Project: Random Password Generator
This Python script is a command-line tool for generating random passwords with customizable length. Users can specify password requirements such as including uppercase letters,lowercase letters, digits,and special characters. The application ensures that the generated passwords are secure and random,making them resistant to brute-force attacks and guessing.

### Features:
1> Customizable password length.
2> Option to include uppercase letters, lowercase letters, digits, and special characters.
3> Ensures that at least one character from each selected set is included in the password.
4> Simple and easy-to-use command-line interface.

### How to Run
step 1> Save the script in a file --- >>  random_password_generator.py.
step 2> Open your terminal (or command prompt).
step 3> Navigate to the directory where the script is saved.
step 4> Run the script with the desired options.


#### Step 1
##### Python Code file ( eg. random_password_generator.py )

```
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

```

#### Step 2 
 Open your terminal (or command prompt).
#### Step 3
 Navigate to the directory where the script is saved.
#### Step 4
 Run the script with the desired options. For example:
 `python random_password_generator.py -length 8 -uppercase -lowercase -digits -special `


 This will generate a secure, random password according to the specified options.


#### For Examples:

1> Generate a password of length 13 including UpperCase letters and digits only:
   ` python random_password_generator.py -length 13 -uppercase -digits `

2> Generate a password with default length 10 including lowercase letters  :
   ` python random_password_generator.py -lowercase   ` 


