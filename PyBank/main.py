# import neccessary plugins
import os
import csv

# create a path
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

# initialize variables
months = []
profitLoss = []
monthCounter = 0
noOfMonths = 0
net_Amt = 0
max_Num = 0
min_Num = 0

# Open csv file
with open(budget_data_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')

    header = next(csv_reader)
    # noOfMonths = len(list(budget_data_csv))

    for a,b in csv_reader:   
        # Get the month count  
        monthCounter = monthCounter + 1
        # Calculate net total profit/Losses
        net_Amt = net_Amt + int(b)
        # Retreive the greatest increase in profit
        max_Num = max(b)
        # Retreive the greatest increase in profit
        min_Num = min(b)

# Calculate Average change
Av_change = (net_Amt/monthCounter)

# QC statements
print(f"No of months is {monthCounter}")
print(f"Net profit is {net_Amt}")
print(f"Average change is {Av_change}")
print(f"Greatest Increase in Profits is: {max_Num}")
print(f"Greatest decrease in Profits is: {min_Num}")



# Calculate net total profit/Losses
    # for a,b in csv_reader: 
        # print(b)    
        # net_Amt = net_Amt + int(rows[1])
    # for rows in csv_reader: 
        # print(rows[1])    
        # net_Amt = net_Amt + int(rows[1])

# print(rows[1])



# import os
# import csv


# cereal_csv = os.path.join("..", "Resources", "cereal.csv")
# Crls=[]
# with open(cereal_csv, "r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter = ",")

#     header = next(csv_reader)
#     for row in csv_reader:
#         if float(row[7]) >= 5:
#             print(row[0])
#             # if you want to save these output rows
#             crls.append(row)
