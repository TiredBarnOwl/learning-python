# define a function to convert temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# define a function to convert temperature from Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# use a while loop to keep the program running until the user quits
while True:
    # print menu options
    print("\nPlease select an option:")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Quit the program")

    # get user input for choice
    choice = input("> ")

    # if choice is 1, convert temperature from Celsius to Fahrenheit
    if choice == "1":
        # get user input for temperature in Celsius
        celsius = float(input("Enter temperature in Celsius: "))
        # call the celsius_to_fahrenheit function to perform the conversion
        fahrenheit = celsius_to_fahrenheit(celsius)
        # print the result
        print(f"{celsius} degrees Celsius is {fahrenheit} degrees Fahrenheit.")

    # if choice is 2, convert temperature from Fahrenheit to Celsius
    elif choice == "2":
        # get user input for temperature in Fahrenheit
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        # call the fahrenheit_to_celsius function to perform the conversion
        celsius = fahrenheit_to_celsius(fahrenheit)
        # print the result
        print(f"{fahrenheit} degrees Fahrenheit is {celsius} degrees Celsius.")

    # if choice is 3, quit the program
    elif choice == "3":
        print("Goodbye!")
        break

    # if choice is invalid, prompt user to select again
    else:
        print("Invalid choice. Please select again.")
