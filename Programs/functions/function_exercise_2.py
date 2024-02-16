number = int(input("Enter a number: "))
if number % 2 != 0: # Odd Number
    for i in range(1, number+1):
        for j in range(1, i + 1):
            print("* ", end= '')
        print()
else:
    for i in range(1, number + 1):
        for j in range(1, number + 2 - i):
            print("* ", end= '')
        print()



