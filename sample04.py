num = int(input("Enter a number: "))
sum_of_cubes = 0
for i in range(1, num + 1):
    cube = i ** 3
    sum_of_cubes += cube
print(f"The sum of cubes from 1 to {num} is {sum_of_cubes}")
