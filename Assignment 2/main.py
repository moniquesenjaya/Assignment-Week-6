#Initializing the prices dictionary
prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
}

#Initializing the prices dictionary
stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
}

#Printing the key,price,stock using loop
for i in prices:
    print( i + "\nprice: " + str(prices[i]) + "\nstock: " + str(stock[i]) + "\n")

total = 0

#Looping through the two dictionaries to multiply the values and add to total
for i in prices:
    print(i + ": " + str(prices[i]*stock[i]))
    total += prices[i]*stock[i]

print("Total: " + str(total))