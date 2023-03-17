# Python Password Generator

This program generates a strong password of a specified length using random characters from a given set of characters.

## Getting Started

To use this program, simply run the `password_generator.py` file in a Python environment. The program will prompt the user to enter a length for the password they want to generate, as well as a set of characters to use in generating the password. If no set of characters is specified, the program will use a default set of characters.

## How it Works

The `password_generator.py` file defines a function called `generate_password()` that takes two arguments: `length` and `chars`. The `length` argument is an integer specifying the length of the password to generate, and `chars` is a string specifying the set of characters to use in generating the password.

The function first imports the `random` module, which is used to generate random characters. It then initializes an empty string called `password`, which will be used to store the generated password.

Next, the function generates a random character from the set of characters specified by the `chars` argument for each character in the password length specified by the `length` argument. The `join()` method is used to combine the characters into a single string, which is returned as the generated password.

If no `chars` argument is provided, the function uses a default set of characters that includes uppercase and lowercase letters, digits, and symbols.

## Future Improvements

Some potential improvements to this program could include:

- Adding options to generate passwords with specific requirements (e.g. minimum number of uppercase letters, minimum number of digits, etc.)
- Creating a user interface to make it easier to generate passwords without using the command line interface.
- Adding options to save generated passwords to a file or copy them to the clipboard.

## Authors

TiredBarnOwl

## License

This project is licensed under the MIT License


