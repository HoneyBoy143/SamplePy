num = int(input("Assign a number: "))
total = 0  # Initialize the accumulator variable
while num != 0:
    total += num  # Add the input number to the total
    print("Current sum:", total)
    num = int(input("Assign another number (or enter 0 to stop): "))  # Update num
