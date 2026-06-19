months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun")

sales = []
expenses = []

print("Enter Sales and Expenses for 6 Months\n")

for month in months:
    sale = float(input(f"Enter Sales for {month}: "))
    expense = float(input(f"Enter Expenses for {month}: "))

    sales.append(sale)
    expenses.append(expense)

def total_amount(data):
    return sum(data)

def average_amount(data):
    return sum(data) / len(data)

def calculate_profit(sales, expenses):
    profits = []

    for i in range(len(sales)):
        profits.append(sales[i] - expenses[i])

    return profits

profits = calculate_profit(sales, expenses)

total_sales = total_amount(sales)
total_expenses = total_amount(expenses)
total_profit = total_amount(profits)

average_sales = average_amount(sales)

best_month = months[sales.index(max(sales))]

profit_percentage = (total_profit / total_sales) * 100

print("\n")
print("=" * 40)
print("     BUSINESS FINANCIAL REPORT")
print("=" * 40)

print(f"Total Sales      : ₹{total_sales:,.2f}")
print(f"Total Expenses   : ₹{total_expenses:,.2f}")
print(f"Total Profit     : ₹{total_profit:,.2f}")

if total_profit > 0:
    print("Business Status  : PROFIT")
else:
    print("Business Status  : LOSS")

print(f"Average Sales    : ₹{average_sales:,.2f}")
print(f"Best Sales Month : {best_month}")
print(f"Profit Percentage: {profit_percentage:.2f}%")

print("\nMonthly Profit Report")
print("-" * 30)

for i in range(len(months)):
    print(f"{months[i]} : ₹{profits[i]:,.2f}")

print("=" * 40)
