# Code will read a comma separated text file containing monthly profit or loss data and produce
# financial analysis over the time frame printing to the screen and saving to file

# operating system
import os
# Comma Separated Values
import csv

# Variables
TotMonths = 0
Tot = 0
ChangeByMonth = []
CountMonths = []
LargestIncrease = 0
LargestIncreaseMonth = 0
LargestDecrease = 0
LargestDecreaseMonth = 0

# Path setting (This is the path on local Windows 10 machine given the current working folder)
path = os.path.join('Python-Challenge', 'PyBank', 'Resources', 'budget_data.csv')
# C:\Users\Tbbsp\TinaDataClass\Python-Challenge\PyBank

# with to open file and ensure it closes
with open(path, newline='') as csvfile:
    
    # Comma delimited file definition
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Deal with header
    csv_header = next(csvreader)
    row = next(csvreader)
    
    # Variables and calculations
    PrevRow = int(row[1])
    TotMonths += 1
    Tot += int(row[1])
    LargestIncrease = int(row[1])
    LargestIncreaseMonth = row[0]
    
    # Go through the rows
    for row in csvreader:
        
        # How many months are there
        TotMonths += 1
        
        Tot += int(row[1])

        # What are the changes
        revenue_change = int(row[1]) - PrevRow
        ChangeByMonth.append(revenue_change)
        PrevRow = int(row[1])
        CountMonths.append(row[0])
        
        # What is the largest increase we see
        if int(row[1]) > LargestIncrease:
            LargestIncrease = int(row[1])
            LargestIncreaseMonth = row[0]
            
        # what is the largest decrease we see
        if int(row[1]) < LargestDecrease:
            LargestDecrease = int(row[1])
            LargestDecreaseMonth = row[0]  
        
    # averaging the change
    average_change = sum(ChangeByMonth)/ len(ChangeByMonth)
    
    highest = max(ChangeByMonth)
    lowest = min(ChangeByMonth)

# Output to terminal
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {TotMonths}")
print(f"Total: ${Tot}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {LargestIncreaseMonth}, (${highest})")
print(f"Greatest Decrease in Profits:, {LargestDecreaseMonth}, (${lowest})")

# path for output creating output file (This is the path on local Windows 10 machine given the current working folder)
RevisedBudget = os.path.join('Python-Challenge', 'PyBank', 'Analysis', 'budget_data_revised.text')

# write the output
with open(RevisedBudget, 'w',) as OutPutFile:

    OutPutFile.write(f"Financial Analysis\n")
    OutPutFile.write(f"---------------------------\n")
    OutPutFile.write(f"Total Months: {TotMonths}\n")
    OutPutFile.write(f"Total: ${Tot}\n")
    OutPutFile.write(f"Average Change: ${average_change}\n")
    OutPutFile.write(f"Greatest Increase in Profits:, {LargestIncreaseMonth}, (${highest})\n")
    OutPutFile.write(f"Greatest Decrease in Profits:, {LargestDecreaseMonth}, (${lowest})\n")
