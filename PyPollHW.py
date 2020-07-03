#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[2]:


pwd


# In[3]:


path = os.path.join("../Resources/election_data.csv")
path


# In[10]:


with open(path) as csvfile:
    polldata = csv.reader(csvfile, delimiter=",")
    csvheader = next(polldata)
    vote_total = 0
    Candidate = []
    print("Election Results!:")
    print("--------------------------------------------")
    for i in polldata:
        vote_total = vote_total + 1
        Candidate.append(i[2])
    print(f"Total amount of votes cast was: {vote_total}") 
    
    per_dict ={}
    can_dict ={}
    for i in set(Candidate):
        can_dict.update({i:0})
        per_dict.update({i:0})
    for i in Candidate:
        can_dict[i] += 1
        per_dict[i] += 1
    print("---------------------------------------------")
    for k,v in can_dict.items():
        print(f'{k} had {round(v * 100/vote_total)}% ({v})'.format(k,v))
print("--------------------------------------------------")    
print(f'The winner is {k}!')
print("---------------------------------------------------")


# In[ ]:


with open(outpath, w) as txtfile:
    
    


# In[ ]:




