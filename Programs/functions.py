# def find_total(expenses):
#     total = 0
#     for expense in expenses:
#         total += expense
#     return total
#
# john_expenses = [445,232,54512,34,77774,790,56,12]
# matt_expenses = [12,343,56,900,34,789,1256,90]
#
# total = find_total(john_expenses)
# print(f"John's expenses is {total}")
# total = find_total(matt_expenses)
# print(f"Matt's expenses is {total}")

def find_cylinder_volume(height, radius):
    print(f"Radius = {radius}, Height = {height}")
    volume = 3.14 * radius ** 2 * height
    return volume

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
volume = find_cylinder_volume(radius = radius, height= height) # Python keyword argument.
print(f"The volume is: {volume}")












