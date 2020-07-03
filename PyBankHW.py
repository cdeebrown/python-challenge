#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import csv


# In[3]:


path = os.path.join("../Resources/budget_data.csv")


# In[4]:


path


# In[31]:


with open(path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    tot_months = 0
    csv_header = next(csvreader)
    net_profit = 0
    netchange_l = []
    greatest_increase = 0
    greatest_increase_month = ""

    greatest_decrease = 99999999999999999999
    greatest_decrease_month = ""
    
    for row in csvreader:
        
        tot_months = tot_months + 1
        net_profit = net_profit + int(row[1])
        netchange_l.append(int(row[1]))
        
        if greatest_increase < int(row[1]):
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
        
        if greatest_decrease > int(row[1]):
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]
    
    avg_change =sum(netchange_l)/len(netchange_l)
    
    print(f"Total Months = {tot_months}")
    print(f"The net profit/loss is ${net_profit}")
    print(f"Average change = ${avg_change:.2f}")
    print(f"Greatest increase = ${greatest_increase}, {greatest_increase_month}")
    print(f"Greatest decrease = ${greatest_decrease}, {greatest_decrease_month}")


# In[32]:


outpath = os.path.join("/Users/Smokey/python-challenge/PyBank/Analysis")
outpath


# In[ ]:




