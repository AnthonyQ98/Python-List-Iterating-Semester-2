"""
Anthony Quinn X00138635
Lab 1
25 Jan 2021
"""

# EXERCISE ONE
"""
total_rainfall = 0
week_rainfall = []

for number in range(7):
    rainfall = float(input("Rainfall (in cm): "))
    week_rainfall.append(rainfall)
    total_rainfall += rainfall


for i in range(len(week_rainfall)):
    if week_rainfall[i] > 3.5:
        print("Rainfall exceeded 3.5cm on Day" + str(i + 1))

average_rainfall = total_rainfall / 7

print(total_rainfall)
print(round(average_rainfall, 2))
"""

# Exercise 2
"""
numbers = []

for i in range(5):
    number = float(input("Number: "))
    numbers.append(number)
print(numbers)

for x in range(len(numbers)):
    numbers[x] = numbers[x] + 1
print(numbers)
"""

# EXERCISE 3
"""
sales_total = 0
total_sales_list = []
num_salespeople = int(input("Number of salespeople: "))


print("Sales Person\t\t\tSales €")
print("-" * 32)
for people in range(num_salespeople):
    total_sales = float(input("Sales Person {0}:\t\t\t".format(people + 1)))
    total_sales_list.append(total_sales)
    sales_total += total_sales
print(("-" * 10) + "Summary" + ("-" * 10))

# AVERAGE SALE CALCULATION
average_sales = total_sales / num_salespeople

print("Total sales        : €", round(sales_total, 2))
print("Average sales      : €", round(average_sales, 2))
print("Maximum Sale       : €", max(total_sales_list))
print("Minimum Sale       : €", min(total_sales_list))
"""





