# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = "/Users/darianaibarra/Downloads/Starter_Code 6/PyBank/Resources/budget_data.csv"
file_to_output = "/Users/darianaibarra/Downloads/Starter_Code 6/PyBank/analysis/budget_data.txt"

# Define variables to track the financial data
total_months = 0
total_net = 0
monthly_profit_change = []
previous_profit = 0
greatest_increase = ["", 0]  # [month, amount]
greatest_decrease = ["", float("inf")]  # [month, amount]

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_profit = int(first_row[1])

    # Debugging output for the first row
    print(f"First Row: {first_row}, Total Net: {total_net}, Previous Profit: {previous_profit}")
   
    # Process each row of data
    for row in reader:
        # Increment the total months
        total_months += 1
   
    # Track the total and net change
    current_profit = int(row[1]) 
    total_net += current_profit

    # Track the net change
    change = current_profit - previous_profit
    monthly_profit_change.append(change)
    previous_profit = current_profit

    # Debugging output for each row
    print(f"Row: {row}, Current Profit: {current_profit}, Total Net: {total_net}, Change: {change}")

    # Calculate the greatest increase in profits (month and amount)
    if change > greatest_increase[1]:
        greatest_increase[0] = row[0]
        greatest_increase[1] = change

    # Calculate the greatest decrease in losses (month and amount)
    if change < greatest_decrease[1]:
        greatest_decrease[0] = row[0]
        greatest_decrease[1] = change
    
# Calculate the average net change across the months
if len(monthly_profit_change) > 0:  # Avoid division by zero
    average_change = sum(monthly_profit_change) / len(monthly_profit_change)
else:
    average_change = 0

# Generate the output summary
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
