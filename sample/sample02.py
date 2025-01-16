#star pattern

num = int(input("Enter num: "))
for i in range(num):
    for j in range(i):
        print(" ", end="")
    for j in range(2 * (num - i) - 1):
        print("*", end="")
    print()
