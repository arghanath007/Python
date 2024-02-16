my_expenses = {'Clothes' : 1100, 'Shoes' : 1000,'Watch' : 1900, 'Mobile Recharge' : 699, 'Petrol' : 1980}

wife_expenses = {'Mobile Recharge' : 799,'DTH Recharge' : 999,'Clothes' : 2310,'Makeup' : 3670,'Shoes' : 999}

my_expenses_total = wife_expenses_total = 0
# print(type(my_expenses))
print(my_expenses['Clothes'])


for i in my_expenses:
    value = my_expenses[i]
    my_expenses_total += value
for i in wife_expenses:
    value = wife_expenses[i]
    wife_expenses_total += value
    
print(f'My expenses are {my_expenses_total} and my wife expenses are {wife_expenses_total}')

if my_expenses_total > my_expenses_total:
    print('I am spending more')
else:
    print('My wife is spending more')

my_expensive_item = my_expenses['Clothes']
for item in my_expenses:
    value = my_expenses[item]
    if value > my_expensive_item:
        my_expensive_item = my_expenses[item]

wife_expensive_item = wife_expenses['Clothes']
for item_w in wife_expenses:
    value = wife_expenses[item_w]
    if value > wife_expensive_item:
        wife_expensive_item = wife_expenses[item_w]

print(f'My most expensive item is {my_expensive_item} and my wife most expensive item is {wife_expensive_item}')











