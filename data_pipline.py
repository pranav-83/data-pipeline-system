from functools import reduce
from collections import defaultdict

sales = [
    ("Laptop", 800),
    ("Phone", 500),
    ("Tablet", 300),
    ("Laptop", 900),
    ("Phone", 550)
]

def group_helper(acc, item):
    product, price = item
    acc[product].append(price)
    return acc

def sum_helper(a, b):
    return a + b

def max_helper(acc, item):
    key, value = item
    if acc is None or value > acc[1]:
        return (key, value)
    return acc

def group_sales(data):
    return reduce(group_helper, data, defaultdict(list))

def calculate_averages(grouped):
    averages = {}
    for k, v in grouped.items():
        total = reduce(sum_helper, v)
        averages[k] = total / len(v)
    return averages

def calculate_totals(grouped):
    totals = {}
    for k, v in grouped.items():
        totals[k] = reduce(sum_helper, v)
    return totals

def highest_product(totals):
    result = reduce(max_helper, totals.items(), None)
    return result[0]

def display_grouped(grouped):
    print("\nGrouped Sales:")
    for k, v in grouped.items():
        print(k, ":", v)

def display_averages(averages):
    print("\nAverage Price per Product:")
    for k, v in averages.items():
        print(k, ":", round(v, 2))

def display_highest(totals):
    product = highest_product(totals)
    print("\nHighest Selling Product:")
    print(product, "with total =", totals[product])

def display_summary(grouped, totals, averages):
    print("\nSales Summary Report:")
    for k in grouped:
        print(f"{k} -> Total: {totals[k]}, Average: {averages[k]:.2f}")

def main():
    grouped = group_sales(sales)
    averages = calculate_averages(grouped)
    totals = calculate_totals(grouped)

    while True:
        print("\n--- MENU ---")
        print("1. Show Grouped Sales")
        print("2. Show Averages")
        print("3. Show Highest Selling Product")
        print("4. Show Summary Report")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            display_grouped(grouped)
        elif choice == "2":
            display_averages(averages)
        elif choice == "3":
            display_highest(totals)
        elif choice == "4":
            display_summary(grouped, totals, averages)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, try again.")

main()