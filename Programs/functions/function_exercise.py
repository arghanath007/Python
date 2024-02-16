number = int(input("Enter a number: "))
count = 0
if number % 2 != 0: # Odd Number
    for i in range(1, number):
        if number % i == 0:
            count += 1
    if count <= 1:
        print(f"{number} is odd as well as prime number")
else:
    print(f"{number} is not an odd number")

