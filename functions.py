def add_numbers():
    # Get user input
    number = (input("Enter a number: ")) 
    add_value = (input("Enter a value to add: "))

    # Perform the addition
    result = int(number) + int(add_value)

    # Output the result
    print(f"The result is: {result}")

# Call the function
add_numbers()
