price = int(input("Enter the price of the object: "))
payed = int(input("Enter the amount you have payed already: "))
due_amount= price - payed

for i in range(due_amount):
    print(i)
    pass
    break


print("You still need to pay", due_amount)