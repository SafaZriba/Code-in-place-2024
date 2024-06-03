"""
Program: multiply two numbers
--------------------
This program asks the user for two
integers and prints the value of the first number
multiplied with the second
"""

def main():
    print("This program multiplies two numbers.")
    number_1 = int(input('Enter first number:'))
    number_2 = int(input('Enter second number:'))
    print(str(number_1 * number_2))


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()