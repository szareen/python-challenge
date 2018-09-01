import os
import csv

output_path = os.path.join('output', 'new.txt')

# Read the csv 

csvpath = os.path.join('Resources', 'budget_data.csv')
total_months = 0
prev_profit = 0
month_change = []
profit_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_netamount = 0

with open(csvpath) as budget_data:
    reader = csv.DictReader(budget_data)

    for row in reader:

        # Calculate the total
        total_months = total_months + 1
        total_netamount = total_netamount + int(row["Profit/Losses"])

        # Calculating the profit/losses change
        profit_change = int(row["Profit/Losses"]) - prev_profit
        prev_profit = int(row["Profit/Losses"])
        profit_change_list = profit_change_list + [profit_change]
        month_change = month_change + [row["Date"]]

        # Calculate the greatest increase
        if (profit_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = profit_change

        # Calculate the greatest decrease
        if (profit_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = profit_change

# Calculate the Average Revenue Change
average_change = sum(profit_change_list) / len(profit_change_list)

# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total : ${total_netamount}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(output_path, "w") as txt_file:
    txt_file.write(output)