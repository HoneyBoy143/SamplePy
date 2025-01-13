num = int(input("Enter number: "))

if num >= 90 and num <= 100:
    print("You got O")
elif num >= 80 and num <= 89:
    print("You got A+")
elif num >= 60 and num <= 79:
    print("You got B")
elif num >= 45 and num <= 59:
    print("You got C")
else:
    print("You failed!")