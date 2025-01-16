num = int(input("Enter num: "))
for i in range(num):
    for j in range(i):
        print("*", end="")
    print()