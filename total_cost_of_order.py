menu = {"Nachos": 6.00, "Pizza": 6.00, "Cheeseburger": 10, "Water": 4.00, "Coke": 5.00}
order = input().split()
total = 0
tax = 1.07

for i in order:
    if i in menu:
        total += menu[i]
    else:
        total += menu["Coke"]

print(round(total * tax, 2))
