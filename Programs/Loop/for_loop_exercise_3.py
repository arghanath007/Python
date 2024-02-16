pushups = int(input("Enter a number: "))
while True:
    if pushups == 50:
        print("Congratulations! You made it")
        break
    print("Are you tired?")
    reply = input("Enter y or yes and n or no: ")
    if reply == 'yes' or reply == 'y':
        print(f"You did total of {pushups} push-ups")
        break
    elif reply == 'no' or reply == 'n':
        print(f"The number of push-ups remaining are {50 - pushups} push-ups.")