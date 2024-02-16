# def find_pe_and_pb(price, eps, book_value):
#     pe = price / eps
#     pb = price / book_value
#     return (pe, pb) # or return pe, pb

# pe_ratio, pb_ratio = find_pe_and_pb(price=100, eps=10, book_value=5)
# print(pe_ratio, pb_ratio) 

# This is a list of tuples
contacts = [('Tracy', 1536978520), ('Karen', 6987412360), ('Marci', 4123078952)]
# This is a dictionary
d_contacts = {'Tracy': 1536978520, 'Karen': 6987412360, 'Marci': 4123078952}
print(d_contacts['Marci'])
print(d_contacts.get('John')) # None Value is returned.
d_contacts['John'] = 5698741023
print(d_contacts['John'])
print(d_contacts)
del d_contacts['Tracy']
print(d_contacts)

print('argha' in d_contacts)
d = {'Rachael': {'location': 'India', 'address': '5 pally'}, 'John': {'location': 'USA', 'address': '5 pally'}}
print(d['John']['address'])
for name in d_contacts:
    print(name, d_contacts[name])
for name, phone in d_contacts.items(): ## .items() is getting us the key-value pairs.
    print(name, d_contacts[name])
    
print(d_contacts.keys())
print(d_contacts.values())
# print(d_contacts['John': 'Tracy']) # Error
print(type(d_contacts))
print(type(contacts))