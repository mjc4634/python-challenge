#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv
get_ipython().system('pwd')


# In[2]:


#create a list to read in our csv data
pypoll_data = []
#Define Path to csv file
PyPoll_path = os.path.join('election_data.csv')
#open the csv and read it to a variable
with open(PyPoll_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    csv_header = next(csv_reader)
    print("CSV Header: ", csv_header)
    
    for row in csv_reader:
        pypoll_data.append(row)
    print(pypoll_data[0:5])


# In[3]:


get_ipython().run_cell_magic('time', '', 'votes = 0\ndef vote_counter(data):\n    print_variable_1 = ("Total Votes:", len(data))\n    return print_variable_1\n\n\ndef canidate_counter(data):\n    #Total_votes = int(len(data))\n    canidates_list = []\n    c1 = 0\n    c2 = 0\n    c3 = 0\n    c4 = 0\n    counter = [[], [], [], []]\n    for i in data:\n      votes = i\n      canidates = i[2]\n      canidates_list.append(canidates)\n    #print(canidates_list)\n    for canidate in canidates_list:\n      if canidate == \'Khan\':\n        c1 = c1 + 1\n      if canidate == \'Correy\':\n        c2 = c2 + 1\n      if canidate == \'Li\':\n        c3 = c3 + 1\n      if canidate == "O\'Tooley":\n        c4 = c4 + 1\n            \n    total_votes = (c1+c2+c3+c4)\n    counter[0] = ("Khan: ", c1)\n    counter[1] = ("Correy: ", c2)\n    counter[2] = ("Li: ", c3)\n    counter[3] = ("O\'Tooley: ", c4) \n    if total_votes == 0:\n      no_votes = str("NO VOTES!")\n      return no_votes\n    Khan_percent = int(c1/total_votes*100)\n    Correy_percent = int(c2/total_votes*100)\n    Li_percent = int(c3/total_votes*100)\n    OTooley_percent = int(c4/total_votes*100)\n    \n    khan = ("Khan: " + str(Khan_percent) + ".000%  " + "(" + str(c1) + ")" )\n    correy = ("Correy: " + str(Correy_percent) + ".000%  " + "(" + str(c2) + ")" )\n    li = ("Li: " + str(Li_percent) + ".000%  " + "(" + str(c3) + ")" )\n    otooley = ("O\'Tooley: " + str(OTooley_percent) + ".000%  " + "(" + str(c4) + ")" )\n    \n    total_list = [c1,c2,c3,c4]\n    winner = max(total_list)\n    if winner == total_list[0]:\n        winner = ("Winner: Khan")\n        return [[khan, correy, li, otooley], winner]\n    elif winner == total_list[1]:\n        winner = ("Winner: Correy")\n        return [[khan, correy, li, otooley], winner]\n    elif winner == total_list[2]:\n        winner = ("Winner: Li")\n        return [[khan, correy, li, otooley], winner]\n    elif winner == total_list[3]:\n        winner = ("Winner: O\'Tooley")\n        return [[khan, correy, li, otooley], [winner]]\n    else: \n        print(\'No winner.\')\n        \n        \n\n#print(canidates_list[0:10])')


# In[4]:


#the output will write to csv
output_path = os.path.join("output", "new.csv")


with open(output_path, 'w', newline='') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['-------------------------------'])
    # Write the first row (column headers)
    csvwriter.writerow([vote_counter(pypoll_data)])
    csvwriter.writerow([canidate_counter(pypoll_data)])
##############


# In[ ]:





# In[ ]:




