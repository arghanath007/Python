# number = int(input("Enter a number: "))

def odd_prime(number):
    count = 0
    if number > 1:
        if number % 2 != 0: # Odd Number
            for i in range(1, number//2):
                if number % i == 0:
                    count += 1
            if count <= 1:
                print(f"{number} is odd as well as prime number")
            else:
                print(f"{number} is odd but not prime number")
        else:
            print(f"{number} is not an odd number")
    else:
        print(f"{number} is less than 1")

for i in range(1, 11):
    odd_prime(i)
