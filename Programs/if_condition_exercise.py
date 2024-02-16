height = float(input("Enter the height in meters:"))
weight = int(input("Enter the weight in Kgs:"))
bmi = weight/(height ** 2)
if bmi > 30:
    print("Obesity")
elif bmi > 25 and bmi < 29:
    print("Overweight")
elif bmi > 18.5 and bmi < 25:
    print("Normal")
elif bmi < 18.5:
    print("Underweight")

India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

USA = ["New York","Chicago","Las Vegas", "San Francisco"]

UK = ["London", "Manchester", "Liverpool", "Nottingham"]

city = input("Enter a city name: ")
if city in India:
    print(f"{city} belonged to India")
elif city in USA:
    print(f"{city} belonged to USA")
elif city in UK:
    print(f"{city} belonged to UK")
else:
    print(f"The county of the {city} cannot be determined")

# cityOne, cityTwo = input("Enter the name of two cities: ").split()
cityOne = input("Enter city: ")
cityTwo = input("Enter another city: ")
if cityOne in India and cityTwo in India:
    print(f"Both the cities are in India")
elif cityOne in USA and cityTwo in USA:
    print(f"Both the cities are in USA")
elif cityOne in UK and cityTwo in UK:
    print(f"Both the cities are in UK")
else:
    print("They don't belong to the same country")











