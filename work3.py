"""
Anthony Quinn
X00138635
28/01/2021
"""

# Question 1
"""
prices = [] # create empty list for 5 prices.
total_prices = 0

price_counter = 0
for i in range(5):
    price = float(input("Price {}: ".format(price_counter + 1)))
    price_counter += 1
    total_prices += price
    prices.append(price) # add to end of list.

# Calculating average price.
average_prices = total_prices / price_counter
print("The average price is: ", round(average_prices, 2))

print("Prices less than €5: ")
for price in prices: # display prices less than 5.
    if price < 5:
        print(price)

print("Higher than calculated average: ")
for price in prices: # displaying prices greater than average
    if price > average_prices:
        print(price)
"""
max_score = 0
scores = []
score_counter = 1
print("Enter 5 scores: ")

for i in range(5):
    score = int(input("Score {}: ".format(score_counter)))
    score_counter += 1
    scores.append(score)

print("The highest score is: ", max(scores))

for score in range(len(scores)):
    difference = max(scores) - scores[score]
    print("Score {}: ".format(score + 1), scores[score], "differs from max by", difference)





