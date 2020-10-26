def compute_bill(food):
    total = 0
    #Iterate through all items in list
    for item in food:
        # Check if stock is more than 0
        if stock[item] > 0:
            # Add price to total and substract 1 from stock
            total += prices[item]
            stock[item] = stock[item] - 1
    return total

groceries= ["banana","orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


print(compute_bill(groceries))
print(stock)