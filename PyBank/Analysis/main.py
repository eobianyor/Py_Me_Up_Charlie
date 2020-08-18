# import neccessary plugins
import os
import csv

# create a path
budget_data_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# initialize variables
monthCounter = 0
noOfMonths = 0
net_Amt = 0
delta_Amt = 0
pl_Amt = 0
max_Num = 0
incident_of_max_Num = None
min_Num = 0
incident_of_min_Num = None

# Open csv file
with open(budget_data_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')

    header = next(csv_reader)
    # Seed profit/loss amount (pl_Amt) so it cancels out for line 1
    pl_Amt = 867884

    for a,b in csv_reader:
        # Calculate the cum change in profit/Loss  
        delta_Amt = delta_Amt + (int(b) - pl_Amt)
        pl_Amt = int(b)
        
        # Get the month count  
        monthCounter = monthCounter + 1
        
        # Calculate net total profit/Loss
        net_Amt = net_Amt + int(b)
        
        # Retreive the greatest increase in profit
        if max_Num < int(b):
            max_Num = int(b)
            incident_of_max_Num = (a)
        
        # Retreive the greatest decrease in profit
        if min_Num > int(b):
            min_Num = int(b)
            incident_of_min_Num = (a)
    
# Calculate Average change
Av_change = (delta_Amt/(monthCounter - 1))
Av_PandL = (net_Amt/monthCounter)

# QC statements
print("Financial Analysis")
print("----------------------------------------- ")
print(f"Total no. of months: {monthCounter}")
print(f"Cumulative total: ${net_Amt:.2f}")
print(f"Average change: ${Av_change:.2f}")
print(f"Greatest increase in Profits: {incident_of_max_Num} (${max_Num:.2f})")
print(f"Greatest decrease in Profits: {incident_of_min_Num} (${min_Num:.2f})")

# print(f"Greatest increase in Profits occurs in {incident_of_max_Num}")
# print(f"Greatest decrease in Profits occurs in {incident_of_min_Num}")
# print(f"Cum change in profit/Loss is {delta_Amt}")
# print(f"Average profit/Loss is {Av_PandL}")