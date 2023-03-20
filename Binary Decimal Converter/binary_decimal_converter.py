def binary_to_decimal(binary):
    """
    Converts binary number to decimal.

    Args:
        binary (str): A binary number represented as a string.

    Returns:
        int: The decimal representation of the binary number.
    """
    decimal = 0
    power = len(binary) - 1  # set the power of 2 to start at the rightmost bit

    # loop through each bit in the binary number
    for bit in binary:
        if bit == "1":
            decimal += 2**power  # if bit is 1, add 2^power to decimal
        power -= 1  # decrement the power of 2

    return decimal


def decimal_to_binary(decimal):
    """
    Converts decimal number to binary.

    Args:
        decimal (int): A decimal number.

    Returns:
        str: The binary representation of the decimal number.
    """
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary  # append the remainder to the binary string
        decimal //= 2  # integer division to get the quotient

    return binary

# Main program
while True:
    print("\nPlease select an option:")
    print("1. Convert binary to decimal")
    print("2. Convert decimal to binary")
    print("3. Quit the program")
    choice = input("> ")

    if choice == "1":
        binary = input("Enter a binary number: ")
        decimal = binary_to_decimal(binary)
        print(f"{binary} in decimal is {decimal}.")
    elif choice == "2":
        decimal = int(input("Enter a decimal number: "))
        binary = decimal_to_binary(decimal)
        print(f"{decimal} in binary is {binary}.")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select again.")
