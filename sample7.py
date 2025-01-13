import math

num = int(input("Enter a number: "))
sum = 0
for i in range(1, num + 1):
    sum += (i + 3) / math.factorial(i)
print(sum)