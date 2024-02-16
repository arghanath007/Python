def pay_bill(expenses, percent_comm = 9.8, special_disc_amt=0):
    price =0
    for i in expenses:
        price += i
    comm = price * (percent_comm/100)
    special_disc = price * (special_disc_amt/100)
    payable_price = price - (comm + special_disc)
    return payable_price


expenses = [45, 342, 351,348,90,12]
comm = 5
special_offer_amt = 300
purchase = 500
if purchase > special_offer_amt:
    bill = pay_bill(expenses = expenses, percent_comm = comm, special_disc_amt= 1.2)
else:
    bill = pay_bill(expenses, comm)

print(f"The payable price of the bill is {bill}")