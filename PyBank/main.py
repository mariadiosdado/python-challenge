import csv
import os

# read the csv file 
csvpath = os.path.join('BudgetData.csv')
csvoutput = os.path.join("output.txt")

total_months = 0
net_total_amount = 0
average_change = 0
net_change_list = []
months = []


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    csv_headers = next(csvreader)
    
    # Total number of months in BudgetData.csv
    # Net total amount of "Profit/Losses" over period
    # Changes in "Profit/Losses" over period, then average changes
    
    total_months +=1
    row1 = next(csvreader)
    prior_net = int(row1[1])
    net_total_amount += int(row1[1])
    
    for x in csvreader:
        months.append(x[0])
        total_months +=1
        net_total_amount += int(x[1])
        
        net_change = int(x[1]) - prior_net
        net_change_list.append(net_change)
        
        prior_net = int(x[1])
        
        #total_net_change = total_net_change + net_change
        average_change = sum(net_change_list) / len(net_change_list)
    
    print("Financial Analysis")
    print(f"-"*25)
    print(f"Total Months is : {(total_months)}")
    print(f"Total : ${net_total_amount}")
    #print (f"total net change is :{str(total_net_change)}")
    print (f"Average Change : ${str('%.2f' %average_change)}")
    print(f"Greatest Increase in Profits: {months[net_change_list.index(max(net_change_list))]} (${max(net_change_list)})")
    print(f"Greatest Decrease in Profits: {months[net_change_list.index(min(net_change_list))]} (${min(net_change_list)})")    
        
