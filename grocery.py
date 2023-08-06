items = list(map(str,input("Enter name of groceries: ").split()))
n = len(items)
d = {}
o_amnt = []
for i in range(n):
    print("\n")
    print("enter amount of ",items[i])
    amount = float(input("Enter amount of grocery in KG: "))
    o_amnt.append(amount)
    d[items[i]] = amount

print("\n")
print("Total Groceries:-")
print(d)
print("\n")

new = {}

for i in range(n):
    print("Enter new amount for ",items[i])
    new_amount = float(input("Enter new: "))
    d[items[i]] = new_amount
    if(float(new_amount) <= float(0.25*o_amnt[i])):
        new[items[i]] = new_amount
    else:
        continue

print("\n")
print("\33[31m ALERT! Follwing items are runnning low:-")
print(new,"\33[0m")
print("\n")