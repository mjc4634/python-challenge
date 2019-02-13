#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[2]:


data_list = []
csvpath = os.path.join("budget_data.csv")

with open(csvpath, newline='') as csv_file:
    #csv reader 
    csvreader = csv.reader(csv_file, delimiter = ',')
    
    #print(csvreader)
    
    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')
    
    for row in csvreader:
        data_list.append(row)
    print(data_list[0:5])


# In[5]:


#calculate number of months
def month_counter(data):
    print_variable_1 = ("Total Months:", len(data))
    return print_variable_1
    
#calculates the net amount of profit
def profit_calc(csv_list):
    Total = 0
    for i in csv_list:
        monthly_total = int(i[1])
        Total = monthly_total + Total
    print_variable_2 = ('Total: $'+ str(Total))
    return print_variable_2
    

#calculates the change in profit over entire, and max and min
def chg(data):
    Total = 0
    money_list = []
    for i in data:
        monthly_total = int(i[1])
        Total = monthly_total + Total
        money_list.append(monthly_total)
    inc = int(max(money_list))
    dec = int(min(money_list))
    avg = float(Total/(len(data)))
    print_variable_3 = ("Average Change: $" + str("%.2f" % avg))
    #return print_variable_3
    month_tot = 0
    for i in data:
        month_tot = int(i[1])
        if month_tot == inc: 
            print_variable_4 =("Greatest Increase in Profits: ", i[0]+ " ($" + str(i[1]) + ")")
            #return print_variable_3, print_variable_4
        elif month_tot == dec: 
            print_variable_5 =("Greatest Decrease in Profits: ", i[0]+ " ($" + str(i[1]) + ")")
            return print_variable_3, print_variable_4, print_variable_5


# In[6]:


#the output will write to csv
output_path = os.path.join("output", "new.csv")


with open(output_path, 'w', newline='') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['-------------------------------'])
    # Write the first row (column headers)
    csvwriter.writerow([month_counter(data_list)])
    csvwriter.writerow([profit_calc(data_list)])
    csvwriter.writerow([chg(data_list)[0]])
    csvwriter.writerow([chg(data_list)[1]])
    csvwriter.writerow([chg(data_list)[2]])


# In[ ]:





# In[ ]:




