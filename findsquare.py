def square_number(number):
    # Calculate the square of the number
    return number ** 2

def main():
    # Get user input
    number = int(input("Enter a number: "))
    
    # Calculate the square
    result = square_number(number)
    
    # Output the result
    print(f"The square of {number} is: {result}")

# Call the main function
main()
